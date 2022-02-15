#!/usr/bin/env python
# coding: utf-8

# # LFI
# 
# LFI, or Local File Inclusion, is a web exploit, where you form a request in which the server passes back data it wasnt supposed to (this could be anything kept on the server, webfiles, stored passwords, local credentials etc). Normally the server runs checks on the requested resource, but there are options...
# 
# ## Finding a vulnerable site
# This vulnerability could present in multiple ways. The most obvious is shown below and can be seen when examining the URL.
# Here, we are requesting a file "userCV.pdf"
# > Note: This is a PHP vulnerability example, but an LFI vulnerability could be seen in other locations as well
# 
# ![image.png](../images/LFI_PHP_FORMAT.png)
# 
# source: https://tryhackme.com/room/fileinc
# 
# 
# 

# ## Easy Methods
# 
# ### The Trivial Path
# The most obvious path to try, is simply request a different file. Instead of "?file=userCV.pdf", how about "?file=secret.txt"
# Tools like BurpSuite or gobuster could automate this process based on wordlists.
# 
# ### Directory Traversal
# The next check, is if we can move "up a level". 
# 
# Normally a linux box will host in "usr/var/www/pages", but that doesnt mean we cant 'ask' for other files
# To move up a level, try "..", "?file=../../../../" puts us in the root directory asking for a file.
# 
# Windows hosts in "C:\inetpub\www"
# To move up a level, its still "..", isnt consistency nice?
# 
# ## Harder Methods
# Now, LFI is a known issue, and there are ways to prevent it. Not all 'fixes' are created equal, and there are ways around many of them.
# 
# ### Filter
# Instead of asking for an executed file, pass a filter to prevent execution (file is stored in /resource)
# > php://filter/resource="file.ext"
# 
# ### Convert Base64
# Can be used instead of filter (file is stored in /resource)
# >convert.base64-encode/resource="file.ext"
# 
# 

# In[ ]:




