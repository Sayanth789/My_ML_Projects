from ttt_rl.TicTacToe import TicTacToeEnv
from ttt_rl.agent import QLearningAgent
import random

def train(agent, episodes=50000):
    env = TicTacToeEnv()

    for episode in range(episodes):
        state = env.reset()
        done = False

        while not done:
            # agent chooses action
            available = env.available_actions()
            action = agent.choose_action(state, available)

            # environment responds
            next_state, reward, done = env.step(action)

            if done:
                # agent won or drew
                agent.update(state, action, reward,
                             next_state, [], done=True)
                break

            # OPPONENT MOVE – random
            opponent_actions = env.available_actions()
            opponent_action = random.choice(opponent_actions)
            next_state2, reward2, done = env.step(opponent_action)

            # if opponent played and finished the game:
            if done:
                # opponent win ⇒ agent gets -1
                agent.update(state, action, -1,
                             next_state2, [], done=True)
                break

            # else continue the game
            next_available = env.available_actions()

            # agent updates
            agent.update(state, action, reward,
                         next_state2, next_available, done=False)

            state = next_state2  # move forward

        # Optionally print progress
        if episode % 5000 == 0 and episode > 0:
            print(f"Training... Episode {episode}/{episodes}")

    return agent
