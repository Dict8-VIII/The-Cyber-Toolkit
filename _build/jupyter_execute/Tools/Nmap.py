#!/usr/bin/env python
# coding: utf-8

# # Nmap
# 
# Nmap is a Scanning tool used for the enumeration stage of Pen Testing. It is very versatile and industry standard.
# 
# Common usages
# - Port Scanning
# - Service Enum
# - Running Nmap scripts for specific enum
# 
# ### Syntax
# 
# > nmap \[ip] [scan method] [MANY arguements] -vv
# 
# - [ip] : The target server IP address
# - [scan method] : -s[something], there can be a number of arguements here
#     - -sV is to try determine what is running behind the ports
#     - -sS sneaky stealth scan
#     - -sA is to try determine OS version
# - [arguements]
#     - --script [Nmap script]
#     - vuln [ip] \t try determine known exploits
# - -vv : VeryVerbose, stops you going crazy wondering if its working

# In[ ]:




