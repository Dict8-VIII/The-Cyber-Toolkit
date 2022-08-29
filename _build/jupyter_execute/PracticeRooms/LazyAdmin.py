#!/usr/bin/env python
# coding: utf-8

# # LazyAdmin
# 
# Welcome to the LazyAdmin room. This is a easy level room which is completely self guided, you are asked for the user flag (gaining a shell) and then the root flag, escalating to root. There is a bit of research needed here but it's one of the easier rooms I've done so far, with a few little 'got-ya-s'. I'll mention these when I get to them.
# 
# <hr>

# ## First Steps
# So, we've got an IP, lest start with a scan. Nmap gives us 2 ports on the standard scan. <br>
# ![LazyAdmin_Nmap.png](../images/PracticeRooms/LazyAdmin_Nmap.png)<br>
# 
# So we have HTTP and SSH. SSH tends to be a later stage step, so lets bring up the HTTP connection. It looks to be the default page. Guess where the Lazy in the room came from...<br>
# 
# Nothing looks obvious here, lets spin up GoBuster and Nikto. For me, GoBuster gave the first bit of useful info, a /content directory.<br>
# ![LazyAdmin_GoBuster.png](../images/PracticeRooms/LazyAdmin_GoBuster.png)<br>
# 
# Bring up this page brings us a default page for "sweetrice", a CMS system. Great. Theres a few pages on Exploit-DB about sweetrice, but for the sake of investigation I didnt start here. If you want to skip ahead, go to the end of the chapter and use the login in the /content/as directory.<br>
# 
# Running GoBuster on the /content directory gives us a few more sub directories
# - /inc
# - /as
# - /images
# - /_themes
# - /attachment
# 
# These are more interesting than the content page. A few are browsable directories and the /as is a login page. <br>
# ![LazyAdmin_LoginPage.png](../images/PracticeRooms/LazyAdmin_LoginPage.png)<br>
# 
# As we dont have any logins yet, lets start with directory browsing. The images page is boring, /inc gives us some fun data though. We get version 1.5.1 from the Lastest.txt file (good England there...) but the backup directory also looking quite tasty. We have a SQL backup in there.<br>
# ![LazyAdmin_BackupLocation.png](../images/PracticeRooms/LazyAdmin_BackupLocation.png)<br>
# 
# Using your tool of choice, examining the backup drops all the tables then repopulates them. A weird backup process but OK... However when we examine the file, the repopulation includes the Admin account in the database. Cool. I just threw it into crackstation and it came back with a password.<br>
# ![LazyAdmin_BackupDetails.png](../images/PracticeRooms/LazyAdmin_BackupDetails.png)<br>
# 
# The file can be a bit hard to read, but the Admin Account is "manager" with the password "Password123". Throw it into your login page and we are now connected
# 
# <hr>

# ## Getting to a Shell
# 
# jump to ads, add a new one and copy the reverse shell script. name code. Start listener and navigate<br>
# ![LazyAdmin_AdsExploit.png](../images/PracticeRooms/LazyAdmin_AdsExploit.png)<br>
# 
# http://10.10.221.72/content/inc/ads/code.php
# 
# user flag is in itguy's folder<br>
# ![LazyAdmin_UserFlag.png](../images/PracticeRooms/LazyAdmin_UserFlag.png)<br>
# 
# theres a sql login: rice:randompass<br>
# 
# can run sudo -l, gives a perl script with sh running.... helpful.. but its only root writable<br>
# ![LazyAdmin_Sudo.png](../images/PracticeRooms/LazyAdmin_Sudo.png)<br>
# 
# The shell itslef runs somethign else though. which we can write too<br>
# ![LazyAdmin_copySH.png](../images/PracticeRooms/LazyAdmin_copySH.png)<br>
# 
# It keeps not allowing sudo even though we have NoPasword enabled.... annoying. Fix is here<br>
# ![LazyAdmin_GetRoot.png](../images/PracticeRooms/LazyAdmin_GetRoot.png)<br>
# 
# flag is /root/root.txt
