import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from ttt_rl import QLearningAgent 
from ttt_rl.trainer import train

agent = QLearningAgent(alpha=0.5, gamma=0.9, epsilon=0.2)
trained = train(agent, episodes=50000)

import pickle
with open("trained_agent.pyl", "wb") as f:
    pickle.dump(trained.Q, f)

print("Training Complete..!")    
