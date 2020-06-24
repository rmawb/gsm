import sys
import os
import subprocess

import server_commands
import global_var

def invalid(*args, **kwargs):
    """
    Called when there is an unrecognized command
    """
    print(command, "is not a recognized command!")

def list_running_game_servers(*args, **kwargs):
    print(global_var.running_servers)

def test():
    path = os.path.join('/home/robert', 'tomato')
    os.mkdir(path)

while True:
    input_command = input()
    command, *arguments = str.split(input_command)
    cmds = {
        'exit'    : sys.exit,
        'install' : server_commands.install_server,
        'start'   : server_commands.start_server,
        'stop'    : server_commands.stop_server,
        'restart' : server_commands.restart_server,
        'list'    : list_running_game_servers,
        'test'    : test
    }
    func = cmds.get(command, invalid)
    func(*arguments)