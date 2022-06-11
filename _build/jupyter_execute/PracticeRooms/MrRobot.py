#!/usr/bin/env python
# coding: utf-8

# # MR Robot CTF room
# 
# NMap scan
# 
# - 80 gives a console, with text.... logged in as root?
# 
# Nikto (nikto -host < ip>)
# 
# - Theres a robots.txt..
# - It has a dictionary and flag 1
# 
# dictionary is a list of.... passwords?
# 
# dirbuster
# - gives a few login pages; /admin /login
# 
# brute force.... burp or Hydra
# - we only have one list.... the page gives back if we have the wrong user or password, so break on length.
# - This gives the user 'Elliot'.
# - now we can itterate through passwords
# 
# 
# 
