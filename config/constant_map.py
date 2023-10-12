# -*- coding: utf-8 -*-
# @Time:  23:20
# @Author: tk
# @File：model_maps
from aigc_zoo.constants.define import (TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING)

__all__ = [
    "TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING",
    "MODELS_MAP"
]

MODELS_MAP = {
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

    'internlm-20b': {
        'model_type': 'internlm',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm-20b',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm-20b/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm-20b',
    },
    'internlm-chat-20b': {
        'model_type': 'internlm',
        'model_name_or_path': '/data/nlp/pre_models/torch/internlm/internlm-chat-20b',
        'config_name': '/data/nlp/pre_models/torch/internlm/internlm-chat-20b/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/internlm/internlm-chat-20b',
    },
}

# 按需修改
# TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING


