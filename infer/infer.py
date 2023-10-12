# @Time    : 2023/4/2 22:49
# @Author  : tk
# @FileName: infer
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import torch
from deep_training.data_helper import ModelArguments, DataArguments
from transformers import HfArgumentParser, BitsAndBytesConfig
from data_utils import train_info_args, NN_DataHelper, get_deepspeed_config,global_args
from aigc_zoo.model_zoo.internlm.llm_model import (MyTransformer,InternLMConfig,InternLMTokenizer,
                                                   RotaryNtkScaledArguments,RotaryLinearScaledArguments)
# from aigc_zoo.utils.llm_generate import Generate

deep_config = get_deepspeed_config()

if __name__ == '__main__':
    parser = HfArgumentParser((ModelArguments,))
    (model_args, ) = parser.parse_dict(train_info_args, allow_extra_keys=True)

    dataHelper = NN_DataHelper(model_args)
    tokenizer, config, _,_= dataHelper.load_tokenizer_and_config()
    config.pad_token_id = config.eos_token_id

    enable_ntk = False
    rope_args = None
    if enable_ntk:
        rope_args = RotaryNtkScaledArguments(name='rotary_emb', max_position_embeddings=2048, alpha=4)  # 扩展 8k
        # rope_args = RotaryLinearScaledArguments(name='rotary_emb',max_position_embeddings=2048, scale=4) # 扩展 8k

    pl_model = MyTransformer(config=config, model_args=model_args,torch_dtype=torch.float16,rope_args=rope_args)

    model = pl_model.get_llm_model()
    model = model.eval()
    model.requires_grad_(False)
    if not model.quantized:
        # 按需修改，目前只支持 4/8 bit 量化 ， 可以保存量化模型
        model.half().quantize(4).cuda()
        # 保存量化权重
        # model.save_pretrained('internlm-chat-7b-int4',max_shard_size="4GB")
        # exit(0)
    else:
        # 已经量化
        model.half().cuda()

    text_list = ["写一个诗歌，关于冬天",
                 "晚上睡不着应该怎么办",
                 "从南京到上海的路线",
                 "登鹳雀楼->王之涣\n夜雨寄北->",
                 "Hamlet->Shakespeare\nOne Hundred Years of Solitude->",
                 ]
    for input in text_list:
        response, history = model.chat(tokenizer=tokenizer, query=input, max_new_tokens=512,
                                       eos_token_id=[2, 103028],
                                       do_sample=False, top_p=0.7, temperature=0.95, )
        print('input', input)
        print('output', response)