#!/usr/bin/env python
# coding: utf-8

# # Agent Sudo
# 
# This is an "Easy" level room that comes with a bit of everything. Scanning, Hashing, brute force and steganography. I havent seen a lot here that actually covers steganography so it was a bit of googling for me.
# 
# <hr>

# ## First Steps
# 
# As normal, we can start with a scan. Nmap for the standard ports is a good start<br>
# ![AgentSudo_NmapScan.png](../images/PracticeRooms/AgentSudo_NmapScan.png) <br>
# 
# So, we have 3 open ports
# - FTP
# - SSH
# - HTTP
# 
# FTP we can look at later, lets start with the website.
# 
# <hr>
# 

# ## Website Access
# 
# So we bring up the website, and are greeted with: <br>
# ![AgentSudo_WelcomePage.png](../images/PracticeRooms/AgentSudo_WelcomePage.png)<br>
# 
# What does it mean though? After a bit of googling, the 'user-agent' is just a header that is passed to the site. We can see this by capturing the request in BurpSuite.<br>
# ![AgentSudo_BurpProxy.png](../images/PracticeRooms/AgentSudo_BurpProxy.png)<br>
# 
# > Now, as an aside here, I actually had trouble with this next part. It asks to provide a codename to the site, but I couldnt see any example code names. So my thought was to just brute force it. The problem with this however is that Burp is SLOW and I didnt have another tool that could pass header values to a site. In the end I just made my own program to brute force it, [WebBruteForce v1.0](../Tools/Programs/WebBruteForce.ipynb). I set it up and ran it, but it didnt give me a valid name... I thought about it over the next day and had a bit of a D'oh! moment. The result is the steps below.
# 
# Now that we know where to replace (user-agent), we need to generate a list of guesses. We can see that "Agent C" signed off the welcome message, so lets start with that. Send it to repeater and we'll see what we get. <br>
# <br>
# 
# Doesnt look good... how about just "C"<br>
# ![AgentSudo_BurpRepeater.png](../images/PracticeRooms/AgentSudo_BurpRepeater.png)<br>
# 
# Still looks similar, but we can see we got back a redirect. Clicking the "Follow Redirection" tab gives us a new page. Yay.<br>
# ![AgentSudo_BurpRendered.png](../images/PracticeRooms/AgentSudo_BurpRendered.png) <br>
# 
# <hr>
# 

# ## FTP access
# 
# So, remember how I said we'll look at FTP later, well here we are. We have a username now (chris), and a note saying the password is weak. Thats nice of them. Time to spin up hydra me thinks. <br>
# ![AgentSudo_HydraFTP.png](../images/PracticeRooms/AgentSudo_HydraFTP.png) <br>
# 
# Nice, now we can log in. Listing our directory gives 3 files. Lets grab all 3. <br>
# ![AgentSudo_FTPFiles.png](../images/PracticeRooms/AgentSudo_FTPFiles.png) <br>
# 
# <hr>
# 

# ## Steganography
# 
# Jumping the gun a bit here, but it's where we are heading. Take a look at the txt file we just grabbed. Agent C is implying that Agent J's password is stored in the pictures. If we look at the pictures they seem normal though. Spoiler alert: they arent.
# 
# ### Exiftool
# Running Exiftool on the files gives us our first clue. The JPG file "looks" pretty normal, but the PNG has a warning about data after the end of the PNG file.<br>
# ![AgentSudo_ExifPNG.png](../images/PracticeRooms/AgentSudo_ExifPNG.png)<br>
# 
# ### Binwalk
# This will give us an idea what the extra data might be (and allow us to extract it)<br>
# ![AgentSudo_Binwalk.png](../images/PracticeRooms/AgentSudo_Binwalk.png)<br>
# 
# Ding ding ding! Extract out the files with -e. The will be put in a folder named "_\<originalFileName>"
# 
# ### Cracking the Zip
# John does this in his sleep. I've already done it so the password doesnt show, "alien"<br>
# ![AgentSudo_ZipCracking.png](../images/PracticeRooms/AgentSudo_ZipCracking.png)<br>
# 
# We can now extract the zip and take a look
# 
# > 7z e 8702.zip
# 
# We now have a populated "to_agentR.txt"<br>
# ![AgentSudo_ToR.png](../images/PracticeRooms/AgentSudo_ToR.png)<br>
# 
# 
# ### Decode the Data
# So, we have a string, 'QXJlYTUx', thats got to be an encoding of some sort, time for cyberchef. Its all characters so my guess would be base64 encoded.<br>
# 
# ![AgentSudo_CyberChef.png](../images/PracticeRooms/AgentSudo_CyberChef.png)<br>
# 
# ### Steghide
# Hmm, another password. We still dont have anything fun from that JPG, but we have a password now. Does it work with Steghide?
# ![AgentSudo_Steghide.png](../images/PracticeRooms/AgentSudo_Steghide.png)<br>
# 
# Thats a yes :-)
# 
# <hr>

# ## Connect and Escalate
# 
# So, from the above we now have a user and password. Can SSH to the machine now.
# > ssh james@10.10.217.248
# 
# What can we run as root?<br>
# ![AgentSudo_SudoList.png](../images/PracticeRooms/AgentSudo_SudoList.png)<br>
# 
# Interesting, can run sudo, but not(!) as root. We can check the version of sudo though:
# 
# > sudo -V
# 
# This gives us version 1.8.21p2. Exploit DB gives us an exploit that looks about right.<br>
# ![AgentSudo_ExploitDB.png](../images/PracticeRooms/AgentSudo_ExploitDB.png)
# 
# The code is nice an easy too.<br>
# ![AgentSudo_Escalate.png](../images/PracticeRooms/AgentSudo_Escalate.png)<br>
# 
# The flag can be found in /root/root.txt, which includes the answers for the remaining questions.
# 
# <hr>

# In[ ]:




