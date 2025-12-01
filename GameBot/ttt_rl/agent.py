import numpy as np
import random

class QLearningAgent:
    """
    Q-learning agent for Tic-Tac-Toe.
    Uses a Python dict as Q-table:
        Q[(state, action)] = value
    """

    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.2):
        self.alpha = alpha     # learning rate
        self.gamma = gamma     # discount factor
        self.epsilon = epsilon # exploration
        self.Q = {}            # Q-table

    def get_Q(self, state, action):
        """Return Q-value, default 0.0."""
        return self.Q.get((state, action), 0.0)

    def choose_action(self, state, available_actions):
        """ε-greedy action selection."""
        if random.random() < self.epsilon:
            return random.choice(available_actions)
        
        # greedy choice
        qs = [self.get_Q(state, a) for a in available_actions]
        max_q = max(qs)
        # pick one of the best actions randomly
        best_actions = [a for a, q in zip(available_actions, qs) if q == max_q]
        return random.choice(best_actions)

    def update(self, state, action, reward, next_state, next_actions, done):
        """Q-learning update rule."""
        old_q = self.get_Q(state, action)

        if done:
            target = reward
        else:
            max_next_q = max([self.get_Q(next_state, a) for a in next_actions], default=0)
            target = reward + self.gamma * max_next_q

        new_q = old_q + self.alpha * (target - old_q)
        self.Q[(state, action)] = new_q
