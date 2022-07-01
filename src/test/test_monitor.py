# test_monitor.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from archer_a9_uptime import monitor


def test_ping():
    valid_ip = '8.8.8.8'
    invalid_ip = '192.0.2.1'

    assert monitor.ping(valid_ip)
    assert not monitor.ping(invalid_ip)


def test_get_gateway():
    gateway = monitor.get_gateway()

    assert gateway.count('.') == 3
    assert all(byte.isdecimal() for byte in gateway.split('.'))


def test_is_network():
    assert monitor.is_network()


def test_is_internet():
    assert monitor.is_internet()
