#!/usr/bin/env python
# coding: utf-8

# # Misc Tools
# 
# Theres a few, https://docs.microsoft.com/en-us/sysinternals/downloads/misc-utilities
# 
# <hr>

# ## BgInfo
# I've always wondered how they do this. This tool displays info on the machines desktop and is really hand if you look after multiple machines.
# 
# <hr>

# ## Regjump
# This is a small tool that jumps you to a location in Regedit instead of having to manually access it. It takes both full name (HKEY_LOCAL_MACHINE) and abbreviation (HKLM). There a few other tools that will run queries on the registry (such as reg query and Get-item/Get-ItemProperty), but this one opens Regedit and puts you in the path specified.
# 
# ### Arguements
# Nice and simple one here
# > regjump HKLM\System\CurrentControlSet\Services\Webclient -accepteula
# 
# <hr>

# ## Strings
# This one searches a file for strings of ASCII or Unicode format with a length of 3+ (by default). A hand tool for investigating a file.
# 
# ### Arguements
# To search a file
# > strings [file]
# 
# To search for files of with certain criteria
# > strings [file] | findstr /i "[search results string]"
# 
# <hr>

# In[ ]:




