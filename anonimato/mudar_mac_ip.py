#!/usr/bin/env python

import subprocess

def mudar_mac():
    print("[+] Mudando o MAC Address.....")
    interface = input("Digite a interface: ")
    novo_mac = input("Digite um novo MAC ADDRESS: ")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", novo_mac])
    subprocess.call(["ifconfig", interface, "up"])

mudar_mac()

def mudar_ip():
    print("[+] Mudando o Endereço IP.....")
    interface = input("Digite a interface: ")
    novo_ip = input("Digite um novo IP: ")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, novo_ip, "netmask", "255.255.255.0"])
    subprocess.call(["ifconfig", interface, "up"])

mudar_ip()