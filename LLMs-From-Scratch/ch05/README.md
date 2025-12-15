## Chapter 5: Pretraining on Unlabeled Data 

### Main Chapter Code 

* [ch05.ipynb] // contains all the code as it appears in the chapter
* previous_chapters.py is a Python module that contains the MultiHeadAttention module and GPTModel class from the previous chapters,
 which we import in ch05.ipynb to pretrain the GPT model
* gpt_download.py contains the utility functions for downloading the pretrained GPT model weights

  ##### Optional Code

  * gpt_train.py is a standalone Python script file with the code that we implemented in ch05.ipynb to train the GPT model
   (you can think of it as a code file summarizing this chapter)
 *  gpt_generate.py is a standalone Python script file with the code that we implemented in ch05.ipynb to load and use the
   pretrained model weights from OpenAI
