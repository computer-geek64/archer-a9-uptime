#!/usr/local/bin/python -B
# monitor.py

from reboot import reboot
from datetime import datetime
from subprocess import Popen, DEVNULL


def network():
    return Popen(['ping', '-c', '1', '-W', '3', '192.168.0.1'], stdout=DEVNULL, stderr=DEVNULL).wait() == 0


def internet():
    return Popen(['ping', '-c', '1', '-W', '10', '8.8.8.8'], stdout=DEVNULL, stderr=DEVNULL).wait() == 0


if __name__ == '__main__':
    if not network():
        with open('/data/connectivity.log', 'a') as log:
            log.write(f'{datetime.now()} - NETWORK OFFLINE\n')
    elif not internet():
        with open('/data/connectivity.log', 'a') as log:
            log.write(f'{datetime.now()} - NO INTERNET ACCESS\n')
            
        reboot()
