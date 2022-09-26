#!/usr/bin/env python
# coding: utf-8

# # Armitage
# 
# ## Install
# https://tryhackme.com/room/introtoc2 Task 4
# 
# > git clone https://gitlab.com/kalilinux/packages/armitage.git && cd armitage <br>
# > bash package.sh
# 
# 
# ![Armitage_Clone.png](../images/Tools/Armitage_Clone.png)<br>
# ![Armitage_Build.png](../images/Tools/Armitage_Build.png)<br>
# 
# Files should now be in ./release/unix/<br>
# ![Armitage_Built.png](../images/Tools/Armitage_Built.png)<br>
# 
# The fun files here are:
# - TeamServer: Creates a server for the team to use. It must be passed<br>
#   - IP address<br>
#   - Shared Password<br>
# - Armitage: Used to connect to a server. It gives you a screen to log in with. THe username is a 'nickname'<br>
# 
# > this is actually in the kali repos now, can jsut install armitage<br>
# > same with teamserver
# 
# just... use the built in one... I had so many issues connecting
# 
# <hr>
# 
# ### Prepare The Environment
# 
# Since it uses metasploit, make sure its all worky<br>
# - Start the DB
#   - sudo systemctl start postgresqla
# - Clear the DB<br>
#   - sudo msfdb delete<br>
# - ReInitialise<br>
#   - sudo msfdb init<br>
# 
# 
# <hr>
# 

# ## Start & connect
# 
# Make sure youre in the right directory:<br>
# - sudo teamserver [ip] [password]<br>
#   - Open a new terminal<br>
# - armitage<br>
#   - teamserver gives the logins, use msf as your user and the above password<br>
# 
# ![Armitage_Connect.png](../images/Tools/Armitage_Connect.png)<br>
# 
# <hr>
# 

# ## Make It Do Fun Things
# 
# ### Start a Scan
# 
# ![Armitage_StartScan.png](../images/Tools/Armitage_StartScan.png)<br>
# 
# You'll get a window for a target, can do an IP or a subnet. Quick or OS detection doesnt give the -vv option though....<br>
# I did "10.10.247.213"<br>
# After a while, the scan completes and I get a new host on my display<br>
# 
# ![Armitage_NewHost.png](../images/Tools/Armitage_NewHost.png)<br>
# 
# ### Run Exploits
# 
# You can now open exploits and pick your attack. Drag drop the attack to the host and you can now set your arguments and let it run<br>
# ![Armitage_StartEternalBlue.png](../images/Tools/Armitage_StartEternalBlue.png)<br>
# 
# If it works, it gets all Thor-d<br>
# ![Armitage_exploited.png](../images/Tools/Armitage_exploited.png)<br>
# 
# ### Run POST modules
# 
# You can then right click and take control of the shell<br>
# Most of the time, you will want to excalate this to a meterpreter shell. Right click the host and select your shell, then Post. It will expand your tree to show the post modules. Under manager is the shell_to_meterpreter module. Run it and will attempt to create a second shell for meterpreter.
# ![Armitage_Meterpreter.png](../images/Tools/Armitage_Meterpreter.png)<br>
# 
# <hr>
