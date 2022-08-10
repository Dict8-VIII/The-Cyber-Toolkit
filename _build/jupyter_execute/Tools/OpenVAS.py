#!/usr/bin/env python
# coding: utf-8

# # OpenVAS
# 
# THM Room : https://tryhackme.com/room/openvas
# 
# Web App and endpoint scanner for vulnerabilities.
# Part of GreenBone Vulnerability Management solution.
# 
# 
# Taken from : https://tryhackme.com/room/openvasTaken 
# 
# ![GVM_Framework.png](../images/Tools/GVM_Framework.png)
# 
# 

# ## Installation
# 
# From Repos:
# https://websiteforstudents.com/how-to-install-and-configure-openvas-on-ubuntu-18-04-16-04/
# https://www.agix.com.au/installing-openvas-on-kali-in-2020/
# 
# From Source:
# https://github.com/greenbone/openvas-scanner/blob/master/INSTALL.md
# 
# For Docker (prefered)
# https://github.com/mikesplain/openvas-docker
# https://hub.docker.com/r/mikesplain/openvas/dockerfile
# 
# > apt install docker.io<br>
# > docker run -d -p 443:443 --name openvas mikesplain/openvas
# 
# Can then open in 127.0.0.1 (browser)<br>
# Default credentails admin/admin
# 
# <hr>

# ## Intial Config / Basic scan
# 
# Scans > Tasks and click purple wand to set up a scan.<br>
# Scans > reports to see progress and prev reports <br>
# 
# run against 127.0.0.1 to test
# 
# 
