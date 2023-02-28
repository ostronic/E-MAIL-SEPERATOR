#: !usr/bin/python
#: Title	: EMAIL EXTRACTOR AND SEPERATOR
#: Date:	: 2022-07-2
#: Author	: "ostronics" <sosumade@gmail.com>
#: Version	: 1.0
#: Description	: Reads through a file and extracts email from it and save to another file.
#: Options	: upgradeable

import os, sys
import re
import time
from time import sleep
import threading

black="\033[1;30;20m"
red="\033[1;31;20m"
green="\033[1;32;20m"
yellow="\033[1;33;20m"
blue="\033[1;34;20m"
purple="\033[1;35;20m"
cyan="\033[1;36;20m"
white="\033[1;37;20m"
stopcolor="\033[38;2;255;255;255m"
def banner():
    logo=f"""
   
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
█████╗░░██╔████╔██║███████║██║██║░░░░░█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗
███████╗██║░╚═╝░██║██║░░██║██║███████╗███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                    +-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                        |e|-|m|a|i|l| |e|x|t|r|a|c|t|o|r|
                    +-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                    {cyan}
    """
    return logo
bdv = banner()
print(bdv)

def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


try:
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')


    os1 = []
    try:
        try:
            sam = input(f"{blue}[*] Enter file to extract data from: {green}\n\t" )
        except KeyboardInterrupt:
            print(f"{red}Keyboard Interrupt, QUITTING!!")
            quit()
        
    except:
        (f"{red}[-]   Enter a valid mail or file!!!")

    with open(sam, 'r', encoding='utf-8') as barn:
        contents = barn.read()
        
        matches = pattern.findall(contents)
        for match in matches:
            os1.append(match)
            time.sleep(2)
            clear()
    for item in os1:
        print (item)        
        with open('newmail.txt', 'w', encoding='utf-8') as f:
            f.write((item))
    
    print(f"{yellow}[-] Number of emails are:\n", len(os1))
    time.sleep(1)
        
except KeyboardInterrupt:
    print ("Keyboard Interupt, QUITTING!!!")
    quit()
