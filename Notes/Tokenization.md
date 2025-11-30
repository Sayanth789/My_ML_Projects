Tokenization is the process of conerting the sesitive data into a unique, non-sensitive substitute 
called a "token" or breaking the text into smaller untis called **tokens**. In data security it is used
to protect things like credit card number by replacing them with a tokenthat has no intericic value and 
can't be used to acces the original informaation, which is stored securly elsewhere. In NNP (Natural 
Language Processing)  It's a fundamental step for breaking down text into smaller components like words
or characters to  be processed by the computer.

# * Purpose  🤠
* To prepare text data for analysis by machine learing models.
* What a token is : A token can be a word, a number or a punctuation mark. For eg: The sentence
  "I am learnin" can be tokenized into 3 tokens : "I", "am", "learning".
* Application : This is a crucial first step for many NLP tasks, such as Machine translation, sentiment analysis, and text
* summarization.
### Types of Tokenization 
* Whitespace tokenization
* Rule-based tokenization
* Statistical Tokenziation
* Byte- Pair Encoding
* Transformer based Tokenization


  As an eg: Consider the sentece "Chatbots are helpful" , when tokenized by words, it becomes.
  ["Chatbots", "are", "helpful"]
  IF toknenized by characters, it becomes:
  ["C", "h", "a", "t", "b", "o", "t", "s" , "a", "r", "e", "h", "e", "l", "p", "f", "u", "l"]

    Ecah approach has its own advanteage depending on the context and the specific NLP  task at hand.
  ### Types
  **Word Tokenization** : This is the most common , where text is divided into individual words. It works
  well for languages with clear word boundaries, like English

  **Sub-word Tokenization**: In this method text is split into individual characters. This is particulary useful for
  languages without clear word boudaries or for tasks that require a detailed analysis, such as spelling correction
  **Sentence Toknization** : Sentence tokenization is also a common technique used to make a division of paragraph
  or large set of seneteces into seperate seneteces as tokens

  **N-gram Tokenization** : N-Gram tokenization spit the word into a fixed-sized chunks (size = n) of data
  ## Use cases 🪛 🔩
   It is critical is nemerous applications , including :
  * **Information retrieval** : Tokenization is essential for indexing and searchin in systems that store and retrieve info:
  * efficiently based on the words or phrases
 
  * **Search Engines** : Use tokenization to process and undestand user queries. By breaking down the query into tokens , enhance
   match and return precise search results.
 
  *  **Machine Translation** : Tools like Google Translate rely on tokenization to convert senteces from one language into another,
    Segment and Reconstruct to preserve meaning .
 
  *  **Speech Recongnition** Voice assistant such as Siri and Alexa use tokenization to process spoken language. Command
    is first converted into text and then tokenized enalbing the system to understand and execute it accurately.

## Challenges Of Tokenization
Despite its importance, tokenization faces several challenges:
1 * **Ambiguity** : Human languages are inherently ambigous. A sentence like "I saw her duck" can have multiple 
meaning and iterpretaions depending on the tokenization and context.

2 **Languages Without Clear Boundaries** : Languags like Chinese and Japanese don't have clear word boudaries.
Making tokenization more complex.
3 **Special Characters** : Handling special characters such as punctuations, email address and URLs can be challenging.
For instance "John.doe@email.com" could be tokenized in multiple ways and interpretations , complicating 
the text anlaysis.
Advanced tokenization methods, like the BERT tokenizer, and techniques such as character or sub-word tokenization can help address these challenges.



    
