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

def config():
    """
    Checks if config file is valid.
    """
    traits = ('server_path')
    try:
        with open('gsm/config.txt', 'r') as f:
            for line in f:
                trait, value = line.split('=')
                if trait not in traits:
                    print(trait)
                    e = ExtraTraitError()
                    raise e
    except FileNotFoundError:
        print("Config file not found! Check for config.txt in gsm directory!")
        sys.exit()
    except ExtraTraitError:
        print("Unknown config option:", trait)
        print("Please check config file.")
        sys.exit()
    except Exception as e:
        print("Unexpected error:")
        print(e)
        sys.exit()

