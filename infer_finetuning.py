# @Time    : 2023/4/2 22:49
# @Author  : tk
# @FileName: infer

import torch
from deep_training.data_helper import ModelArguments, DataArguments, TrainingArguments
from transformers import HfArgumentParser, AutoConfig
from data_utils import train_info_args, NN_DataHelper, get_deepspeed_config
from aigc_zoo.model_zoo.internlm.llm_model import MyTransformer,InternLMConfig,InternLMTokenizer
# from aigc_zoo.utils.llm_generate import Generate

deep_config = get_deepspeed_config()


if __name__ == '__main__':
    parser = HfArgumentParser((ModelArguments, DataArguments))
    model_args, data_args  = parser.parse_dict(train_info_args, allow_extra_keys=True)

    dataHelper = NN_DataHelper(model_args, None, data_args)
    tokenizer, _, _,_= dataHelper.load_tokenizer_and_config()


    config = InternLMConfig.from_pretrained('./best_ckpt')
    pl_model = MyTransformer(config=config, model_args=model_args,torch_dtype=torch.float16,)

    # deepspeed 权重使用转换脚本命令
    # 一般根据时间排序选最新的权重文件夹
    # cd best_ckpt/last
    # python zero_to_fp32.py . ../last.ckpt

    train_weight = './best_ckpt/last.ckpt'
    pl_model.load_sft_weight(train_weight,strict=True)

    # 保存hf权重
    # config.save_pretrained('convert/')

    # 保存sft p-tuning-v2 权重
    #  pl_model.save_sft_weight('convert/pytorch_model_sft_ptv2.bin')

    # 保存sft权重
    # pl_model.save_sft_weight('convert/pytorch_model_sft.bin')

    model = pl_model.get_llm_model()

    if not model.quantized:
        # 按需修改，目前只支持 4/8 bit 量化 ， 可以保存量化模型
        model.half().quantize(4).cuda()
    else:
        # 已经量化
        model.half().cuda()

    text_list = ["写一个诗歌，关于冬天",
                 "晚上睡不着应该怎么办",
                 "从南京到上海的路线",
                 ]
    for input in text_list:
        response, history = model.chat(tokenizer=tokenizer,query=input,  max_new_tokens=512,
                                          eos_token_id=[2, 103028],
                                          do_sample=False, top_p=0.7, temperature=0.95, )
        print('input',input)
        print('output',response)