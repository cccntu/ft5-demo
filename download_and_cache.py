from transformers import T5ForConditionalGeneration, T5TokenizerFast, pipeline
from transformers.models.f_t5.modeling_t5 import \
    T5ForConditionalGeneration as FT5ForConditionalGeneration
from transformers.models.f_t5.tokenization_t5_fast import \
    T5TokenizerFast as FT5TokenizerFast

model_name = 'flax-community/ft5-cnn-dm'
ft5_model = FT5ForConditionalGeneration.from_pretrained(model_name)
ft5_tokenizer = FT5TokenizerFast.from_pretrained(model_name)
ft5_summarizer = pipeline(
    "summarization", model=ft5_model, tokenizer=ft5_tokenizer, framework="pt"
)

