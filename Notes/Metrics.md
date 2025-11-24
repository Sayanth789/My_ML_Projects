#### While these are the metrics that measures different things, but we can list them under a 
#### single unmbrella 🏖️ ☔ ☔

# BLEU : (Billigual Evaluation Understudy) 
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

 # ROGUE (Recall-Oriented Underdtudy for Gisting Evaluation) 
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

#    Perplexity
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
       
