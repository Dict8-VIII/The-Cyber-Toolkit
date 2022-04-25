#!/usr/bin/env python
# coding: utf-8

# # The OSI Model
# 
# The OSI model is one of the fundamental understandings of how networks work. It is a model of 7 layers (or 5 if you're lucky), with the top layer being the most human-readable, and the bottom layer being purely electronics. When data is transfered across a network, it is all done at the bottom level, but having multiple layers allow us to encapsulate (down) or deencapsulate (up) data whereby we dont need to understand how every layer works.
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
# ### Application Layer
# HTTP, FTP, SMTP, POP3, IMAP
# 
# ### Presentation Layer
# SSL, TLS
# 
# HTTP	80	HTTPS	443 <br>
# FTP 	21	FTPS	990 <br>
# SMTP	25	SMTPS	465 <br>
# POP3	110	POP3S	995 <br>
# IMAP	143	IMAPS	993 <br>
# 
# ### Session Layer
# 
# ### Transport Layer
# TCP, UDP
# 
# ### Network Layer
# IPv4, IPv6, routing
# 
# ### Data Link Layer
# MAC, ARP
# 
# ### Physical layer
# Ethernet, Wifi, Fibre, Pigeon etc
# 1,0,1,1,0,1,0,0

# In[ ]:




