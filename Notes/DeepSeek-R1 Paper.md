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

## What does the Pipeline contains 🛜
**It contains 4 stages**
### 1 Cold start 

**In this work, they collect thousands of cold-start data to fine-tune the DeepSeek-V3-Base as the starting point for RL. Compared to DeepSeek-R1-Zero, the advantages of cold start data include**

* Readability
* Potential

##    Reasoning-oriented Reinforcement Learning
This phase focused on enhancing the model’s reasoning capabilities, particularly in reasoning-intensive tasks such as coding, mathematics, science, and logic reasoning, which involve well-defined problems with
clear solutions. 

## Rejection Sampling and Supervised Fine-Tuning
When reasoning-oriented RL converges, thy utilized the resulting checkpoint to collect SFT (Supervised Fine-Tuning) data for the subsequent round. Unlike the initial cold-start data, which primarily focuses on reasoning, this stage incorporates data from other domains to enhance the model’s capabilities in writing, role-playing, and other general-purpose tasks. 

## Reinforcement Learning for all Scenarios
o further align the model with human preferences, they implemented a secondary reinforcement learning stage aimed at improving the model’s helpfulness and harmlessness while simultaneously refining its reasoning capabilities. Specifically, we train the model using a combination
of reward signals and diverse prompt distributions. For reasoning data, they adhere to the methodology outlined in DeepSeek-R1-Zero, which utilizes rule-based rewards to guide the learning process in math, code, and logical reasoning domains. 


** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *** ** ** ** ** ** ** ** 














