**Recurrent Neural Network Grammars (RNNGs)** : A new generative probabilistic model of sentences that explicitly mod-
els nested, hierarchical relationships among words and phrases 😃
🚀 . RNNGs operate via a recursive syntactic process reminiscent of probabilistic context-free
grammar generation, but decisions are parameterized using RNNs that condition on the entire syntac-
tic derivation history, greatly relaxing context-free independence assumptions.
🌹RNNGs maintain the algorithmic convenience of transition-
based parsing but incorporate top-down (i.e., root- to-terminal) syntactic information
#RNN Grammars:
Formally, an RNNG is a triple (N, Σ, Θ) consisting of a finite set of nonterminal symbols (N ), a finite
set of terminal symbols (Σ) such that N ∩ Σ = ∅, and a collection of neural network parameters Θ. 
It does not explicitly define rules since these are implicitly characterized by Θ. 

#Parser Transition:
The parsing algorithm transforms a sequence of words x into a parse tree y using two data structures
(a stack and an input buffer).
As with the bottom up algorithm of Sagae and Lavie  our algorithm begins with the stack (S) empty and the com-
plete sequence of words in the input buffer (B). The buffer contains unprocessed terminal symbols, and
the stack contains terminal symbols, “open” nonterminal symbols, and completed constituents. At each
timestep, one of the following three classes of operations  is selected by a classifier, based on
the current contents on the stack and buffer.

**(Note that refer the page to see the real data: The image and tabels are quite informational and the 
additional information is harder to provider , even it done it is meaningless without images and tables, thus we omit
the discussion here)**

#Generator Transition
The parsing algorithm that maps from sequences of words to parse trees can be adapted with mi-
nor changes to produce an algorithm that stochastically generates trees and terminal symbols. Two
changes are required: (i) there is no input buffer of unprocessed words, rather there is an output buffer
(T ), and (ii) instead of a SHIFT operation there are GEN(x) operations which generate terminal symbol
x ∈ Σ and add it to the top of the stack and the output buffer.
At each timestep an action is stochastically selected according to a conditional distribution
that depends on the current contents of S and T.

RNNGs can be combined with a particle filter inference scheme (rather than the importance sampling
method based on a discriminative parser, §5) to produce a left-to-right marginalization algorithm that
runs in expected linear time. Thus, they could be used in applications that require language models.

A second possibility is to replace the sequential generation architectures found in many neural net-
work transduction problems that produce sentences conditioned on some input. Previous work in ma-
chine translation has showed that conditional syntactic models can function quite well without the
computationally expensive marginalization process at decoding time.

A third consideration regarding how RNNGs, human sentence processing takes place in a left-to-
right, incremental order. While an RNNG is not a processing model (it is a grammar), the fact that it is
left-to-right opens up several possibilities for developing new sentence processing models based on an
explicit grammars.

