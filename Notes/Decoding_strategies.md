## Greedy-Search 😠 😈
### What it does:
Greedy decoding always picks the **single most probable next token** at every time step.

**Example** 
If the model predicts the token probabilities:
 * "the" -> 0.60
 * "a" -> 0.30
 * "this" -> 0.10


   ### Greedy always chooses -> "the".

   ## Characteristics
   * Fastest decoding method
   * Determinstic (always gives the same output)
   * Can get stuck in local optima  ->  **not always the best overall sentence**
  ## Use Cases 
  * When need **Speed** 🚗 🔥
  * Wnen  **Determinism** is important
  * When model quality is already high

 ## Beam Search 🕵️ 🕵️‍♂️
 ### Use case 
 Beam Search keeps **k (beam size)** number of candidates sequences at every step 

 Example:
 If beam size = 3:
 
 At every step:
 * Expand all 3 cadidates
 * Keep only the top 3 highest-scoring sequences
 * Repeat

   ## Why Beam Search Helps
   * Better translations
   * Better summarization
   * Reduces the chance of bad local choices

     ## Use cases 🗳️
     * Translation
     *  Summarization
     * Dialogue response when quality > speed

 ## Sampling .

  ### What it does.
 Instead of picking the highest probability , sampling **randomly chooses the next token
 proportional to its probability.**  

 Example (same probabilites) 
 * the (0.60)
 * a (0.30)
 * this (0.10)

Samplig might choose:
 * "the" , or
 * "a" or
 * (rarely) "this"

 ## Characteristics
 * Stochastic (not deterministic)
 * Create **more varied ,creative , diverse** text
 * Can become incoherent if randomness too high.
 * Usually combined with:
 * **Top-k sampling**
 * **Top-p (nucleus) sampling**
 * **Temperature scaling**

 ## Use cases
 * Story generation
 * Chatbots that need creativity
 * Dialog generation
 * Any generative task needing variery
   
 ## Note 📓 📓
 Temperature is a **hyperparameter** used during **sampling-based decoding** that controls how random or confident a
 model is when generating the next token.
It **reshapes the probability distribution** output by the model before sampling a token.

**Low Temperature (< 1)** -> model  becomes **more confident** , less random 

**High Temperature (> 1)** -> model  becomes **more random** , less creative
**Temperature = 1** -> normal probabilies (no change) 


















