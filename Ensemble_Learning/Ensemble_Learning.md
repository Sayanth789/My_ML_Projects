## Ensemble Learning
If we aggregate the predictions of a group of predictors (classifiers/regressors) 
we will often get better predictions that with the best individual predictor. A group of
predictor is called an ensemble, the technique of aggregation is called the Ensemble Learning.
And an Ensemble Learning algorithm is called Ensemble method.

Ensemble method work best when predictors are as independent from one another as possible.
Training the dataset using very different classifiers increases the chance of them making a very different 
types of erros, improving the ensemble's accuracy.
 **Ensemble methods can be divided into 2 groups**
 * Sequential methods; where the base learners are generated sequentially (eg: AdaBoost)

> The basic motivation of sequential methods is to exploit the dependence between the base learners.
 The overall performance can be boosted by weightining the previosuly mislabeled examples  with higher weight.
* Parallel ensemble methods : Where the base learnerrs are generated in parallel (eg: Random Forest)

  > The basic motivation of paraller methods is to exploit the indepdendeces between the base learners since the error
    can be reduced dramtically by averaging.
## Voting Classifiers 
* Train a few classifiers (Logistic regression classifier, SVM, Random Forest, K-Nearest neighbors etc.) on the training set.
![Alt text](Ensemble-Learning/Images/Voting_classifiers.png)

* 

    
 
