#!/usr/bin/env python
# coding: utf-8

# # Hashcat
# 
# Similar to John The Ripper, Hashcat is used for well... hashes....
# Unlike John however, hashcat requires that you define the mode (hash type) and attack method.
# 
# ## Simple Example
# 
# > hashcat -m [the mode number] -a [the attack method] [the file with hashes listed]
# 
# The file could include salts as well, depending on the mode number defined. <br>
# There is also a useful tool for Identifying the hashes: [HashID](HashID.ipynb) <br>
# There are a LOT of modes (hash types) that can be cracked. To see the list <br>
# 
# > hashcat -h
# 
# * 0:      MD5
# * 100:    SHA1
# * 1800:   sha512crypt ( &#36;6&#36; hashes)
# 
# The attack modes are easier, theres only 5
# 
# * 0 : Straight
# * 1 : Combination
# * 3 : Brute-Force
# * 6 : Hybrid Wordlist + Mask
# * 7 : Hybrid Mask + Wordlist
# 
# <hr>
# 
# ## Formatting of Hash File
# It can be frustrating getting the hashes in the right format, but Hashcat includes a method for this too, where it gives what is expected in the hash file
# 
# ![Hashcat_ExampleHashFormat.png](../images/Tools/Hashcat_ExampleHashFormat.png)
# 
# <hr>

# In[ ]:




