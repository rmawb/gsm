import server_commands
import sys
import os

def invalid(*args, **kwargs):
    """
    Called when there is an unrecognized command
    """
    print(command, "is not a recognized command!")
    return 0

def test(compare):
    test_str = "server_path"
    trait, value = compare.split('=')
    if trait == test_str:
        print('I AM THE SAME')
    return 0

while True:
    input_command = input()
    command, *arguments = str.split(input_command)
    cmds = {
        'exit'    : sys.exit,
        'install' : server_commands.install_server,
        'start'   : server_commands.start_server,
        'stop'    : server_commands.stop_server,
        'restart' : server_commands.restart_server,
        'test'    : test
    }
    func = cmds.get(command, invalid)
    func(*arguments)