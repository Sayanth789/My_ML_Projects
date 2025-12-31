## Bagging And Pasting 
In Bagging/Pasting, same training algorithm is used for every predictor (classifier/Regressor), but we 
train them on differetn random subsets of the training set. When sampling is performed with replacement, the method is called bagging/boostrap aggregation.
When sampling is performed without replacement, it is called pasting.

![Bagging](Images/Bagging.png)
Once all predictors are trained, the ensemble can make a prediction for a new instance by aggregating the predictions of all predictors. The aggregation function is generally the statistical mode
(most frequent prediction) for classification, or the statistical mean for regression.

Each individual predictor has a higher bias(underfit) because only a subset of the training set 
is trained on it, aggregation reduces both bias and variance than a single predictor trainedon the original trainng set.

Bagging and Pasting scale very well on different CPU cores and servers, all predictors can be trained in parallel, predictors can also be made in parallel.

#### Out Of Bag Evaluation 
With bagging at each iteration, the reamining training instances that are not sampled are called out-of-bag (oob) instances.
These instances are not the same for all predictors. Sicne a predictor never sees the oob instances during training , it can be evaluated on these instances, without the need for a seperate validation
set or croo-validation. We can evaluate the ensemble itself by averaging the oob evaluations of each predictor.
