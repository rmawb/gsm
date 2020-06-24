#main commands for managing game servers

import subprocess
import os
import sys

import valid
import extract
import global_var
import misc
from errors import LastResortError

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
    path_for_servers = extract.trait('path_for_servers', '/home/robert/gsm/config.txt')
    server_path = os.path.join(path_for_servers, server_name)
    try:
        os.mkdir(server_path)
    except FileExistsError:
        print("Server already exists!")
        print("Check", path_for_servers, "for directory called:", server_name)
        sys.exit()
    except FileNotFoundError:
        print("Path invalid. Check config file for 'path_for_servers'")
        sys.exit()
    except Exception as e:
        print("Unexpected Error:")
        print(e)
        sys.exit()

    #Checks module for that game and creates server
    game_module = valid.game(game_name)
    game_module.core.get(server_path)
    print("Making server:", server_name)

    #Creates gsm data for later use
    with open ('{}'.format(server_path + '/.gsm_info.txt'), 'w') as f:
        f.write('game={}'.format(game_name))

def start_server(server_name):
    """
    Starts a server with the given server_name
    Input: server_name
    """
    #gets info on what game the server is
    path_for_servers = extract.trait('path_for_servers', 'gsm/config.txt')
    server_path = os.path.join(path_for_servers, server_name)
    game_name = extract.trait('game', server_path + '/.gsm_info.txt')
    game_module = valid.game(game_name)

    #gets processes related to game and stores them
    processes = game_module.core.start(server_path)
    global_var.running_servers[server_name] = processes
    

def stop_server(server_name):
    """
    Stops a server with the given server_name
    Input: server_name
    """
    if server_name in global_var.running_servers:
        process = global_var.running_servers[server_name]
    else:
        print("There is no server with the name", server_name, "currently running!")
        return
    path_for_servers = extract.trait('path_for_servers', 'gsm/config.txt')
    server_path = os.path.join(path_for_servers, server_name)
    game_name = extract.trait('game', server_path + '/.gsm_info.txt')
    game_module = valid.game(game_name)
    try:
        game_module.core.stop(server_path, process)
        global_var.running_servers.pop(server_name)
    except LastResortError:
        print("Server is not shutting down properly, killing the process.")
        misc.hard_kill(process)
        global_var.running_servers.pop(server_name)
    except Exception as e:
        print("Unexpected Error:")
        print(e)

def restart_server(server_name):
    """
    Restarts a server with the given server_name
    Input: server_name
    """
    stop_server(server_name)
    start_server(server_name)