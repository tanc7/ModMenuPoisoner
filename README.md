# ModMenuPoisoner
Triggers False-Flag Antivirus Alerts against GTA V Mod Menus

# Installation Instructions
git clone this repo on your terminal
>cd /root
>git clone https://github.com/tanc7/ModMenuPoisoner

# How to Start Using It
Type the following command:
>python /root/ModMenuPoisoner/ModMenuPoisoner.py

Make sure you run the SETUP utility, which only takes up a split second of your time. From the main menu type:
>SETUP

Then from the Main Menu you have the following options:

	#0. Exit the Poisoner Program
	#1. Poison a Mod Menu and make it look like a virus to VirusTotal
	#2. Open the directory where your altered mod menu files are located
	#3. Poison Mod Menu Executables via a Wordlist full of GTA V Mod Executables
	#SETUP. Creates the necessary directories and setup

Number 1 is really simple, it poisons one file, runs msfvenom encoders through it, and adds "virus-like" characteristics
Number 2 just opens a GUI window for the poisoned files
Number 3 Means you need to supply a wordlist, just a text file, with the location of one mod file per line
