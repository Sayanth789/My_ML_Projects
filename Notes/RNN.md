#Recurrent Sequence to Sequecne Learning 



**Sequence to sequence** modeling has been synonymous
with recurrent neural network based encoder-decoder ar-
chitectures (Sutskever et al., 2014; Bahdanau et al., 2014).
The encoder RNN processes an input sequence x =
(x1, . . . , xm) of m elements and returns state representa-
tions z = (z1. . . . , zm). The decoder RNN takes z and
generates the output sequence y = (y1, . . . , yn) left to
right, one element at a time. To generate output yi+1, the
decoder computes a new hidden state hi+1 based on the
previous state hi, an embedding gi of the previous target
language word yi, as well as a conditional input ci derived
from the encoder output z. Based on this generic formula-
tion, various encoder-decoder architectures have been pro-
posed, which differ mainly in the conditional input and the
type of RNN.

Recurrent neural networks (RNNs) are a rich class of dynamic models that have
been used to generate sequences in domains as diverse as music, text 
and motion capture data. RNNs can be trained for sequence generation by
processing real data sequences one step at a time and predicting what comes
next. Assuming the predictions are probabilistic, novel sequences can be gener-
ated from a trained network by iteratively sampling from the network’s output
distribution, then feeding in the sample as input at the next step. In other
words by making the network treat its inventions as if they were real, much like
a person dreaming.Although the network itself is deterministic, the stochas-
ticity injected by picking samples induces a distribution over sequences. This
distribution is conditional, since the internal state of the network, and hence its
predictive distribution, depends on the previous inputs.


ong Short-term Memory (LSTM) is an RNN architecture designed to
be better at storing and accessing information than standard RNNs. LSTM has
recently given state-of-the-art results in a variety of sequence processing tasks,
including speech and handwriting recognition.

##Long Short-Term Memory

 However it  have found that the Long Short-Term Memory architecture, which uses purpose-built memory cells to store information, is better at finding and exploiting long range dependencies in the data.

 


