#!/usr/bin/env python
# coding: utf-8

# # HoloLive Walkthrough - Task 9
# 
# So, to start with we are told about Virtual Hosts, GoBuster & Wfuzz. Lets not get ahead of ourselves though, the first question asks for which directory the images on the server are loaded from:
# 
# Theres a few ways to achieve this, but as the question specifically asks about the image directory, lets check that out. Open the web server in your browser, right click the 'image', and select "Copy Image Location"
# 
# ![Hololive-Task9_getLocation.png](../images/Hololive-Task9_getLocation.png)
# 
# Paste it somewhere (I just opened a new tab), and you can see the domain (host)
# 
# ![Hololive-Task9_imageLocation.png](../images/Hololive-Task9_imageLocation.png)
# 
# Easy Question, easy answer :-)
# 
# They wont always be that easy. How you should probably check this is by viewing the source for the image. Right click a blank space and go "view source"
# 
# ![Hololive-Task9_viewSource.png](../images/Hololive-Task9_viewSource.png)
# 
# You'll get a lot of code, look for something that looks like an image (spoiler alert, search .png)
# 
# ![Hololive-Task9_source.png](../images/Hololive-Task9_source.png)
# 
# <hr>

# We have our target, Great! Before we can do some brute forcing, we need to add the server to our hosts
# 
# ![Hololive-Task9_instructions.png](../images/Hololive-Task9_instructions.png)
# 
# I just used nano
# > sudo nano /etc/hosts
# 
# ![Hololive-Task9_hostsfile.png](../images/Hololive-Task9_hostsfile.png)
# 
# Now that that's out of the way lets throw some directories at it and see what sticks.
# 
# The explaination gives us options, Gobuster or Wfuzz. I'm a fan of Gobuster so lets see what we find
# 
# ![Hololive-Task9_gobuster.png](../images/Hololive-Task9_gobuster.png)
# 
# Well thats right to it, questions can be answered

# In[ ]:




