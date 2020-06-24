#module to check if operation is valid

import importlib
import sys
import os
from errors import ExtraTraitError

def game(game_name):
    """
    Checks if there is a module for the game_name.
    Input: game_name
    """
    try:
        game_module = __import__(game_name)
        return game_module
    except ModuleNotFoundError:
        print("Missing", game_name, "module! Check for", game_name +".py")
        sys.exit()
    except Exception as e:
        print("Unexpected error:")
        print(e)
        sys.exit()
        

