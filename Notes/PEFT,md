# PEFT: Parameter-Efficient Fine-Tuning. 
A **family of techniques** that allow you to fine-tune very large language models without updating 
all of their parameters.
**Instead**, PEFT methods update only a tiny percentage (0.1%–3%) of the model parameters, while keeping the rest frozen.
PEFT allows you to adapt a large model to a new task by training ONLY a small number of additional parameters, while the original model weights stay fixed.

## Eg:

### LoRA (Low -Rank Adaptation) 
Replaces a large weight update with 2 small matrices:
  W + ΔW   →   W + (A · B)
Where A and B are low rank matrices. Only A and B are trainable , W stays frozen.

## QLoRA ( Quantized Low-Rank Adaptation).
### What it adds on top of LoRA ?
* Quantizes the model to **4-bit NF4**
* Stores LoRA adapters in **16-bit precision**
* Uses a **double quantization** trick to preserve accuracy.
## Advantages
* Fine-tune 7B–70B models on a single RTX 4090 or A100
* Minimal Memory footprint 
* High-quality results

## 🧩 Prefix Tuning
 ** What does it do**
Adds a small set of learnable vectors to the attention machanism.
[prefix vectors] + [input tokens]

Model weights stays frozen 
## Benefits
* Enable task specialization 
* Lightweight and fast 
* Useful for NLP tasks like summarization or QA
## Category 
** Algorithmic / Model-level method **

## 🧩 4. P-Tuning v2
Advanced form of prefix tuning using deeper trainable modules.
## Benefits 

* Works well for large models 
* High accuracy with small memory 

## Category 
**Model / Algorithm-level optimization ** 


## 🧩 5. Adapters

Adds small neural modules inside each Transformer layer.

## 📌 Highlights

* Only adapter layers are trained

* Base model stays frozen

* Popular in NLP before LoRA

## 📌 Category
Model - level traning strategy.



















