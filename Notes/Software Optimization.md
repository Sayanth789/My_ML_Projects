### Data Parallelism (DP) 
Each GPU gets different baches of data but trains the same full model.

## How It Works 
* Suppose we have 8 GPUs
* Copy entire model -> each GPU
* Split batch across GPUs
* Each GPU processes forward + backward
* Gradients are **averaged** across GPUs(all-reduce)
* All GPUs update weights synchronously

## Pros 
* Simple
*  Scales well for small models
## Cons
* If model is too large to fit on a single GPU → **data parallelism fails**
* Gradient sharing becomes expensive
