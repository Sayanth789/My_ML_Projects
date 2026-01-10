##FaceNet:A Unified Embedding for face Recognition and Clustering
###Note: I just quote the important notes from the paper for [full paper] (https://arxiv.org/pdf/1503.03832)

Despite significant recent advances in the field of face recognition,  implementing face verification
and recognition efficiently at scale presents serious challenges to current approaches. Here the authors 
present a system, called FaceNet, that directly learns a mapping from face images to a compact Euclidean space where distances
directly correspond to a measure of face similarity. Once this space has been produced, tasks such as face recogni-
tion, verification and clustering can be easily implemented using standard techniques with FaceNet embeddings as fea-
ture vectors.

Here they use  a deep convolutional network trained to directly optimize the embedding itself, rather than an in-
termediate bottleneck layer as in previous deep learning approaches. To train, they use triplets of roughly aligned matching / non-matching face patches generated using a
novel online triplet mining method. The benefit of their approach is much greater representational efficiency: they
achieved state-of-the-art face recognition performance using only 128-bytes per face.


Here they also introduce the concept of harmonic embeddings, and a harmonic triplet loss, which describe different ver-
sions of face embeddings (produced by different networks) that are compatible to each other and allow for direct comparison between each other.

**Note** here `we, us , our` sites the authors:
 Our method is based on learning a Euclidean embedding per image using a deep convolutional network. The
network is trained such that the squared L2 distances in the embedding space directly correspond to face similarity:
* Faces of the same person have small distances and faces of distinct people have large distances.

* 
