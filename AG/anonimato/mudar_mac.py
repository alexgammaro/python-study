#!/usr/bin/env python

import subprocess

interface = input("Digite a interface: ")
novo_mac = input("Digite um novo MAC ADDRESS: ")

# subprocess.call(f"ifconfig {interface} down", shell=True)
# subprocess.call(f"ifconfig {interface} hw ether {novo_mac}", shell=True)
# subprocess.call(f"ifconfig {interface} up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", novo_mac])
subprocess.call(["ifconfig", interface, "up"])