#!/usr/bin/env python
# coding: utf-8

# # Terminator
# 
# Gobuster after, to get where its used (squirrelmail)

# This is a Terminator themed room, at the "easy" level
# 
# ## First steps
# 
# As normal, lets start with an Nmap scan of the server<br>
# ![Terminator_Nmap.png](../images/PracticeRooms/Terminator_Nmap.png)<br>
# 
# Ok, a few things to look at today
# 
# - 22 FTP
# - 80 Web Server
# - 110 POP3
# - 139 NetBios (Samba)
# - 143 IMAP
# - 445 NetBios (samba)
# 
# ### IMAP / POP3
# I've never played with these before so I started here. IMAP didnt allow authentication over unsecure (requires SSL/TLS), a non starter for me atm. POP3 couldnt really get me anywhere. Skipping past these for now
# 
# <hr>
# 

# ## SMB
# Ok, SMB tends to give away a bit, so lets go there next. Nmap has a built in enum script for this:<br>
# ![Terminator_NmapEnumShares.png](../images/PracticeRooms/Terminator_NmapEnumShares.png) <br>
# 
# Now we're getting somewhere. Both the anonymous and IPC directorys have anonymous access, im going to start with the anonymous one.<br>
# ![Terminator_SMBaccess.png](../images/PracticeRooms/Terminator_SMBaccess.png)<br>
# Which was indeed very interesting. I've grabbed the txt files in the initial directory and the log1 file from the logs directory. These look a lot like passwords, which the attention.txt file supports:<br>
# ![Terminator_SMBfiles.png](../images/PracticeRooms/Terminator_SMBfiles.png)
# 
# ### Using the Found Passwords
# Now that we have a list of passwords, lets try use these against the share we dont have a login for:<br>
# Aaaand, I got nothing using the username
# - MilesDyson
# - Miles
# 
# What else have we got?
# 
# <hr>
# 

# ## Website Enumeration
# So we have a user and password, but nowhere to put it.... thats annoying... Lets move on to the website enumeration. I'm a fan of gobuster so I'll start there<br>
# ![Terminator_GoBusterScan.png](../images/PracticeRooms/Terminator_GoBusterScan.png)<br>
# 
# - No luck in the /Admin or /ai pages
# 
# SquirrelMail is an interesting one though, its asks for a username and password. Burp makes short work of that...<br>
# ![Terminator_BurpSquirrelMail.png](../images/PracticeRooms/Terminator_BurpSquirrelMail.png)<br>
# "cyborg007haloterminator"... nice....
# 
# ### Exploring
# So, we have a webmail box...<br>
# ![Terminator_Inbox.png](../images/PracticeRooms/Terminator_Inbox.png)<br>
# 
# - Nothing in the Drafts, sent or Trash
# - 2 emails look a bit noisy... cyberchef gives one back as a string from the other, might be something for later
# - The other one is a password reset for SMB... well thats helpful: 
# )s{A&2Z=F^n_E.B`
# 
# <hr>
# 

# ## Back to SMB
# Lets try this back in Miles SMB share:<br>
# ![Terminator_MilesDirectory.png](../images/PracticeRooms/Terminator_MilesDirectory.png)<br>
# 
# Ok, wasnt expecting that... Lets see what's in "notes"<br>
# ![Terminator_Notes.png](../images/PracticeRooms/Terminator_Notes.png)<br>
# 
# Well that looks Important. "Get" it then take a look<br>
# ![Terminator_Important.png](../images/PracticeRooms/Terminator_Important.png) <br>
# Nice /45kra24zxs28v3yd
# 
# <hr>
# 

# ## Now What?
# 
# Ok, we've sorta hit a dead end now. That page wasnt very fun. That being said, it was mentioned that this directory is a beta version. Maybe there is more in this subdirectory?<br>
# ![Terminator_GobusterAgain.png](../images/PracticeRooms/Terminator_GobusterAgain.png)<br>
# 
# Hey, look at that, theres a new admin page. Cuppa CMS<br>
# ![Terminator_Cuppa.png](../images/PracticeRooms/Terminator_Cuppa.png)<br>
# 
# None of our logins work here either. Any known exploits with it?<br>
# ![Terminator_ExploitDB.png](../images/PracticeRooms/Terminator_ExploitDB.png)<br>
# 
# Thats a yes, looks like a Local File Inclusion exploit which includes an example for the etc/passwd file, so lets grab that
# > http://10.10.252.2/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd
# 
# We cant get the shadow file though, so what else can we do? How about a Remote File inclusion? Grab a PHP reverse shell file and host a HTTP server<br>
# 
# ![Terminator_ReverseFileHosted.png](../images/PracticeRooms/Terminator_ReverseFileHosted.png)<br>
# 
# Host a reverse shell listener based on your config<br>
# ![Terminator_Listening.png](../images/PracticeRooms/Terminator_Listening.png)<br>
# 
# And use the exploit to pull your reverse shell file<br>
# ![Terminator_ExploitLink.png](../images/PracticeRooms/Terminator_ExploitLink.png)<br>
# 
# If we've done it all correct, we should now get a reverse shell<br>
# ![Terminator_ReverseShell.png](../images/PracticeRooms/Terminator_ReverseShell.png)<br>
# 
# All the Woot :-)<br>
# The user flag is in /home/milesdyson/user.txt<br>
# 
# <hr>
# 

# ## PrivEsc
# 
# Time for some Privelige Escalation :-)
# 
# - Sudo -l : Nope
# - SUID/GUID : Nope
# - passwd/shadow files : Nope (only passwd)
# - LinPeas : Nope, includes a 95% exploit but couldnt find much on this
# - LinEnum : Victory
# 
# LinEnum has given us a PrivEsc point, there is a job that runs every minute in a directory that we can access<br>
# ![Terminator_Crontab.png](../images/PracticeRooms/Terminator_Crontab.png)<br>
# 
# 
It runs TAR on all files in the directory
create a .sh that will run what we want (cp /bin/bash /tmp/shell && chmod +s /tmp/shell)
create 2 files
touch /var/www/html/--checkpoint-action....
touch /var/www/html/--checkpoint=1
THE / AFTER HTML is needed

GTFOBINS image added already