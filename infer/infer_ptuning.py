# @Time    : 2023/4/2 22:49
# @Author  : tk
# @FileName: infer_ptuning
import os
import torch
from deep_training.data_helper import ModelArguments, DataArguments
from transformers import HfArgumentParser,AutoConfig

from data_utils import train_info_args, NN_DataHelper
from aigc_zoo.model_zoo.internlm.llm_model import MyTransformer,PromptArguments,InternLMConfig,InternLMTokenizer
# from aigc_zoo.utils.llm_generate import Generate

if __name__ == '__main__':
    train_info_args['seed'] = None
    parser = HfArgumentParser((ModelArguments,))
    model_args, data_args = parser.parse_dict(train_info_args,allow_extra_keys=True)

    dataHelper = NN_DataHelper(model_args)
    tokenizer, _, _, _ = dataHelper.load_tokenizer_and_config()

    train_weight_dir = './best_ckpt/last'
    config = InternLMConfig.from_pretrained(train_weight_dir)
    prompt_args = PromptArguments.from_pretrained(train_weight_dir)

    assert prompt_args.inference_mode == True

    new_num_tokens = config.vocab_size
    if config.task_specific_params is not None and config.task_specific_params.get('vocab_size', None) is not None:
        config.vocab_size = config.task_specific_params['vocab_size']

    pl_model = MyTransformer(config=config, model_args=model_args, prompt_args=prompt_args,
                             torch_dtype=torch.float16,new_num_tokens=new_num_tokens,
                             )
    # 加载sft权重
    pl_model.load_sft_weight(train_weight_dir)

    pl_model.eval().half().cuda()

    model = pl_model.get_llm_model()

    #基础模型精度
    model.base_model_torch_dtype = torch.half

    text_list = ["写一个诗歌，关于冬天",
                 "晚上睡不着应该怎么办",
                 "从南京到上海的路线"]
    for input in text_list:
        response, history = model.chat(tokenizer=tokenizer, query=input, max_new_tokens=512,
                                       eos_token_id=[2, 103028],
                                       do_sample=False, top_p=0.7, temperature=0.95, )
        print('input', input)
        print('output', response)