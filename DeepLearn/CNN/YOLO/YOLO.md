YOLO is the approach to object detection. Prior the work on object detection repurposes 
classifier to object detecction, here the authors frame the obhect detection as a regression problem to 
spatially seperated bouding boxes and associated class probabilities.
A single neural network predicts te bouding boxes and class probabilities directly from full images in one evaluation.
Since the whole detection pipeline is a single network, it can be optimized end-to-end directly on detection performance. 


Here, a single convolutioal network simultaneously predicts multiple bouding boxes and class probibilities for those boxes.
YOLO trains on full images and-directly optimizes detection performance. This unified model has several benefits over trandititonal methods of 
object detection.
............

For more see the paper at [YOLO](https://arxiv.org/pdf/1506.02640)
