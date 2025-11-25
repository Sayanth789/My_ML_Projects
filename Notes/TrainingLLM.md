## 3 main Stages Of LLM Training
## 1 Pre-training (Foundation of LLM) 
### Goal : 
Teach the model general language understanding 
 ## Data 
 Massive , diverse text:
 * Books
 * Websites
 * code
 * Articles
 * conversations

 ### Task 
 Self-supervised learning ( no manual labels) 
 Most common objectives:
 * #### Next Token Prediction (autoregressive)
   "" The cat sat on the _ " -> model predicts next token 
* ### Masked Language Modeling ( BERT --style)
* Grammar
* World knowledge
* reasoning between words
* relationship between  words
* representations of language
### Compute 
This is the expensive step (GPUs + weeks or months) 

## 2 Susepervised Finetuning 
### Goal 
Teach the model how to follow human instructions 

#### Data 
A smaller dataset containing: 
* Instructions -> responses
* chat conversations
* summaries , explanations
* question answering

Eg:
Iput : "Explain Newton's 2nd law"
Output : "Newtion's 2nd Law states that F = ma ... "

**Here the mdoel learns:** 
* how to respond like a helpful assistant
* how to format answers
* how to follow task instructions
* how to stay on topic  

## 3 RLHF ( Reinforcement Learning From Human Feedback) 
#### Goal 
* Safer
* more aligned
* less likely to hallucinate
* more helpful

This happens in 2️⃣ steps 
### A) Rward Model (RM) Training 
Humans rate LLM response:
* Which answer is better
* Which is safer?
* Which is more helpful?

Eg: 
Prompt : "Explain black holes"
Model Response A: ...
Model Response B: ....
Human picks the bset.

The model learns a **reward system** that approximates human preferences.
### b) RL Training (PPO, DPO, etc.)
The LLM generates the responses -> the Reward Model scores them -> 
RL algorithm (like PPO) adjusts the LLM to maximize the reward 

This is how the model learns 
* politness
* non-toxicity
* avoding dangerous content
* giving structured , helpful answers

### 🔎 Optional Step: Continued Training / Domain Adaptation
Sometimes comapnies add : 

* Domain Fine-tuning
* Tool -use fine tuning
* Long context fine-tuning
* Multimodal training (images/videos/audio)



  




















  
