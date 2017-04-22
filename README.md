# ModMenuPoisoner
Triggers False-Flag Antivirus Alerts against GTA V Mod Menus

# Requirements
	1. Kali Linux https://www.kali.org/downloads/
	2. Metasploit Framework
	3. Python 2.7 (should be installed in Kali by default)
	4. A basic understanding of how to use a ordinary Linux Terminal

# Installation Instructions
git clone this repo on your terminal
>cd /root

>git clone https://github.com/tanc7/ModMenuPoisoner

# How to Start Using It
Type the following command:
>python /root/ModMenuPoisoner/ModMenuPoisoner.py

Make sure you run the SETUP utility, which only takes up a split second of your time. From the main menu type:
>SETUP

This also adds ModMenuPoisoner to the command line.

Then from the Main Menu you have the following options:

	#0. Exit the Poisoner Program
	#1. Poison a Mod Menu and make it look like a virus to VirusTotal
	#2. Open the directory where your altered mod menu files are located
	#3. Poison Mod Menu Executables via a Wordlist full of GTA V Mod Executables
	#SETUP. Creates the necessary directories and setup

	Number 1 is really simple, it poisons one file, runs msfvenom encoders through it, and adds "virus-like" characteristics
	Number 2 just opens a GUI window for the poisoned files
	Number 3 Means you need to supply a wordlist, just a text file, with the location of one mod file per line

# How to Submit the Poisoned Executables to get them flagged

Go to VirusTotal
>www.virustotal.com

Submit the files in your directory to virus scans one at a time (unfortunately multi-scans are not available)
>/root/Documents/ModMenusReencoded

# DISCLAIMER, Keep your Windows Partition CLEAN

Please try to avoid leaving remnants of mod menus in a Windows Hard Drive. Rockstar Anti-Cheat is known to scan your directories, and even if you don't cheat, you could still get banned for it
