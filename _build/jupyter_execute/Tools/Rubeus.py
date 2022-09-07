#!/usr/bin/env python
# coding: utf-8

# # Rubeus
# 
# Another tool for attacking kerberos. It is used for harvesting tickets for other attacks. You'll need to run this from a windows box.<br>
# 
# https://github.com/GhostPack/Rubeus <br>
# 
# For many of these attacks, you need to add the DC to the hosts file, this is different from linux
# 
# > echo [ip] [DC] >> C:\Windows\System32\drivers\etc\hosts
# 
# <hr>

# ## Harvesting
# 
# ### Basic
# ![Rubeus_Harvest.png](../images/Tools/Rubeus_Harvest.png)<br>
# 
# <hr>
# 
# ### For Kerberoasting
# First, run Rubeus with the kerberoast mode<br>
# 
# > Rubeus.exe kerberoast
# 
# ![Ruebus_kerberoasting.png](../images/Tools/Ruebus_kerberoasting.png)<br>
# 
# Once you have the hashes dumped, copy to a hash.txt file and crack it against a wordlist using hashcat mode 13100. NOTE: the hash is the entire dumped string, not just the password hash itself (grab everything that is dumped in the 'Hash" field) <br>
# ![Ruebus_HashcatKerberoast.png](../images/Tools/Ruebus_HashcatKerberoast.png)<br>
# 
# <hr>
# 
# ### For AS-REP Roasting
# 
# > Rubeuse asreproast (AS REP ROAST)
# 
# ![Rubeus_ASREP-roast.png](../images/Tools/Rubeus_ASREP-roast.png)<br>
# 
# This time, once you have the hashes dumped you need to modify them so hashcat can do its thing. Add a 23(dollar) after (dollar)krb5asrep(dollar) so that your hash looks something like this<br>
# ![Rubeus_Add23.png](../images/Tools/Rubeus_Add23.png)<br>
# 
# You can then attack with mode 18200
# > hashcat 0m 18200 -a 0 hash.txt wordlist.txt --force
# 
# <hr>

# ## Spraying
# Instead of trying to brute force passwords for a user, you can instead bruteforce users for a specific password. If the password is correct, you get the .kirbi TGT.<br>
# Example from https://tryhackme.com/room/attackingkerberos <br>
# 
# ![Rubeus_Spray.png](../images/Tools/Rubeus_Spray.png)<br>
# 
# <hr>
