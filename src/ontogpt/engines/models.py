"""Model names to be used by the class KnowledgeEngine class."""

# Each is a list of potential synonyms for the model.

# OpenAI Models
# See https://platform.openai.com/docs/models/overview
MODEL_GPT_3_5_TURBO = ["gpt-3.5-turbo", "openai-gpt-3.5-turbo"]
MODEL_TEXT_DAVINCI_003 = ["text-davinci-003", "openai-text-davinci-003"]
MODEL_GPT_4 = ["gpt-4", "openai-gpt-4"]
OPENAI_MODELS = [MODEL_GPT_3_5_TURBO, MODEL_TEXT_DAVINCI_003, MODEL_GPT_4]

# GPT4ALL Models
# See https://gpt4all.io/
GPT_4_ALL_J_1_3_GROOVY = ["ggml-gpt4all-j-v1.3-groovy"]
GPT_4_ALL_L13B_SNOOZY = ["ggml-gpt4all-l13b-snoozy"]
MPT_7B_CHAT = ["ggml-mpt-7b-chat"]
VICUNA_13B_1_1_Q4_2 = ["ggml-vicuna-13b-1.1-q4_2"]
WIZARDLM_7B_Q4_2 = ["ggml-wizardLM-7B.q4_2.bin"]
GGML_MODELS = [
    GPT_4_ALL_J_1_3_GROOVY,
    GPT_4_ALL_L13B_SNOOZY,
    MPT_7B_CHAT,
    VICUNA_13B_1_1_Q4_2,
    WIZARDLM_7B_Q4_2,
]

MODELS = [
    MODEL_GPT_3_5_TURBO,
    MODEL_TEXT_DAVINCI_003,
    MODEL_GPT_4,
    GPT_4_ALL_J_1_3_GROOVY,
    GPT_4_ALL_L13B_SNOOZY,
    MPT_7B_CHAT,
    VICUNA_13B_1_1_Q4_2,
    WIZARDLM_7B_Q4_2,
]

DEFAULT_MODEL = MODEL_GPT_3_5_TURBO[0]
