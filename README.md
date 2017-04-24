# GTA V Mod Menu Poisoner
Triggers False-Flag Antivirus Alerts against GTA V Mod Menus, which forces Mod Menu devs to push out new updates to prevent their cheat menus from getting auto-deleted by Antivirus Programs.

# How it works
	1. We take a harmless cheat menu file, usually a DLL injection file like dsound.dll
	2. And we inject malware code into it
	3. We then submit it to the cloud-antivirus system known as VirusTotal
	4. VirusTotal alerts to AV manufacturers that this particular filename and hash = malicious
	5. The AV manufacturers pick up the database update, and immediately kills any look-a-likes for mod menus
	6. The Mod Menu Dev gets real mad. He releases a new, slightly altered version to get around the blockage
	7. We come back, and do this shit again, and we can do this much faster and quicker than he is able to release more dickhead mod menus

Stay on the lookout on mpgh.net for any fresh mod menus to tamper with and get flagged!

# Installation Instructions (New)

1. Git Clone the repo when you open your terminal

>'git clone https://github.com/tanc7/ModMenuPoisoner'

2. Navigate to the cloned repo

>'cd ModMenuPoisoner'

3. Run the autoinstaller

>'python setup.py'

4. After a few minutes install is complete. Run Mod Menu Poisoner by opening terminal and typing:

>'ModMenuPoisoner.py'


# Basis for this tactic
http://www.reuters.com/article/us-kaspersky-rivals-idUSKCN0QJ1CR20150814
"Exclusive: Russian antivirus firm faked malware to harm rivals - Ex-employees "

Furthermore, what is described in this article WILL NOT WORK on mod menus
http://www.pcworld.com/article/2883692/virustotal-tackles-false-positive-malware-detections-plaguing-antivirus-and-software-vendors.html

Who on earth would be stupid enough to register/list their Dickhead Menu as a "trusted source"? These modders want to protect their anonymity, first and foremost.

And so... the cycle continues.

# Requirements
	1. Kali Linux https://www.kali.org/downloads/
	2. Metasploit Framework
	3. Python 2.7 (should be installed in Kali by default)
	4. A basic understanding of how to use a ordinary Linux Terminal
	5. Usage instructions for total newbies of Kali Linux will be described in the "Using Kali Linux VM" section

# Features, UI printout:

### REGULAR USAGE ###
	#0. Exit the Poisoner Program
	#1. SINGLE FILE, Poison a Mod Menu and make it look like a virus to VirusTotal
	#2. OPEN ALTERED FILE DIRECTORY, Open the directory where your altered mod menu files are located
	#3. MULTIPLE FILES, Poison Mod Menu Executables via a Wordlist full of GTA V Mod Executables


### CUSTOMIZED USAGE ###
	#4. CUSTOM PARAMETERS, Use a completely custom method of payload generation
	#5. VEIL-EVASION, Run Veil-Evasion on a executable instead (if msfvenom doesnt work)


 ### NO-ENCODER, if there are encoding errors ###
	#6. NO-ENCODER, Run msfvenom WITHOUT encoders (tends to be more successful)
	#7. NO-ENCODER (MULTIPLE), Run msfvenom on a wordlist of files


 ### YOUR FIRST TIME ###
	#SETUP. Creates the necessary directories and setup


# Installation Instructions (Old)
Installation instructions here:
> https://raw.githubusercontent.com/tanc7/ModMenuPoisoner/master/HowToInstallandUseForTotalNewbies.webm

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

# Troubleshooting

># 1. msfvenom says "an encoding exception occured"

It's hard for me to explain why it does this, but basically you need to use a DIFFERENT encoder. That is the hardest part of using msfvenom, is to figure out which encoder would not cause errors to the file. Or you can opt for NO encoding instead.

But then the altered mod won't even run in the first place because it'll hit a bad byte and crash or something. You know... if you actually wanted to "be a dick" and send a modder menu file to someone else, and wanted him or her to connect back to your listener or something.

># 2. msfvenom spits out a error like "Error: Cannot find rva! 3117297757"

