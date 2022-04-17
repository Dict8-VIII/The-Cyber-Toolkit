#!/usr/bin/env python
# coding: utf-8

# # HoloLive Walkthrough - Task 10
# 
# So, its time to fuzz some directories. But what does that mean?
# Fuzzing has a few definitions, depending on who you ask.
# * From a known string, modify some characters and try again. This is normally password related in our context. From "Password123"; try "password123", "P@ssw0rd123" etc
# * Brutforce subdomains on a website. From "google.com"; try "admin.google.com", "dev.google.com", "dev.admin.google.com" etc
# 
# For this room, the second option is our goal
# 
# <hr>
# 
# Lets spin up a terminal and see what we can find
# 
# GoBuster Syntax:
# ![GoBuster-DirectoryScanpng.png](../images/GoBuster-DirectoryScanpng.png)
# 
# Wfuzz Syntax:
# 
# ![WFuzz-Example.png](../images/WFuzz-Example.png)
# 
# 
# While gobuster returned inital results faster, the file we are after was found first by GoBuster. Wfuzz did find it eventually.....
# 
# ![Hololive-Task10_robotsFound.png](../images/Hololive-Task10_robotsFound.png)
# ![Hololive-Task10_wfuzzrobots.png](../images/Hololive-Task10_wfuzzrobots.png)
# 
# If we open the robots.txt file, theres a whole load of files listed, they look like directories. Guess we have found our first answer :-)
# 
# ![Hololive-Task10_robots.txt.png](../images/Hololive-Task10_robots.txt.png)
# 
# <hr>
# 
# Apparently we now have and admin domain to find..... fortunately we have just the tool for that.

# ## I didnt actually do it this way....
# So, that was (probably) how the author wanted you to answer the questions. I didnt use GoBuster or WFuzz to start with. Having run into problems with both in the past, I actually ran Nikto first. It didnt give a nice list of files found, but it got the robots file pretty quick....
# 
# ![Hololive-Task10_niktoScan.png](../images/Hololive-Task10_niktoScan.png)

# In[ ]:




