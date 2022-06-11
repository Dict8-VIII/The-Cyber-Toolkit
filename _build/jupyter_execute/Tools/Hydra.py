#!/usr/bin/env python
# coding: utf-8

# # Hydra
# If youre trying to brute force a login, (THC) Hydra is the place to be. It supports MANY protocols, is very efficient and amazingly versatile.
# 
# ## Examples
# The basic structure of attacks doesnt really change unless youre doing something special.
# 
# > hydra -l OR -L [login or list of logins] -p OR -P [password or list of passwords] [target] [protocol] [arguements]
# 
# Arguement options:
# - -t n : use n threads, 16 is high
# - -s n : use this port if non-standard
# - -I : dont use the restore file, and it's ok to override
# 
# It looks complicated, but it's actually quite simple. Some examples
# 
# ### IMAP
# This example is taken from the [TryHackMe "Protocols and Servers 2" room](https://tryhackme.com/room/protocolsandservers2).
# 
# > hydra -l lazie -P /home/kali/rockyou.txt 10.10.206.48 imap -t 16 -I
# 
# ![Tools-Hydra_IMAP.png](../images/Tools-Hydra_IMAP.png)
# 
# Breaking this down, we have
# 
# - hydra : run hydra
# - -l : use this specific login for all attempts
# - -P : use this list of passwords to itterate through
# - 10.10.206.48 : my target IP
# - imap : attack the IMAP service (default port 143)
# - -t 16 : use 16 threads
# - -I : dont wait, just override the restore file
# 
# <hr>

# ## Web Forms
# 
# We can also use hydra to attack a web form login (instead of the time limited burpsuite). Unfortunately we can only use 1 wordlist though so its a 'sniper' attack. We can swap the user/password to use a wordlist but it's for the user here.
# 
# > hydra -L < file> -p < known password> [ip] http-post-form "/url.ext:log=^USER^&pwd=theknownpassword:Invalid username" -t 30
# 
# - ^USER^ is where the defined username will be put
# - ^PASS^ is where the defind password will be put
# 
# So, why did we do all of this? In this case it is an attack where the browser reports back if the user or password is invalid. As we are iteratting through users, its the invalid username response we care about (if it changes).
