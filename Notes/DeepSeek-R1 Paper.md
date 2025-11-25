# 🔑 Points / Ideas 
##1️⃣ Pure RL ( No Supervised Fine-Tuning) for Reasoning
* * They trained a model called **Deepseek-R1-Zero** using just reinforcement learning, without
*  any SFT at first
* * This model shows emergent reasoning behaviors : self-reflection, verification , chain-of-thought.
 
## 2️⃣ Multi-Stage Training Pipeline 
* To fix issues like `language mixing` and readability , they introduce **DeepSeek-R1**
* this pipeline includes: cold-supervied data, then **RL** then SFT again , then another RL.

* ## 3️⃣GRPO  (Group Relative Policy Optimization)
* They use GRPO as the RL algorithm rather than PPO.
* GRPO helps them scale RL and optimize reasoning.

## 4️⃣   Distialltions to smaller models
* They distill reasoning from the large DeepSeek-R1 into smaller dense models (Qwen, llama).
* * These distilled models performs well on reasoning tasks, showing that the  "reasoning patrerns" can transfer.
 
## 5️⃣ Evaluation Results 
* Huge gains on reasoning benchmark: for example , DeepSeek-R1-Zero's math performance is very
* high after RL
* * Their full R1 model is **compatible to OpenAI's o1** model on reasoning tasks.

## ⚠️ Critical Notes :

*  Because R1-Zero is trained purely with RL, there's a risk of **nnatural or weird reasoning styles**
 (they themselves admit language mixing, etc.)

* Distillation is very powerful: smaller models get reasoning ability without needing as much RL compute.  


