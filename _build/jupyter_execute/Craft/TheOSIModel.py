#!/usr/bin/env python
# coding: utf-8

# # The OSI Model
# 
# The OSI model is one of the fundamental understandings of how networks work. It is a model of 7 layers (or 5 if you're lucky), with the top layer being the most human-readable, and the bottom layer being purely electronics. When data is transferred across a network, it is all done at the bottom level, but having multiple layers allow us to encapsulate (down) or decapsulate (up) data whereby we don’t need to understand how every layer works.
# 
# ## The Layers
# As mentioned above, there are 7 layers in the OSI model. From top - down, these are:
# 
# 7 Application Layer <br>
# 6 Presentation Layer<br>
# 5 Session Layer<br>
# 4 Transport Layer<br>
# 3 Network Layer<br>
# 2 Data Link Layer<br>
# 1 Physical layer<br>
# 
# <hr>

# ## Application Layer
# 
# HTTP, FTP, SMTP, POP3, IMAP
# 
# <hr>

# ## Presentation Layer
# 
# SSL, TLS
# 
# HTTP	80	HTTPS	443 <br>
# FTP 	21	FTPS	990 <br>
# SMTP	25	SMTPS	465 <br>
# POP3	110	POP3S	995 <br>
# IMAP	143	IMAPS	993 <br>
# 
# <hr>

# ## Session Layer
# 
# <hr>

# ## Transport Layer
# 
# TCP, UDP
# 
# <hr>

# ## Network Layer
# 
# IPv4, IPv6, routing
# 
# <hr>

# ## Data Link Layer
# 
# MAC, ARP
# Is actually made up of 2 sub layers
# 
# - LLC: Logical Link Controller. Used for encapsulation
# - MAC: Media Access Control
# 
# IEE 802.11
# 
# 1. ?
# 2. ?
# 3. Ethernet (3u:Fast Ethernet, 3z:gigabit over firbre, 3ab:Gigabit over copper, 3ae:10GB over Fibre)
# 4. ?
# 5. ?
# 6. ?
# 11. Wireless
# 
# ### 802.11.3
# 
# Unicast - 1 to one on MAC
# Broadcast - 1 to all
# Multicast - 1 to group
# 
# ARP - Address Resolution Protocol
# 
# Store and forward switch - get the whole frame then forward after. Can run the checks
# Cut through - Send as you get it, faster but cant check
# Fragment free - send in 64bite groups
# <hr>

# ### Physical layer
# 
# Ethernet, Wi-Fi, Fibre, Pigeon etc
# 1,0,1,1,0,1,0,0
# 
# <hr>
