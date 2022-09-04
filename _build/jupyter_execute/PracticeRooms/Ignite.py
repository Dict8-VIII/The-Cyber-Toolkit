#!/usr/bin/env python
# coding: utf-8

# # Ignite
# 
# We have another easy room here, apparently a startup has some problems with their servers... Lets be another problem.
# 
# ## Initial Steps
# As always, start with an N-Map Scan.<br>
# ![Ignite_Nmap.png](../Images/PracticeRooms/Ignite/Ignite_Nmap.png)<br>
# 
# Ok, port 80. Brint it up <br>
# ![Ignite_DefaultPage.png](../Images/PracticeRooms/Ignite/Ignite_DefaultPage.png) <br>
# 
# FUELCMS, We've run into this before actually. We've got a few options from here<br>
# 1. Run GoBuster
# 2. Check ExploitDB (we have a version)
# 3. Check Robots.txt
# 
# I did all of these, but the first option should be to kick off GoBuster. It just gives the same results as checking Robots.txt though, a directory called /fuel. <br>
# This brings up a login page. As we have already seen the home page is default, I wonder if the password is too. A quick google gives the login admin/admin.<br>
# ![Ignite_CreatePage.png](../Images/PracticeRooms/Ignite/Ignite_CreatePage.png)<br>
# 
# > Full Disclosure here, I managed to get a file uploaded and it dropped in in /tmp (as a PHP file). When I went to replicate this again at the end I dont know which step I did that got it uploaded. I didnt realise files got uploaded to /tmp until I found it a while later. I'll add my notes at the end of the page but clearly need to note things better. Fortunately theres multiple issues with this box so I found another way....
# 
# So looking around the admin portal, I cant work out how to upload a reverse shell. Lets swap to ExploitDB.<br>
# Searching for "Fuel 1.4" gives quite a few exploits. I picked "Remote Code Execution (3)" because reasons...<br>
# ![Ignite_ExploitDB.png](../Images/PracticeRooms/Ignite/Ignite_ExploitDB.png)<br>
# 
# Download it and run it, and we get a 'shell' <br>
# ![Ignite_RunExploit.png](../Images/PracticeRooms/Ignite/Ignite_RunExploit.png)<br>
# 
# Well... not quite. We can run simple commands but cant change directory or do any of the other fun stuff. But we CAN bring down a reverse shell and drop in in the web server now.<br>
# ![Ignite_WgetReverse.png](../Images/PracticeRooms/Ignite/Ignite_WgetReverse.png)<br>
# 
# We can now bring up the reverse shell with /fuel/reverse.php.<br>
# And we're in, the user flag is here:<br>
# ![Ignite_UserFlag.png](../Images/PracticeRooms/Ignite/Ignite_UserFlag.png)<br>
# 
# <hr>
# 

# ## Escalate Root
# 
# I tried a few basic checks here, SUID, capabilities, cron etc but didnt find anything helpful...<br>
# So, lets bring down some tools. I sent up LinEnum and Linpeas<br>
# ![Ignite_GetEnum.png](../Images/PracticeRooms/Ignite/Ignite_GetEnum.png)<br>
# 
# Running them both gives a few bits of info, Linpeas seemed to get more though so I've just listed them:<br>
# ![Ignite_LinPeasPassword.png](../Images/PracticeRooms/Ignite/Ignite_LinPeasPassword.png)<br>
# ![Ignite_LinpeasResults.png](../Images/PracticeRooms/Ignite/Ignite_LinpeasResults.png) <br>
# 
# So we have a password, and a reasonably confident exploit. I started with the exploit.<br>
# It gives us a bit of info: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt. I also downloaded the exploit kit itself.<br>
# ![Ignite_pwnkit.png](../Images/PracticeRooms/Ignite/Ignite_pwnkit.png)<br>
# 
# In the kit we have a nice readme, that even tells us which exploit to run:<br>
# ![Ignite_PwnkitReadme.png](../Images/PracticeRooms/Ignite/Ignite_PwnkitReadme.png)<br>
# 
# We can grab the version from earlier in LinPeas:<br>
# ![Ignite_UbuntuVersion.png](../Images/PracticeRooms/Ignite/Ignite_UbuntuVersion.png)<br>
# 
# Unfortunately, none of these worked for me. Thats a shame, I've never used PWNKIT before and was hoping to see it in action. Back to the drawing board... wasn't there a password somewhere?<br>
# 
# If we jump back to the home page, we can see there is a few steps. One of them gives us a location for some files.<br>
# ![Ignite_Step2.png](../Images/PracticeRooms/Ignite/Ignite_Step2.png)<br>
# 
# Cat-ing the file gives us the location of that password at the end<br>
# ![Ignite_DBConfig.png](../Images/PracticeRooms/Ignite/Ignite_DBConfig.png)<br>
# 
# Swap to root...<br>
# ![Ignite_Root.png](../Images/PracticeRooms/Ignite/Ignite_Root.png)<br>
# 
# ...grab your flag...<br>
# ![Ignite_RootFlag.png](../Images/PracticeRooms/Ignite/Ignite_RootFlag.png)<br>
# 
# And wait for this whole thing to blow over.<br>
# ![WaitForThisToBlowOver.png](../Images/Generic/WaitForThisToBlowOver.png)
# <hr>

# ## What I didnt get Going
# So, as I mentioend above, I was looking around in the web portal and actually managed to upload a file to /tmp. I dont know how, I was sort of messing around at the time with the assets pages<br>
# ![Ignite_AssestsUpload.png](../Images/PracticeRooms/Ignite/Ignite_AssestsUpload.png)<br>
# 
# I found it in /tmp, but it was a bit surprising, I actually thought it was part of the room where the file was already uploaded.<br>
# ![Ignite_SomeoneHere.png](../Images/PracticeRooms/Ignite/Ignite_SomeoneHere.png)<br>
# 
# Anyways, I moved it to the right location and kicked off my reverse shell.<br>
# ![Ignite_moveit.png](../Images/PracticeRooms/Ignite/Ignite_moveit.png)<br>
# 
# <hr>
# 

# In[ ]:




