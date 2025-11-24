# This note explains how the Architectural Evolutions happened as of now.....🌹 👻
##FlashAttention (game changer) 
### Drastically reduces memory and speeds up training ...

####Used in ..
* GPT-4
* LLaMA 2/3
* Mistral
* Qwen

#RoPE (Rotatory Position Embeddings) 
A better alternative to absolute positional embeddings
Allows:
* Longer Context:
* Better extrapolatiion
* Better training stabilty

##Multi-Query Attention (MQA)/ Grouped Query Attention (GQA)
Reduces memory by sharing keys/values across heads
used by:
* PaLM
* GPT-4
* LLaMA 2

## Mixture-of-Experts (MoE)
Onlu a few **experts** activate per token 
-> Massive scale 
-> Lower inference cost 
-> Hgher quality

used in 
* Mistral
* Google's MoE models
* GPT-4 MoE variants (internal)
  
##Training Innocations
####RHLE (Reinforcement Learning from HUman Feedback) 
The technique that made ChatGPT possible 

Involves 
* Supervised fine-tuning
* Reward modeling
* Proximal policy optimization (PPO)

Gives : 
* Helpful
* Safe
* Aligned
* Conversational models

## RLAIF (Reinforcement Learning from  AI feedback ) 
AI models provide the feedback instead of humans .This massively reduces the cost 
## Self-Play / Self-Rewarding 
Models generates their own training data by:
* Asking themselves the question
* Corrcting their own answers
* Creatin synthetic datasets
Used in
* Deepseek
* Qwen
* OpenAI's internal models
  





