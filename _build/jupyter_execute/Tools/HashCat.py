#!/usr/bin/env python
# coding: utf-8

# # Hashcat
# 
# Similar to John The Ripper, Hashcat is used for well... hashes....
# Unlike John however, hashcat requires that you define the mode (hash type) and attack method.
# 
# <hr>

# ## Running Hashcat
# 
# > hashcat -m [the mode number] -a [the attack method] [the file with hashes listed] [a wordlist or charset] <br>
# > hashcat -m [the mode number] -a [the attack method] [the single hash value] [a wordlist or charset]
# 
# The file could include salts as well, depending on the mode number defined. <br>
# There is also a useful tool for Identifying the hashes: [HashID](HashID.ipynb) <br>
# There are a LOT of modes (hash types) that can be cracked. To see the list <br>
# 
# > hashcat -h
# 
# * 0:      MD5
# * 100:    SHA1
# * 1800:   sha512crypt
# 
# The attack modes are easier, theres only 5
# 
# * 0 : Straight
# * 1 : Combination
# * 3 : Brute-Force (this includes dictionary)
# * 6 : Hybrid Wordlist + Mask
# * 7 : Hybrid Mask + Wordlist
# 
# <hr>

# ## Formatting of Hash File
# It can be frustrating getting the hashes in the right format, but Hashcat includes a method for this too, where it gives what is expected in the hash file
# 
# ![Hashcat_ExampleHashFormat.png](../images/Tools/Hashcat_ExampleHashFormat.png)
# 
# <hr>

# ## Example Commands
# 
# ### Single Hash, Type SHA-1, against RockYou
# 
# > hashcat -m 100 -a 3 8d6e34f987851aa599257d3831a1af040886842f /usr/share/seclists/Passwords/Leaked-databases/rockyou.txt
# 
# Spoiler: sunshine
# 
# ### Single Hash, Type MD5, 4 Digits longs
# 
# > hashcat -m 0 -a 3 e48e13207341b6bffb7fb1622282247b ?d?d?d?d
# 
# Spoiler: 1337
# <hr>

# In[ ]:




