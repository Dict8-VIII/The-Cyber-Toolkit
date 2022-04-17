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
#     - -sA is a ACK scan. This is more for understanding firewall rules.
#     - -sN is a NULL scan, set all flags '0'
#     - -sF is a FIN scan, and sets the FIN flag only
#     - -sX is an XMAS scan, it sets FIN, PSH and URG. Shiny....
#     - -sM is the Maimon scan, used against a particular OS (BSD, Berkley Software Distribution). It's discontinued... but you never know.
#     - -sW is a Window Scan, it reads the response of a RST flag.
#     - -sI is an idle (zombie) scan. It requires a very specific case
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
#     - -S \t for spoofing IP addresses
#     - -D \t for creating Decoys
#     - -f \t for fragmenting packets into 8bytes (or -ff for 16 bytes)
#     
# - -vv : VeryVerbose, stops you going crazy wondering if its working
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
# A closed port however should give a ICMP "Destination Unreachable" response. This still searches for a TCP port, not UDP.
# 
# #### -sN
# The NULL scan sets all the flag bits to zero. If a port is open, we would expect no response, but if it's closed then we would recieve a RST. A firewall would also give no response, so Nmap treats this as Open | Filtered.
# 
# #### -sF
# The FIN scan sends only the FIN flag in a port connect. Similar to the null scan, it is looking for no response to indicate an open port. Once again this can only return Open | Filtered.
# 
# #### -sX
# The XMAS scan is named after the lights on a christmas tree, it sets the FIN, PSH and URG flags (All the special case flags). If you had a warning system in the TCP protocol, it would light up everything. As with a NULL and FIN scan, it's looking for no response, and gives Open | Filtered.
# 
# #### -sM
# The Maimon scan is a special case, but we like them. This sends a FIN/ACK message. On most OS, this will return a RST if the port is open or closed, not so helpful. Some BSD (Berkely Software Distribution) OS' drop the packet however if the port is open. The BSD OS isnt widely used, but there are some interesting ones on [wikipedia](https://en.wikipedia.org/wiki/List_of_BSD_operating_systems), such as FreeNAS and the PS3.
# 
# #### -sA
# This is an ACK scan, and by itself an ACK scan doesnt show much. It sets the ACK flag and a host should return RST whether the port is open or closed. However if there is a firewall in between, it will drop the packet. Therefore this scan is used for understanding what is allowed through a firewall. This scan returns an Unfiltered state for 'allowed' ports.
# 
# #### -sW
# A window (not WINDOWS) scan is similar to an ACK scan, however it examines the RST reponse to try determine more information about the port (such as if it's open).
# 
# #### Custom Scan
# You can also create a custom scan, --scanflags [flags to set]
# > for example: sudo nmap 127.0.0.1 --scanflags SYNACKURG
# 
# Naturally, you will need to understand how to interpret these results yourself however.
# 
# #### -sI
# This is the idle scan and is a scan method that is used when trying to evade detection. I requires a 'zombie' machine which is Idle on the network. What this means is that it is transmitting NO data during the scan time, other than what we trigger. There are a few steps to this scan, but it is basically a masked TCP Connect (-sT) scan.
# 1. Send a SYNACK to the idle machine, from this we get back the current packet number ID of the zombie.
# 2. Send a SYN packet to the target machine, with a spoofed IP of the zombie.
# 3. The target will then communicate with the zombie based on its port state.
# 4. Query the zombie again with a SYNACK, and compare the new packet number to the old one.
# 
# If the port was closed on the target, it would have sent a RST packet to the zombie, which doesnt increase its counter. When we query the zombie again, it would have only increased its counter by 1 (us sending the SYNACK a second time).<br>
# If the port was open on the target, it would have sent a SYNACK to the zombie, which wouldh have responded to the target with a RST and increased its own counter. Would would have seen the counter increase by 2 on our second SYNACK. <br>
# If a firewall was blocking the port, we would have the same response as a closed port.
# 
# <hr>

# ## Evasion
# 
# ### Spoof IP -S
# Nmap supports spoofing the source IP of a packet scan, which sounds great but comes with a few requirements. First, you need to be able to listen to the responses to the Spoofed IP. Second, you will likely need to specify the network interface to use. If you want to spoof your MAC, this only makes sense if youre already on the subnet too.
# 
# > nmap -e [Net Interface] --spoof-mac [spoofed MAC] -S [spoofed IP] [target IP]
# 
# <hr>
# 
# ### Decoys -D
# Decoys are another way to hide the source of the traffic. You list a group of IPs to show where the traffic is coming from, and NMAP will run these in parallel. You can also use RND which will randomly create an IP.
# 
# > nmap -D [fake IP1],[fake IP2],[real IP (ME)],[fake IP3]....many more
# 
# <hr>
# 
# ### Fragmentation -f
# Fragmentation is a way to split up packets to make things more difficult for some firewalls, IDS and IPS. Adding a -f will split the packet into 8byte fragments and transmit these seperately. -ff will make it 16 bytes instead.
# 
# <hr>
# 
# ### Zombie Scan (-sI)
# A zombie scan is a method that uses an "idle zombie" to communicate with the target, while spoofing your own IP to make the request appear to be coming from the idle host. More details are in the scan types above.

# In[ ]:




