## Random Forests

Random forest is an ensemble of Decision Trees 
Instead of building a BagginClassifier and pasting it a DecisionTreeClassifier 
, we can insted use the RandomForestClassifer class, which is more conviniect and optimized for 
Decision Tress.

RandomForestClaffier has all the hyperparameters of a DecisionTrresClassifier(to controll how trees are grown), plus all 
the hyperparameters of a BagginClassifier to control the ensemble itself.

In an extremely randomized trees algorithm randomness goes one step further, the splitting threshold are randomized.
Instead of looking for the most discriminative threshold , thresholds are drwan at random for each candidate feature and best of these randomly generated thresholds is 
picked as the splittng rule. This usually allows reduction of the variance of the model a bit more, at the expense of slightly greater increse in the bias.


**Feature Importance** 
 If we look at a single Decision Tree, important features are likely to appear closer to the root of the tree, while unimportant features will often appear closer to the leaves (or not at all). It is possible to get an 
 estimate of a feature’s importance by computing the average depth at which it appears across all trees in the forest.
 
 
