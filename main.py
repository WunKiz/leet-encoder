from time import sleep
import colorama

print(colorama.Fore.RED + "  _ _______________   _____ _   _  ____ ___  ____  _____ ____")
print(colorama.Fore.LIGHTRED_EX + " / |___ /___ /___  | | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \ ")
print(colorama.Fore.LIGHTRED_EX + " | | |_ \ |_ \  / /  |  _| |  \| | |  | | | | | | |  _| | |_) |")
print(colorama.Fore.LIGHTRED_EX +  " | |___) |__) |/ /   | |___| |\  | |__| |_| | |_| | |___|  _ <")
print(colorama.Fore.RED + " |_|____/____//_/    |_____|_| \_|\____\___/|____/|_____|_| \_\ ")
print(colorama.Fore.LIGHTBLACK_EX + "Loading Informations!")
sleep(2)
text = str(input("Type the text to LEET -> "))
while True:
    teste = str(input("Type the mode [1/2] (ENCODE/DECODE) -> ")).lower().strip()[0]
    if teste not in "ed21":
        print("Invalid Args")
    else:
        break


def encoder():
    localstring = text.replace("a", "4")
    localstring = localstring.replace("e", "3")
    localstring = localstring.replace("g", "6")
    localstring = localstring.replace("i", "1")
    localstring = localstring.replace("o", "0")
    localstring = localstring.replace("s", "5")
    localstring = localstring.replace("t", "7")
    return localstring


def decoder():
    localstring = text.replace("4", "a")
    localstring = localstring.replace("3", "e")
    localstring = localstring.replace("6", "g")
    localstring = localstring.replace("1", "i")
    localstring = localstring.replace("0", "o")
    localstring = localstring.replace("5", "s")
    localstring = localstring.replace("7", "t")
    return localstring


if teste == "1" or teste == "e":
    print(colorama.Fore.MAGENTA + "Encoding")
    sleep(1)
    print(colorama.Fore.LIGHTBLACK_EX + text.capitalize() + " in leet is " + encoder())
elif teste == "2" or teste == "d":
    print(colorama.Fore.YELLOW + "Decoding")
    sleep(1)
    print(colorama.Fore.LIGHTBLACK_EX + text.capitalize() + " in normal alphabet is " + decoder())


