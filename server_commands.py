#main commands for managing game servers

import valid
import extract
import os
import sys

def install_server(game_name, *args):
    """
    Installs game server by calling the core "get" function of the game.
    Input: game_name
    """
    #Checks for name and prompts if no name given
    if args:
        server_name = ' '.join(args)
    else:
        print("What would you like this server to be called?")
        server_name = input()

    #Makes directory for server
    server_path = extract.config('server_path')
    try:
        os.mkdir(server_path + "/" + server_name)
    except FileExistsError:
        print("Server already exists!")
        print("Check", server_path, "for directory called:", server_name)
        sys.exit()
    except FileNotFoundError:
        print("Server path invalid. Check config file for 'server_path'")
        sys.exit()
    except Exception as e:
        print("Unexpected Error:")
        print(e)
        sys.exit()

    #Checks module for that game and creates server
    game_module = valid.game(game_name)
    game_module.core.get(server_name, server_path)
    print("Making server:", server_name)

def get_init(server_name):
    """
    Sets values for start, stop, and restart functions.
    Input: server_name
    Output: Tuple of (game_module, server_path)
    
    server_name is the name of the particular server
    game_module is the module describing the game in general
    server_path is the path locating the game servers
    """
    game_name = extract.game_name(server_name)
    game_module = valid.game(game_name)
    server_path = extract.config('server_path')
    valid.dir()
    return game_module, server_path

def start_server(server_name):
    """
    Starts a server with the given server_name
    Input: server_name
    """
    game_module, server_path = get_init(server_name)
    game_module.core.start(server_name, server_path)

def stop_server(server_name):
    """
    Stops a server with the given server_name
    Input: server_name
    """
    game_module, server_path = get_init(server_name, server_path)

def restart_server(server_name):
    """
    Restarts a server with the given server_name
    Input: server_name
    """
    game_module, server_path = get_init(server_name, server_path)