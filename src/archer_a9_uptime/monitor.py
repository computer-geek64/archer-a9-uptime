#!/usr/local/bin/python -B
# monitor.py

from datetime import datetime
from archer_a9_uptime.reboot import reboot
from subprocess import Popen, PIPE, DEVNULL


def ping(ip: str, count: int = 1, timeout: int = 3) -> bool:
    return Popen(['ping', '-c', str(count), '-w', str(timeout), ip], stdout=DEVNULL, stderr=DEVNULL).wait() == 0


def get_gateway() -> str:
    return Popen('ip route | grep "^default" | cut -d " " -f 3', stdout=PIPE, stderr=DEVNULL, shell=True).communicate()[0].decode().strip()


def is_network() -> bool:
    return ping(get_gateway())


def is_internet() -> bool:
    return ping('8.8.8.8')


if __name__ == '__main__':
    if not is_network():
        with open('/data/connectivity.log', 'a') as log:
            log.write(f'{datetime.now()} - NETWORK OFFLINE\n')
    elif not is_internet():
        with open('/data/connectivity.log', 'a') as log:
            log.write(f'{datetime.now()} - NO INTERNET ACCESS\n')
            
        reboot()
