#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
# from termcolor import colored
import sys
import StringIO

# Git Clone
print 'Git cloning newest copy of Poisoner, please wait'
os.chdir('/tmp')
os.system('git clone https://github.com/tanc7/ModMenuPoisoner')

# make directories
print 'Making required directories'
os.system('mkdir /root/ModMenuPoisoner')
os.system('mkdir /root/Documents/ModMenusReencoded/')
# chmod executables
os.system('chmod 777 ./*')
# copy to new install directory
os.system('cp -r ./* /root/ModMenuPoisoner')
# Copy to usr/local/bin
print 'Adding executable to /usr/local/bin'
os.system('cp -r ModMenuPoisoner.py /usr/local/bin')

output_Dir = '/root/Documents/ModMenusReencoded' # This is the directory for output msfvenom payloads
# print setup complete
print 'Setup complete'
print 'For future reference, your reencoded mod menus will be located at: ' + output_Dir
print 'You can run Mod Menu Poisoner Now on terminal by typing: ModMenuPoisoner.py'
