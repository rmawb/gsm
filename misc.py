#miscellaneous functions used throughout

import os

def hard_kill(processes):
    """
    Kills a given popen process or list of popen processes.
    """
    if processes is list:
        for p in processes:
            ID = p.pid
            os.system('kill -9 {}'.format(ID))
    else:
        ID = processes.pid
        print(ID)
        os.system('kill -9 {}'.format(ID))