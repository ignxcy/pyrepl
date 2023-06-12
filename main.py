#!/usr/bin/python3
import os

red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
orange = '\033[0;33m'
blue="\033[1;34m"
purple="\033[1;35m"
cyan="\033[1;36m"
pink = '\033[0;95m'
grey="\033[0;37m"
reset="\033[m"

def do(action):
    if action == "":
        return None 
    else:
        return eval(action)

print("Welcome to " + red + "P" + orange + "y" + yellow + "R" + green + "e" + blue + "p" + purple + "l" + pink + "!" + reset)
print("Press ^C any time to exit")

try:
    while True:
        action = input("> ")
        try:
            result = do(action)

            if result is not None:
                print(result)
        except Exception as e:
            print("An " + red + "error " + reset + "occurred!")
            print(e)
except KeyboardInterrupt:
    print(red + "\nB" + orange + "y" + yellow + "e" + green + "!" + reset)
    pass
