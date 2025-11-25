## THE MAIN HARDWARE / SYSTEM TECHNIQUES IN LLM TRAINING

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

## b) Pipeline Parallelism (PP)
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

## Key-Idea
**Compute attention without forming the huge attention matrix(T x T)**
























