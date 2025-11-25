**DPO (Direct Preference Optimization) is a machine learning technique used to fine-tune large language models to align with human preferences. Instead of using reinforcement learning, DPO directly optimizes the model based on a dataset of user-provided preferences, which consists of a prompt, a preferred response, and a rejected response. This method is computationally simpler and faster 
than traditional Reinforcement Learning from Human Feedback (RLHF).**
**It is an Alternative to the RLHF (Reinforcement Learning from Human Feedback) and is 
simpler , more stable and easier to implement**

## DPO was introduced because of ❗🤠 🔽
Traditional RLHF uses :
### 1. Supervised Fine-Tuning (SFT)
### 2. Reward Model Training 
### 3. PPO-Based RL Training 

The third step (PPO) is complex, unstable and expensive 
## DPO removes the PPO Step entirely.
It optimizes model behavior **directly from prefenrence data.**

### DPO uses paired preference data:
(prompt, chosen_response, rejected_response) 
HUmans (or automated systems ) choose which reponse is better.

**Then DPO trains the model to assign a `higher probability` to preferred answers (“chosen”) and `lower 
probability` to rejected answers.**

### Core idea 🧠 🌹 💦
DPO directly modifies the model's probability distributoin:
* Incrase : P(chosen | prompt )
* Decrease : P(rejected | prompt )
 **Mathematically it optimizes**
log π(chosen|x) - log π(rejected|x)

relative to the original SFT model.

* No reward model.
* No PPO.
* No RL loop.

Just **simple supervised training with a special loss function.**



























