# -*- coding: utf-8 -*-
# @Time:  23:20
# @Author: tk
# @File：model_maps

train_info_models = {
    'internlm-chat-7b': {
        'model_type': 'internlm',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b',
    },
    'internlm-chat-7b-8k': {
        'model_type': 'internlm',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b-8k',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b-8k/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b-8k',
    },
    'internlm-7b': {
        'model_type': 'internlm',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm-7b',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm-7b/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm-7b',
    },
    'internlm-chat-7b-int4': {
        'model_type': 'internlm',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b-int4',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b-int4/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm-chat-7b-int4',
    },

}


# 'target_modules': ['query_key_value'],  # bloom,gpt_neox
# 'target_modules': ["q_proj", "v_proj"], #llama,opt,gptj,gpt_neo
# 'target_modules': ['c_attn'], #gpt2
# 'target_modules': ['project_q','project_v'] # cpmant

train_target_modules_maps = {
    'internlm': ['q_proj','k_proj','v_proj'],
    'baichuan': ['W_pack'],
    'moss': ['qkv_proj'],
    'chatglm': ['query_key_value'],
    'bloom' : ['query_key_value'],
    'gpt_neox' : ['query_key_value'],
    'llama' : ["q_proj", "v_proj"],
    'opt' : ["q_proj", "v_proj"],
    'gptj' : ["q_proj", "v_proj"],
    'gpt_neo' : ["q_proj", "v_proj"],
    'gpt2' : ['c_attn'],
    'cpmant' : ['project_q','project_v'],
    'rwkv' : ['key','value','receptance'],
}

train_model_config = train_info_models['internlm-chat-7b']
