"""Model names to be used by the class KnowledgeEngine class."""

# Each is a dict:
# names: a list of potential synonyms for the model.
# sources: a list of one or more URLs of the source model file(s), if available.

# TODO: restructure into external format, perhaps a TSV or YAML

# OpenAI Models
# See https://platform.openai.com/docs/models/overview
MODEL_GPT_3_5_TURBO = {
    "names": ["gpt-3.5-turbo", "openai-gpt-3.5-turbo"],
    "sources": [""]
}
MODEL_TEXT_DAVINCI_003 = {
    "names": ["text-davinci-003", "openai-text-davinci-003"],
    "sources": [""]
}
MODEL_GPT_4 = {
    "names": ["gpt-4", "openai-gpt-4"],
    "sources": [""]
}
OPENAI_MODELS = [
    MODEL_GPT_3_5_TURBO,
    MODEL_TEXT_DAVINCI_003,
    MODEL_GPT_4,
]

# GPT4ALL Models
# See https://gpt4all.io/
GPT_4_ALL_J_1_3_GROOVY = {
    "names": ["ggml-gpt4all-j-v1.3-groovy"],
    "sources": ["https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin"],
}
GPT_4_ALL_L13B_SNOOZY = {
    "names": ["ggml-gpt4all-l13b-snoozy"],
    "sources": ["https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin"],
}
MPT_7B_CHAT = {
    "names": ["ggml-mpt-7b-chat"],
    "sources": ["https://gpt4all.io/models/ggml-mpt-7b-chat.bin"],
}
VICUNA_13B_1_1_Q4_2 = {
    "names": ["ggml-vicuna-13b-1.1-q4_2"],
    "sources": ["https://gpt4all.io/models/ggml-vicuna-13b-1.1-q4_2.bin"],
}
WIZARDLM_7B_Q4_2 = {
    "names": ["ggml-wizardLM-7B.q4_2"],
    "sources": ["https://gpt4all.io/models/ggml-wizardLM-7B.q4_2.bin"],
}
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

DEFAULT_MODEL = MODEL_GPT_3_5_TURBO["names"][0]
