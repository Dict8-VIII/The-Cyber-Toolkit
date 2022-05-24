#!/usr/bin/env python
# coding: utf-8

# # Windows PrivEsc
# 
# ## Connecting
# 
# > xfreerdp /u:[user] /p:[password] /v:[host]
# 
# ## Getting the Password File
# 
# For windows its a bit harder. Assuming you are trying to check stored passwords on the local machine; these are stored in the SAM file (and isnt the hardest thing to crack). Metasploit has methods to grab these (such as the hash dump) or your can try mimikatz. The files themselves can be found in C:\windows\system32\Config but this requires decent access already.
