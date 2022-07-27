#!/usr/bin/env python
# coding: utf-8

# # Kerbrute
# 
# Kerbrute is a Kerberos user enumeration tool, that attempts to log in using a pre-defined list of usernames. It isnt trying to log in as such, but if it gets a response asking for a password, it assumes the user exists.
# 
# ## Install
# You will need to pull the files from github, and likely run as root to be able to write the files.
# 
# > cd /opt/kerbrute <br>
# > wget https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_linux_amd64 <br>
# > chmod +x kerbrute_linux_amd64 <br>
# 
# ## Running
# You can now run the software from the coppied directory. Red is the Domain, Blue is the IP of the target to try log in to 
# 
# ![Kerbrute_Run.png](../images/Tools/Kerbrute_Run.png)
# 
# 
# <hr>

# In[ ]:



