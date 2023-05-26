#!/usr/bin/python3
from colorama import Fore
import os

orange = '\033[0;33m'
purple = '\033[0;35m'
pink = '\033[0;95m'

def do(action):
    if action == "":
        return None 
    else:
        return eval(action)

print("Welcome to " + Fore.RED + "P" + orange + "y" + Fore.YELLOW + "R" + Fore.GREEN + "e" + Fore.BLUE + "p" + purple + "l" + pink + "!" + Fore.RESET)
print("Press ^C any time to exit")

try:
    while True:
        action = input("> ")
        try:
            result = do(action)

            if result is not None:
                print(result)
        except Exception as e:
            print("An " + Fore.RED + "error " + Fore.RESET + "occurred!")
            print(e)
except KeyboardInterrupt:
    print(Fore.RED + "\nB" + orange + "y" + Fore.YELLOW + "e" + Fore.GREEN + "!" + Fore.RESET)
    pass
