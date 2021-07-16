import json
from datasets import load_dataset

dataset = load_dataset("cnn_dailymail", "1.0.0")

examples = dataset["test"][:10]
with open("examples.json", "w") as f:
    json.dump(examples, f)
