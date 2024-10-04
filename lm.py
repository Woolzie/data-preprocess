# Load model directly
import torch
from datasets import load_dataset, Dataset, Features, Sequence, ClassLabel, Value, Array2D
from transformers import AutoModel
model = AutoModel.from_pretrained("microsoft/layoutlmv3-base")

tokenizer = AutoTokenizer.from_pretrained("microsoft/layoutlmv3-base")
model = AutoModelForTokenClassification.from_pretrained("microsoft/layoutlmv3-base")

# encoding = 