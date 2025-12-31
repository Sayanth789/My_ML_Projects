## Boosting 
Boosting refers to a family of algorithms that are able to convert weak learners to strong learners. The main principle of boosting is to fit a sequence of weak learners− models that are only slightly better than random guessing,
such as small decision trees to weighted versions of the data. More
weight is given to examples that were misclassified by earlier rounds.

The predictions are then combined through a weighted majority vote (classification) or a weighted sum (regression) to produce the final prediction.

Boosting technique cannot be parallelized (or only partially) because each predictor can only be trained after the previous predictor has been trained and evaluated.
As a result, it does not scale as well as bagging / pasting.

## AdaBoost
The predictors(classifier/ regressor) fit the training set in sequence. The next predictor corrects its predecessor by paying more attention to the training instances that the predecessor underfitted. This results in new predictors focusing more and more on the hard cases.
To build an AdaBoost classifier, each instance's weight is set to an initial value. A base classifier (eg. Decision Tree) is trained and makes predictions on the training set. The relative weight of misclassified training instances is then increased. The second classifier is trained on the training
set using the updated weights and again it makes predictions on the training set and update the weights. The algorithm stops when the desired number of predictors is reached, or when a perfect predictor is found.


This sequential learning technique is similar to Gradient Descent, except that instead of tweaking a single predictor’s parameters to minimize a cost function, AdaBoost adds more predictors to the ensemble, gradually making it better.
Scikit-Learn uses a multiclass version of AdaBoost - SAMME. When there are just two classes, SAMME is equivalent to AdaBoost. If the predictors can estimate class probabilities (if they have a predict_proba() method), Scikit-Learn can use a variant of SAMME called SAMME.R, which
relies on class probabilities rather than predictions and generally performs better.

* If AdaBoost ensemble underfits the training data, you can try increasing the number of estimators or reducing the regularization hyperparameters of the base estimator. You may also try slightly increasing the learning rate.
lgorithm :
Each instance weight $$ w^{i} $$ is initialy set to 1/m (m = # of instances) . The first predictor is trained and its weighted error is rate $$ r_{1} $$ is calculated on the training set:
**Weighted error rate for the \(j\)-th predictor:**

$$
r_j = \sum_{i=1}^{m} w_i \, \mathbf{1}\bigl(y_j^{(i)} \neq y_i\bigr)
$$

where \(y_j^{(i)}\) is the \(j\)-th predictor’s prediction for the \(i\)-th instance.

* The predictor’s weight αj is then computed using its weighted error rate , where η is the learning rate hyperparameter (defaults to 1).
* Predictor guessing accurately - Higher weight
* Predictor gueesing mostly wrong = Negative weights
  **Predictor weigts**
  $$ \alpha-j = \eta \, \log \frac{1 - r_j}{r_j} $$

The instance weights are updated using above equation and the misclassified instance' weights are boosted.
**Weight update rule:**

$$
w_i \leftarrow
\begin{cases}
w_i \, e^{-\alpha_j}, & \text{if } y_j^{(i)} = y_i \\[6pt]
w_i \, e^{\alpha_j}, & \text{if } y_j^{(i)} \neq y_i
\end{cases}
$$
All the instance weights are normalized (divided by $$ \sum_{i=1}^{m} w_i $$


* A new predictor is trained using the updated weights, and the whole process is repeated (the new predictor’s weight is computed, the instance weights are updated, then another predictor is trained.
* To make predictions, AdaBoost simply computes the predictions of all the predictors and weighs them using their predictor weights αj. The predicted class is the one that receives the majority of weighted votes.
* Scikit-Learn uses a multiclass version of AdaBoost - SAMME. When there are just two classes, SAMME is equivalent to AdaBoost. If the predictors can estimate class probabilities (if they have a predict_proba() method), Scikit-Learn can use a variant of SAMME called SAMME.R, which relies on class probabilities rather than predictions and generally performs better.

* If AdaBoost ensemble underfits the training data, you can try increasing the number of estimators or reducing the regularization hyperparameters of the base estimator. You may also try slightly increasing the learning rate.

## Gradient Boosting 
* Gradient Boosting works by sequentially adding predictors to an ensemble, each one correcting its predecessor. However, instead of tweaking the instance weights at every iteration like AdaBoost, Gradient Boosting tries to fit the new predictor to the residual errors made by the previous predictor.

  ## Stacking
  Stacking is an ensemble learning technique that uses predictions from multiple models (for example decision tree, knn or svm) to build a new model. This model is used for making predictions on the test set.

Stacking is an ensemble learning technique that uses predictions from multiple models (for example decision tree, knn or svm) to build a new model. This model is used for making predictions on the test set.

![Stacking](Images/stacking.png)

  First, the training set is split in two subsets. The first subset is used to train the predictors in the first layer. Next, the predictors in the first layer are used to make predictions on the second(hold-out) set. Now (in example above) for each instance in the hold-out set there are four predicted values. A new training set is created using these predicted values as input features and keeping the target values. The blender is trained on this new training set, it learns to predict the target value where inputs are the the first layer’s predictions.

It is possible to train several different blenders on the top of one another (e.g., one using Linear Regression, another using Random Forest Regression etc). The training set should be divided equal to the number of layers


  

