#!/usr/bin/env python
# coding: utf-8

# # HoloLive Walkthrough - Task 10
# 
# So, its time to fuzz some directories. But what does that mean?
# Fuzzing has a few definitions, depending on who you ask.
# 1. From a known string, modify some characters and try again. This is normally password related in our context. From "Password123"; try "password123", "P@ssw0rd123" etc
# 2. Bruteforce subdomains on a website. From "google.com"; try "admin.google.com", "dev.google.com", "dev.admin.google.com" etc
# 
# For this room, the second option is our goal
# 
# <hr>
# 

# ## Fuzzing Some Directories
# 
# Lets spin up a terminal and see what we can find
# 
# GoBuster Syntax:<br>
# ![GoBuster-DirectoryScan.png](../images/Tools/GoBuster_DirectoryScan.png)<br>
# 
# Wfuzz Syntax:<br>
# ![WFuzz-Example.png](../images/Tools/WFuzz_Example.png)<br>
# 
# While gobuster returned inital results faster, the file we are after was found first by GoBuster. Wfuzz did find it eventually.....<br>
# 
# ![Task10_robotsFound.png](../images/HoloLive/Task10_robotsFound.png)<br>
# ![Task10_wfuzzrobots.png](../images/HoloLive/Task10_wfuzzrobots.png)<br>
# 
# If we open the robots.txt file, theres a whole load of files listed, they look like directories. Guess we have found our first answer :-)<br>
# 
# ![Task10_robots.txt.png](../images/HoloLive/Task10_robots.txt.png)<br>
# 
# Apparently we now have and admin domain to find..... fortunately we have just the tool for that.
# 
# <hr>

# ## I didnt actually do it this way....
# So, that was (probably) how the author wanted you to answer the questions. I didnt use GoBuster or WFuzz to start with. Having run into problems with both in the past, I actually ran Nikto first. It didnt give a nice list of files found, but it got the robots file pretty quick....
# 
# ![Task10_niktoScan.png](../images/HoloLive/Task10_niktoScan.png)
# 
# <hr>
