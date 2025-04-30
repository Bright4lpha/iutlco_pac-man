import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.game import Game   
if __name__=="__main__":
    pacman = Game()
    pacman.run()