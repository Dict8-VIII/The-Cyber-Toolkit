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
#     - -sS sneaky stealth scan. Better known as a TCP SYN scan
#     - -sA is to try determine OS version (as well as other things, A=Agressive)
#     - -sL \t List the targets that will be scanned, without scanning them. Commonly used with -n
#     - -sn dont port scan (can be combined with -PR)
#     - -sT TCP Connect scan
#     - -sU UDP Connect Scan
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
#     - -F \t Fast mode, only scan best 100, not 1000
#     - -r \t Scan ports in order
#     - -t<n>\t The speed of the scan (for IDS evassion). 3 is normal, 1 is SLOW and 5 is 'insane'
#     
# - -vv : VeryVerbose, stops you going crazy wondering if its working
# 
# 
# <hr>

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
# <hr>

# ### Port Connect
# Now that we know what targets to hit, we now have to decide how to confirm a port is open or closed. Because of annoying things like firewalls however, theres more to it. There are 6 possible states of a port scan. This is copied directly from [TryHackMe's nmap02 Room](https://tryhackme.com/room/nmap02)
# 
# 1. Open: indicates that a service is listening on the specified port.
# 2. Closed: indicates that no service is listening on the specified port, although the port is accessible. By accessible, we mean that it is reachable and is not blocked by a firewall or other security appliances/programs.
# 3. Filtered: means that Nmap cannot determine if the port is open or closed because the port is not accessible. This state is usually due to a firewall preventing Nmap from reaching that port. Nmap’s packets may be blocked from reaching the port; alternatively, the responses are blocked from reaching Nmap’s host.
# 4. Unfiltered: means that Nmap cannot determine if the port is open or closed, although the port is accessible. This state is encountered when using an ACK scan -sA.
# 5. Open|Filtered: This means that Nmap cannot determine whether the port is open or filtered.
# 6. Closed|Filtered: This means that Nmap cannot decide whether a port is closed or filtered.
# 
# #### -sT
# The sT scan is a TCP connect scan. Simply, Nmap attempts a full TCP 3way Handshake for each scanned port (and then kill it with a RST ACK if it completes). This is the only scan that doesnt require a priveliged account.
# 
# #### -sS
# The Sneaky Stealth Scan, or more accurately, the SYN scan. This requires a priveliged user and is mroe sneaky as it doesnt complete a connection (so is less likely to be logged). It starts with the SYN, Recieves a SYNACK and then sends a RST to kill the handshake. As you can guess, this is only more stealthy, but could still be logged.
# 
# #### -sU
# The sU scan is a UDP scan, which sort of runs opposite to the TCP scans. As UDP is stateless, we would expect no response if the port is open (as UDP 'packets' dont have a session or give a response, they are fire and forget).<br>
# A closed port however should give a ICMP "Destination Unreachable" response.

# In[ ]:




