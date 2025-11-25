## THE MAIN HARDWARE / SYSTEM TECHNIQUES IN LLM TRAINING 🤖 🤘

LLM training is fundamentally a **hardware-bound problem**. As model sizes grow (tens to hundreds of billions of parameters), training becomes bottlenecked by GPU memory, compute throughput, and interconnect bandwidth.
This document summarizes the key **hardware-related techniques** that make large-scale training possible.

## Tensor Parallelsim 
Split the large matrix multiplication across multiple GPUs
Most transformer layers (especially attention proejction and feedforward layers) involves extremely large matrix multiplications that may not fit in a single GPU's memory.
### How it works 
* Break large matrix into slices
* Each GPU conputes partial results
* Results are combined ( all-reduce)
### Hardware dependences 
This requires high-bandwidth GPUs links (NVlikns/NVSwitch) , because GPUs exchange large tensors  during forward/backward passes. 


## Model Parallelism (MP) 
Split the model across multiple GPUs because it doesn't fit on one.
## Types of model parallelism:
## a) Tensor Parallelism (TP)
Split **a single matrix** across GPUs

Example:
Attention projection matrix is huge (like 12k × 12k).
Instead of storing it on one GPU:
* Split into 4 slices
* Each GPU computes partial results
* Results are combined

Used by :
* Megatron-LM

* GPT-NeoX

*  Llama v2/v3

* DeepSpeed

## b) Pipeline Parallelism (PP)  🏗
Split the **layers** across GPUs

Example 
* GPU 1 -> layers 0-10
* GPU 2 -> layers 11-20
* GPU 3 -> layers 21-30
Micro-batching allows GPUs to work in parallel instead of idle.

 #### Problem:

#### Pipeline bubbles
(when one GPU waits for another)

  
# c) Sequence Parallelism (SP)
Split input tokens across GPUs.
Useful when sequence length is huge (long context models).

--------------------------------------------------------------
## FlashAttention 
This  is a high efficient implementation of multi-head attention.
Is a **hardware-aware** algorithm that optimizes attention by:
* Using GPU shared memory (SRAM) as a tiling buffer
* Eliminating the need to store the full attention matrix (L × L)
* Reducing memory usage by 2–3×
* Increasing speed significantly (up to 2×) 

It highly exploits 
* Tensor Cores
* Warp-level parallelism
* High-bandwidth SRAM inside modern GPUs

## Key-Idea
**Compute attention without forming the huge attention matrix(T x T)**
Essential for Llama 2/3, Mistral, GPT-family models.

## Low-Precision Compute( FP16, BF16, FP8)
Modern GPUs support specialized low-precision formats to reduce memory and increase throughput.


## GPU Memory Bandwidth & HBM Limits
LLM training performance depends heavily on:
**HBM bandwidth (High-Bandwidth Memory)**
**Per-GPU memory capacity (40GB, 80GB, 141GB)**

Memory limits direcly constrain:
* Maximum model size per GPU
* Activation size
* Sequence length
* Number of micro-batches

##  KV Cache Hardware Considerations

During inference, LLMs store Key/Value tensors from attention layers.


















