#!/usr/bin/env python
# coding: utf-8

# # LFI
# 
# LFI, or Local File Inclusion, is a web exploit, where you form a request in which the server passes back data it wasnt supposed to (this could be anything kept on the server, webfiles, stored passwords, local credentials etc). Normally the server runs checks on the requested resource, but there are options...
# 
# ![image.png](attachment:07a2cfa3-7ecc-4855-a0c6-4a91348d4689.png)
# source: https://tryhackme.com/room/fileinc
# 
# ## Methods
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
# 

# In[ ]:




