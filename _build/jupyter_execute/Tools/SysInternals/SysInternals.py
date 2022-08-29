#!/usr/bin/env python
# coding: utf-8

# # SysInternals
# 
# https://tryhackme.com/room/btsysinternalssg
# 
# ## Installing
# https://docs.microsoft.com/en-us/sysinternals/downloads/
# 
# From your folder, recommened to add ot env variables (path), otherwise will have to navigate.<br>
# Once added, just run from cmd:
# > sysdm.cpl 
# 
# ## Running Live
# Can be launched live, without downloading. On windows, you need to enable some services and features. It uses the live link to run the software without downloading locally. https://live.sysinternals.com/. These setps follow running the tools from CMD.
# 
# > \\live.sysinternals.com\tools\procmon.exe
# 
# It fails, we need to add a few things.
# 
# 1. Make sure WebDav is installed. (it is by default on client, but not server builds)<br>
#     a. Run: Install-WindowsFeature WebDAV-REdirector -Restart<br>
#     b. Can check with: Get-WindowsFeature WebDAV-Redirector | Format-Table -Autosize<br>
# 2. Enable WebDav protocol<br>
#     a. get-service webclient<br>
#     b. start-service webclient<br>
# 3. Enable Network Discovery<br>
#     a. Can do it from "Network and Sharing Center" in Control Panel<br>
#     b. Otherwise: control.exe /name Microsoft.NetworkAndSharingCenter<br>
#     c. Advanced Sharing Settings -> Turn on network discovery.<br>
#     
# Now we can try it again
# 
# ### Mapping Drive
# As a middle ground, you can also map the drive<br>
# >net use * \\live.sysinternals.com\tools\
# 
# The * is to use any drive letter.
# 
# <hr>
# 

# In[ ]:




