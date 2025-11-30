##Notes 
The **earlier** models (like the original Transformer paper, 2017) used the full encoder decoder
architecture.
 ##**The Encoder** -> Process the input 
 ##**The Decoder** -> Generates the output

 ![alt text]( Transformer,_full_architecture(1).png)



 This is used for tasks like **machine translation** where the input and output are different sequences.
 Examples : 
 * Original Transformer
 *  T5
 *  BART

####But Nowdays the LLM uses only "decoders"
Modern large language models (LLMs)
 * GPT-3/ GPT-4/GPT-5
 * LLaMA
 * Mistral
 * Falcon
 * Qwen
 * Claude
 use **decoder-only** transformers.
 Because LLMs are trained to :
* Predict the next token
* Work in an autoregressive manner
* Generate text one token at a time
 The **decoder** has masked self-attention , which is prefered for next-token prediction.

##Transformers are built entirely on "Attention"
They replaced the RNNs/LSTM by using:
* Self-attention
* MultiHead attention
* Layer Normalization
* Feed-Forward blocks
 This allowed:
* Parallel processing
* Long-range dependencies
* Massive scaling

#Tokenization matters

Models understand text in "tokens", not in characters or words.

Differnet tokenizers.
* BPE
* WordPie
* SentencePie
* TikToken (OpenAi optimized)

## A good tokenizer improves:
* vocabulary efficiency
* Speed
* Mepory   
* Performance

