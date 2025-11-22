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
type of RNN
