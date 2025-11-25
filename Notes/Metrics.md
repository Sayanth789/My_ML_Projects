### While these are the metrics that measures different things, but we can list them under a  single unmbrella 🏖️ ☔ ☔

## BLEU : (Billigual Evaluation Understudy) 
Purpose 
* Measures how close a generated text is to one more referecne (grond-truth) texts 
* Mostly used for **Machine learing** but also in summarization and text generation.

  #### How it works
  * BLEU comapres **n_grams** (1-gram, 2-gram, etc) between generated text and reference text
  * * It computes a precision based score
     * # Precision : " How many of the generated words appear in the refercne?"
 ## Range 
 * BLEU = 0 -> completely different
 * BLUE = 1 -> identical to reference (rare)

 ## ROGUE (Recall-Oriented Underdtudy for Gisting Evaluation) 
 **Purpose** 
 * Measures the quality of **Summaries** or **generated text*  with a focus on **recall**

 * Originally built for summarization(unlike BLEU which was for traslation)
### Hoe does it work 
* ROGUE counts how much of the reference text is covered by the generated  text.
*
### Popular variants

ROUGE-1: unigram overlap

ROUGE-2: bigram overlap

ROUGE-L: longest common subsequence

## Range:
* ROGUE = 0 -> no overlap
* ROGUE = 1 -> perfect overlap

##    Perplexity
** Purpose** 
* Measures how well a **language model ** predicts text
* Used during the **training of language models** *(GPTs, LSTM, etc)

  ### How it works
  * A language model outputs a probability for the next token
  * Preplexity = (Exponetial average negative log-likelihood)
  * Lower preplexity = better model

  # Interpretation
  * Preplexity can be thought of as:
    "On aberage, the model is as confused as if it had to choose between P equally likely options."
   ### Range
  * Preplexity = 1 -> perfect (predicts next token with certainnty)
  * Higher = worse
       
## Needle In a HayStack test 
**While it is slightly different from other metrics I still add it to here**
What does it do? : This measure how well a model handles **long input texts.**


## What is the Needle-in-a-Haystack Test?
Imagine giving an LLM a **very long document**, like 20, 000 tokens (huge) and then hiding a **single fact or sentence** somewhere deep inside it :
*.”`**
      This hidden fact is the **needle**
      The long document surrounding is the **haystack**
After providing the whole long text, you ask the model:
**"What is the secret password?**
If the model can **locate and recall** the hidden sentence , it passes the test.
##🧪 What Does It Measure?

The Needle-in-a-Haystack test evaluates **long-context retrieval**, which includes:
 ### 1 Attention quality
 can the model attend to details far back in the input?

 ### 3 Momory span 
 How many tokens can the model reliably track ( eg: 128k , 1M ,etc)?

 ### Information retention under noise.
Can it ignore the irrelevant text and fetch the required datail?

### 4 Context degradation 
Does accuracy drop the deeper the hidden needle is placed?

**Modern models claim very long context windows:**

* GPT-4o mini: 128k tokens

* Claude 3 Opus: 200k tokens

* Gemini 1.5 Pro: 1M+ tokens

* DeepSeek R1: >100k tokens

  But **long context doesn't mean good retrieval**
Many models have a long window but lose accuracy when the needle is far inside.

The NIAH test reveals: 
* Does the model **actually use** the long context?
* Does the model **forget** earlier parts?
* is the context window **real** or **degraded?**















 
 
























