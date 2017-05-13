#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
import StringIO
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

mod_file_format_list = [
    '*.exe',
    '*.dll',
    '*.asi',
    '*.log',
    '*.ev1',
    '*.nig',
    '*.xml'
]

mod_file_name_list = [
    '*nigger*',
    '*dsound*',
    '*menu*',
    '*xenos*',
    '*obama*',
    '*inject*',
    '*subversion*',
    '*ped*'
]
def search_mods():
    search_dir = str(raw_input("Enter the directory of your GTA Installation: "))
    for formats in mod_file_format_list:
        cmd_String = 'find %s -iname %s' % (search_dir, formats)
        print colored('Searching for %s type files','red','on_white') % formats
        os.system(cmd_String)

    for names in mod_file_name_list:
        cmd_String = 'find %s -iname %s' % (search_dir, names)
        print colored('Searching for files containing the word %s', 'blue','on_white') % names
        os.system(cmd_String)

    print colored('Search complete, check the results and add them to a wordlist so you can cleanly delete them','red','on_white')
    main()
    return

def delete_mods():
    
    return

def main():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Search for mod files so you can make a wordlist of what to delete',
        '#2. Delete all mod files by a custom wordlist (PERMANENT)'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        os.system('python /root/ModMenuPoisoner/ModMenuPoisoner.py')
    elif opt_Choice == "1":
        os.system('clear')
        search_mods()
    elif opt_Choice == "2":
        os.system('clear')
        delete_mods()

    return

# loops back to main menu
main()
