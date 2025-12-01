import numpy as np 
from ttt_rl.TicTacToe import TicTacToeEnv
from ttt_rl.agent import QLearningAgent 

def print_board(board_tuple):
    b = np.aray(board_tuple).reshape(3, 3)
    symbols = {1:'x', -1:'o', 0:'.'}
    print("\n".join(" ".join(symbols[x] for x in row) for row in b))
    print()

def play(agent):
    env = TicTacToeEnv() 
    state = env.reset() 


    while True:
        print_board(state)

        # Human move (0)
        action = int(input("Choose your move (0-8)"))
        state, reward, done = env.step(action)
        if done:
            print_board(state)
            print("Game over ! You win...!" if reward ==1 else "Draw")
            return 
        
        # agent move (x)
        available = env.available_actions() 
        action = agent.choose_action(state, available)
        state, reward, done = env.step(action)
        if done:
            print_board(state)
            print("AGent wins .. !" if reward == 1 else "Draw")
            return 
        


