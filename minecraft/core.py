import os
import subprocess

from errors import LastResortError

def get(server_path):
    os.system('wget -O {0} https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar'.format(server_path + '/' + 'minecraft.jar'))
    print("Installing minecraft")
    print("By using this script, you are accepting the minecraft EULA.")
    with open ('{0}'.format(server_path + '/eula.txt'), 'w') as f:
        f.write('eula=true')


def start(server_path):
    """
    Given the server_path, will return the popen object describing the server.
    """
    p = subprocess.Popen('java -jar {}/minecraft.jar nogui'.format(server_path), stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, cwd=server_path)
    return(p)

def stop(server_path, p):
    """
    Given the server_path and the server process, will stop the server.
    """
    try:
        p.communicate(b'/stop')
    except Exception as e:
        print(e)
        raise LastResortError

def restart(server_path):
    print("Restarting")
