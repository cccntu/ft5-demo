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

#model_name = 'flax-community/t5-base-cnn-dm'
#t5_model = T5ForConditionalGeneration.from_pretrained(model_name)
#t5_tokenizer = T5TokenizerFast.from_pretrained(model_name)
#predict_t5 = get_predict(t5_model, t5_tokenizer)

def fn(text, do_sample, min_length, max_length,temperature, top_p):
    out =  ft5_summarizer(text, do_sample=do_sample, min_length=min_length,
    max_length=max_length, temperature=temperature, top_p=top_p,
    truncation=True)
    return out[0]['summary_text']
import gradio as gr

interface = gr.Interface(
    fn,
    inputs=[
        gr.inputs.Textbox(lines=10, label='text'),
        gr.inputs.Checkbox(label='do_sample'),
        gr.inputs.Slider(1, 128, step=1, default=64, label='min_length'),
        gr.inputs.Slider(1, 128, step=1, default=64, label='max_length'),
        gr.inputs.Slider(0.0, 1.0, step=0.1, default=1, label='temperature'),
        gr.inputs.Slider(0.0, 1.0, step=0.1, default=1, label='top_p'),
    ], 
    outputs=gr.outputs.Textbox(),
    server_port=17860,
    server_name='0.0.0.0',
)

interface.launch()
