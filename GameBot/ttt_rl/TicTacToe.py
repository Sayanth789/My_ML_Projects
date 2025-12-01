import numpy as np 

class TicTacToeEnv:

    def __init__(self):
        # Board : 0 = empty , 1 = x, -1 = o 
        self.reset() 

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1 # x starts first 
        return self.get_state() 
    
    def get_state(self):
        return tuple(self.board.reshape(9))  # immutable for dict key 
    
    def available_actions(self):
        return [i for i in range(9) if self.board.flat[i] == 0 ]
    
    def step(self, action):
        # make the move 
        self.board.flat[action] = self.current_player 

        # check if win 
        if self.is_winner(self.current_player):
            reward = 1 
            done = True
        elif len(self.available_actions()) == 0:
            reward =  1 
            done = True 

        else: 
            reward = 0 
            done = False 

        # switch player 
        self.current_player *= -1 

        return self.get_state(), reward, done 

    def is_winner(self, player):
        b = self.board

        return (
            np.any(np.sum(b, axis=0) == player*3) or # columns 
            np.any(np.sum(b, axis=1) == player*3) or # rows
            np.trace(b) == player * 3 or 
            np.trace(np.fliplr(b)) == player*3   # anti diag
        )          