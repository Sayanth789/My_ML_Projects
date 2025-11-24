## Zero shot vs few shot learning 
### Are used in NLP and LLMs like GPT 

--------------------------------------------------------------
## Zero Shot learning 0️⃣ 🔥 🔫 
Zero-shot learning means the model performs a task **without seeing any examples of that
task during inference**
You can give **instructions** and the mdoel uses its general knowledge to solve the
task.

**Example** 
**Prompt**
Translate this sentence to French:
" I love machine learning."
Here **one didnot provinde any examples** of translation
The model still understands the tsak -> **Zero-shot**
### Why it works 
LLMs have been trained on huge datasets and learn general patterns. So they can follow instructions even without task-specific examples.

### Use cases 
* Classification without examples
* Translation
* Summarization
* Q & A
* Sentiment analysis

## Few shot Learning 
### Definition
Few-shot learning means the model is given a **few examples (typically 1–5)** in the prompt before performing the task.
You show the pattern and the model learns the task in `context`
### Example 
### Prompt
Translate the following to French 
English : I like apples 
Frecnch : J'aime les pomess.

English: We are friends
French : Nous sommes amis 

Engilish: I love machine learning.
French: 

### Why it helps 
* GIves the model a pattern
* Reduces mistakes
* Improves the accuracy for tasks the model is not explicitly trained for

### Use cases 
* new tasks model a pattern
* Reduces mistakes
* Improves accuracy for tasks the model is not explicitly trained for

###Use Cases 🧠 🇼🇫
* New tasks with few labels
* Custom classification
* Style imitaiton ("write like this ")
* Extracting fields from text

