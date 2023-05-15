from colorama import Fore 

def do(action):
    return eval(action)

while True:
    action = input("> ")
    try:
        result = do(action)
        if result is not None:
            print(result)
    except Exception as e:
        print("An " + Fore.RED + "error " + Fore.RESET + "occurred!")
        print(e)
