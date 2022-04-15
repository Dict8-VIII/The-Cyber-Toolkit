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
# ## Syntax
# 
# > nmap \[ip] [scan method] [MANY arguements] -vv
# 
# - [ip] : The target server IP address
# - [scan method] : -s[something], there can be a number of arguements here
#     - -sV is to try determine what is running behind the ports
#     - -sS sneaky stealth scan
#     - -sA is to try determine OS version (as well as other things, A=Agressive)
#     - -sL \t List the targets that will be scanned, without scanning them. Commonly used with -n
#     - -sn dont port scan (can be combined with -PR)
#     
# - [arguements]
#     - --script [Nmap script]
#     - vuln [ip] \t try determine known exploits
#     - -n \t Dont resolve DNS
#     - -PR \t ARP request only (better be on the same subnet)
#     - -PE \t Use ICMP Echo to discover hosts
#     - -PP \t Use ICMP timestamp instead of echo, useful if echo is blocked
#     - -PM \t Use ICMP address mask instead of echo, useful if echo is blocked
#     - -PS \t Uses TCP SYN to discover hosts. Can add a port or range (without spaces), default is on Port80
#     - -PA \t Uses TCP ACK to discover hosts (they should respond with a RST)
#     - -PU \t Uses a UDP PING
#     - -R \t Lookup DNS names for offline devices
#     
# - -vv : VeryVerbose, stops you going crazy wondering if its working
# 
# 
# 

# ## Why so many scan options?
# 
# ### Discovery
# These are the scan types for target discovery (is there something on this IP worth investigating).
# 
# #### -PR
# This arguement send a broadcast ARP request only. This is a great one to use as it's not blocked by any firewalls (as it's part of maintaining a network), but it requires you to be on the same subnet as your targets.
# 
# #### -PE -PP -PM
# These are ICMP Echo, Timestamp and Mask respectively. All run in the ICMP domain and are ways to work around a firewall. Echo tends to be blocked (and is by default most times). Timestamp and Mask requests are alternatives.
# 
# #### -PS -PA
# These are TCP discovery methods. -PS Uses a SYN request (on port 80 by default) and if it recieved back a response (SYNACK or RST) then treats the IP as active. It just waits for the response if run as priveliged user, or completes the handshake if not. -PA is an ACK message which will recieve a RST if the target is active (as its not part of an established message), and can only be run as priveliged user (otherwise it will run a SYN).
