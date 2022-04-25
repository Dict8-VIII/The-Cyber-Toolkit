#!/usr/bin/env python
# coding: utf-8

# # TCPDump
# 
# TCPDump is an open source CLI program for listening to traffic. As with any eavesdropping software, you must already have a 'listener' available. This could be:
# - A wireless listener
# - Wiretap
# - Port Mirroring (on a switch)
# - etc.
# 
# > sudo tcpdump port [portnumber] -A
# 
# You need sudo rights to run packet capture.<br>
# -A forces the results to be in ASCII.
# 
# <hr>
