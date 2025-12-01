TWo methhods used for **Hyperparameter tuning** are `GridSearch` and `Randomized Search`. Both test different 
combination of a model's settings to find the best performance. Grid seeach exhaustively checks every combination 
of in a predefined grid of values, while random search randomly samples a sepcified number of combinations from a 
given distribution or set of values. Random search is generally more efficient for large search spaces, while grid serch 
can be better for  smaller spaces where all combinations are managable.

## Grid Search 🕵️ 
Creates a "grid" of all possible hyperparameter combianations from a manually specified set of values and evaluates
the model for each one.

**Use case**: Best for when you have a small number of hyperparameters and a finite , fixed number of values to check.

* It gurantees finding the best combination within the defined grid, but may miss the global optimum if the grid's
* step size is not small enough.

* However , It can be expensive and slow, especially as the number of hyperparameter grows, because the number
* of comibnations increases exponentially.

## **Random Search**🕵️
* Randomly smaples combiantions feom a specified distribution or set of values for a fixed number of iterations.

* **Use case** More efficient for large, high-dimnesional  seacrh spaces.

* It finds good combinations much faster that grid search and is less sensitive to the number of parameters. Allows for extending
* the search space without a proportional increase in computational time.

* However : It does not gurantees finding the absolutte best combination , as its sucess depends of the number of radnom
* samples and luck. It can be less efficient that grid searach for very small search spaces.
