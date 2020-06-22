#module for extracting data

import valid

def config(trait):
    """
    Given a trait in the config, returns the value of the trait.
    Input: trait
    Output: value
    """
    valid.config()
    with open('gsm/config.txt', 'r') as f:
        for line in f:
            split = line.split('=')
            if split[0] == trait:
                return split[1].strip()

def game_name(server_name):
    """
    Given the name of a particular server, returns the name of the game.
    Input: server_name
    Output: game_name
    """
    return "placeholder_game_name"