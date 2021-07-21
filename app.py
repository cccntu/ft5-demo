import os
from transformers import T5ForConditionalGeneration, T5TokenizerFast, pipeline
from transformers.models.f_t5.modeling_t5 import (
    T5ForConditionalGeneration as FT5ForConditionalGeneration,
)
from transformers.models.f_t5.tokenization_t5_fast import (
    T5TokenizerFast as FT5TokenizerFast,
)

import json

with open("examples.json") as f:
    examples = json.load(f)["article"]

model_name = "flax-community/ft5-cnn-dm"
ft5_model = FT5ForConditionalGeneration.from_pretrained(model_name)
ft5_tokenizer = FT5TokenizerFast.from_pretrained(model_name)
ft5_summarizer = pipeline(
    "summarization", model=ft5_model, tokenizer=ft5_tokenizer, framework="pt"
)

model_name = "flax-community/t5-base-cnn-dm"
t5_model = T5ForConditionalGeneration.from_pretrained(model_name)
t5_tokenizer = T5TokenizerFast.from_pretrained(model_name)
t5_summarizer = pipeline(
    "summarization", model=t5_model, tokenizer=t5_tokenizer, framework="pt"
)


def _fn(text, do_sample, min_length, max_length, temperature, top_p, summarizer):
    out = summarizer(
        text,
        do_sample=do_sample,
        min_length=min_length,
        max_length=max_length,
        temperature=temperature,
        top_p=top_p,
        truncation=True,
    )
    return out[0]["summary_text"]


def fn(*args):
    return [_fn(*args, summarizer=s) for s in (t5_summarizer, ft5_summarizer)]


import gradio as gr
PORT = os.environ.get('PORT', None)
PORT = int(PORT) if PORT is not None else None

interface = gr.Interface(
    fn,
    inputs=[
        gr.inputs.Textbox(lines=10, label="article"),
        gr.inputs.Checkbox(label="do_sample", default=True),
        gr.inputs.Slider(1, 128, step=1, default=64, label="min_length"),
        gr.inputs.Slider(1, 128, step=1, default=64, label="max_length"),
        gr.inputs.Slider(0.0, 1.0, step=0.1, default=1, label="temperature"),
        gr.inputs.Slider(0.0, 1.0, step=0.1, default=1, label="top_p"),
    ],
    outputs=[
        gr.outputs.Textbox(label="summary by T5"),
        gr.outputs.Textbox(label="summary by F-T5"),
    ],
    examples=[[ex] for ex in examples],
    server_port=PORT,
    title="F-T5 News Summarizer",
    description="""
F-T5 is a hybrid encoder-decoder model based on T5 and FNet.
The model architecture is based on T5, except the encoder self attention is replaced by fourier transform as in FNet.
The model is pre-trained on openwebtext, fine-tuned on CNN/DM. See the README for more detail: https://github.com/cccntu/ft5-demo.
""",
)

interface.launch()