You will need to use Veil-Evasion instead and select PE_Scrambler (option #20) to add that virus-like signature, here is a How-To Video: https://github.com/tanc7/ModMenuPoisoner/raw/master/WhatToDoIfMSFVenomFailsToEncode.webm

	1. Open terminal and type 'veil-evasion'
	2. Type 'use 20'
	3. Type 'set ORIGINAL_EXE executable.exe'
	4. Type 'run'
	5. Make sure to rename the file to exactly what the original file is called, you can leave out the .exe, VE automatically adds it to the end of the file
	6. Copy and paste the altered file then go submit it to VirusTotal

The file is located at
>/var/lib/veil-evasion/output/compiled/filename.exe

Where filename = whatever mod file you were messing with

>I am also aware that this is a douchy-move. Because submitting a sample, particularly a veil-evasion modified sample ruins the obfuscation process and R&D invested. However, the version of VE (Veil-Evasion 2.28) that is on your Kali Repo is actually outdated as of March 2017 and has yet to receive a update. The newest copy of Veil-Evasion has to be manually installed.
>Furthermore, there is always that one asshole that ruined Veil no matter how many times the devs have tried to plead with the user to NOT submit a sample altered by veil to VirusTotal. Veil 2.0 was already ruined.
>If you really wanted a undetectable payload, you should consider using NON-METASPLOIT payloads. Just because a payload has been generated in Metasploit makes it easily detectable due to its popularity. Consider using Pupy Python RAT or Powershell Empire or something.

>From https://null-byte.wonderhowto.com/news/antivirus-bypass-friendly-reminder-never-upload-your-samples-virustotal-0163390/
			>"Respect the Developers Who Shared Their Code with You"

			>Veil-Evasion was released in 2013. Chris Truncer, one of its creators, announced its release on his personal blog. At the very top, he posted this plea:

			>Aaaannnndddd a few days later someone posted this comment:

			>Thanks, alex!!.

			>And even now it's not hard to find numerous Veil tutorials that end with the demonstrator uploading their payload to VirusTotal:"

># 3. It shows a error 'Error: Couldn't find DOS e_magic'

Yeah this too. The executable format targeted is NOT supported by msfvenom. You will need to go back to #2 in this troubleshooting menu and go run Veil-Evasion.

># 4. How do I know it worked?

Observe this photo: https://raw.githubusercontent.com/tanc7/ModMenuPoisoner/master/Screenshot%20from%202017-04-23%2006-40-35.png

You see how it says:
Microsoft 	Trojan:Win32/Swrort.A 	20170423

That means it has been added to the Microsoft Antivirus Database. The next time Windows 10 gets pushed a "forced-update" from Microsoft, then Windows Defender will immediately run a passive scan and detect/quarantine/kill the "virus app". The mod menu of course!

># 5. What if it is labeled as a virus but not by Microsoft?

Word will travel, and eventually it will make it to Microsoft's databases. Remember, this program actually injects a malware executable with connect-back (reverse-shell) capabilities, however, I coded it to make it "inert". Unless you modify the LHOST parameter in the main file, it cannot harm anyone. All I did was set LHOST=8.8.8.8 (Google DNS LOL).

I should consider changing that Listener HOST IP to Rockstar, so they will eventually figure out that I am helping them by poisoning Mod Menus, and also, they would be able to get the IP of the person that downloaded it and have them banned.

># 6. Why would I need a encoder in the first place?

It's a common misconception that a msfvenom encoder would "make your virus invisible." That is a job for Veil-Evasion, not msfvenom. Veil-Evasion changes the signature of the payload to make it harder to detect from Antivirus. However, a msfvenom Meterpreter shell barely touches the disk (in memory) until you tell it to (persistence exploits).

Msfvenom encodes the traffic between you and your victim (if you were to use this to load targeted malware with reverse shells and listeners), and allows it to bypass a IDS (Intrusion Detection Systems).

Furthermore you would also need to enable StageEncoding in your Metasploit listener to reap the full benefits. Otherwise a section of the traffic will still be in cleartext and therefore, detectable.

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
