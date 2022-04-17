#!/usr/bin/env python
# coding: utf-8

# # Metasploit Framework
# 
# The MetaSploitFramework (msf / Metasploit) is a collection of exploits, payloads, scripts, enum tools,  has its own custom shell, nmap and will probably even walk the dog if you asked nicely enough.
# 
# It also installs a postgresSQL instance, where it stores your history, which must also be running when you launch it.
# 
# ## Launching
# 
# If you need to start the postgress instance manually
# 
# > sudo service start postgressql
# 
# Launching the Console
# 
# > msfconsole
# 
# ## Initial steps
# 
# search for an exploit (includes scanning and post exploit 'exploits')
# 
# > search Eternal_Blue
# > search CVE-2017-0144
# > select # (your number from the list)
# 
# determine which paramaters need to be set
# 
# > options
# 
# Set the paramaters' value (this includes the default payload as described)
# 
# > set Lhost 127.0.0.1
# > set Rhosts 127.0.0.2

# ## Fun exploits
# 
# ### Eternal Blue
# This one is easy, if youre running windows 7 and have SMB enabled (spoiler, they all do), you're screwed
# > search Eternal_Blue
# 
# ### Hashdump
# Dumps all the hashes in an exploited windows box, stores in Metasploit DB.
# > search post/windows/gather/hashdump
# 
# ### Crack Windows
# Follows on from the above hashdump, try to crack the passwords we have... borrowed...
# If its a good password, this is gonna take a while.... use John instead
# > auxiliary/analyze/crack_windows
# 
# ### Escalation Suggester
# One of the built in tools for PrivEx. Requires a session to be created already. I havent had much luck with this though
# > multi/recon/local_exploit_suggester
# 
# <hr>

# In[ ]:




