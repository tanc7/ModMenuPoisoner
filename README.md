# ModMenuPoisoner
Triggers False-Flag Antivirus Alerts against GTA V Mod Menus, which forces Mod Menu devs to push out new updates to prevent their cheat menus from getting auto-deleted by Antivirus Programs.

# Basis for this tactic
http://www.reuters.com/article/us-kaspersky-rivals-idUSKCN0QJ1CR20150814
"Exclusive: Russian antivirus firm faked malware to harm rivals - Ex-employees "

# Requirements
	1. Kali Linux https://www.kali.org/downloads/
	2. Metasploit Framework
	3. Python 2.7 (should be installed in Kali by default)
	4. A basic understanding of how to use a ordinary Linux Terminal
	5. Usage instructions for total newbies of Kali Linux will be described in the "Using Kali Linux VM" section

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

# Using Kali Linux VM

If you are new to Kali Linux, please just use the VM. There really isn't a good reason for a Hard Disk Install unless you want to use the full hardware capabilities of your machine. And then you got bs like SecureBoot to disable. I have a full HDD install, because I needed full hardware support for Wi-Fi Hacking and to be able to crack passwords at 4.5 kilohashes a second (4,500 passwords a second).

A regular VM image of Kali Linux is perfect fine for this application.

Remember, by default the password for the user is:

	USERNAME: root
	PASSWORD: toor

Which is root spelled backwards

Press your Windows key, and then type "terminal" in the search box and press [ENTER]. That will open a terminal to allow you to run commands. 

To copy and paste in terminal, you must use [CTRL][SHIFT][C] or [V] instead of the usual Windows copy/paste command. This only applies to terminal. Everything else in Kali Linux, like word processors have ordinary copy/paste shortcuts. 
