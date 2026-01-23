from __future__ import print_function, division
from builtins import range

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

# Reproducibility
np.random.seed(2)

# Parameters
NUM_TRIALS = 2000
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]


# -----------------------------
# Bandit class
# -----------------------------
class Bandit:
    def __init__(self, p):
        self.p = p        # True win probability
        self.a = 1        # Beta prior alpha
        self.b = 1        # Beta prior beta
        self.N = 0        # Number of times selected

    def pull(self):
        """Simulate pulling the bandit arm"""
        return np.random.random() < self.p 
    
    def sample(self):
        """Draw a sample from the Beta distribution (Thompson Sampling)"""
        return np.random.beta(self.a, self.b)

    def update(self, x):
        """Update posterior based on observed reward x"""
        self.a += x
        self.b += 1 - x
        self.N += 1


# -----------------------------
# Plotting function
# -----------------------------
def plot(bandits, trial):
    x = np.linspace(0, 1, 200)
    plt.figure(figsize=(8,5))
    for b in bandits:
        y = beta.pdf(x, b.a, b.b)
        win_rate = (b.a - 1) / b.N if b.N > 0 else 0
        plt.plot(x, y, label=f"real p: {b.p:.2f}, win rate={win_rate:.2f}")
    plt.title(f"Bandit distributions after {trial} trials")
    plt.xlabel("Probability")
    plt.ylabel("Density")
    plt.legend()
    plt.show()


# -----------------------------
# Main experiment
# -----------------------------
def experiment():
    # Initialize bandits
    bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]

    sample_points = [5, 10, 20, 50, 100, 200, 500, 1000, 1500, 1999]
    rewards = np.zeros(NUM_TRIALS)

    for i in range(NUM_TRIALS):
        # Thompson sampling: choose bandit with highest sampled probability
        j = np.argmax([b.sample() for b in bandits])

        # Plot the posteriors at specific points
        if i in sample_points:
            plot(bandits, i)

        # Pull the selected bandit
        x = bandits[j].pull()

        # Update rewards and bandit posterior
        rewards[i] = x
        bandits[j].update(x)

    # Print results
    print("Total reward earned:", rewards.sum())
    print("Overall win rate:", rewards.sum() / NUM_TRIALS)
    print("Number of times each bandit was selected:", [b.N for b in bandits])


# -----------------------------
# Run experiment
# -----------------------------
if __name__ == '__main__':
    experiment()
