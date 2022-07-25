#!/usr/bin/env python
# coding: utf-8

# # Impacket
# 
# I came across this tool when doing [Active Directory enumeration](https://tryhackme.com/room/attacktivedirectory). It is a collection of scripts and can be found here: https://github.com/SecureAuthCorp/impacket.git
# 
# ## Installation
# As mentioned above, this is mainly a collection of scripts but it can still be installed. Many of these commands require sudo rights, so you'll need to add this if not running as root.
# 
# > git clone https://github.com/SecureAuthCorp/impacket.git /opt/impacket <br>
# > pip3 install -r /opt/impacket/requirements.txt <br>
# > cd /opt/impacket/ && python3 ./setup.py install <br>
# 
# <hr>

# ## Example Scripts
# 
# ### GetNPUsers.py
# This script is used to enumerate users in the AD, basd on a user list. When I did this, my installation didnt bring over the example scripts so I had to pull these manually.
# 
# > cd /opt/impacket/impacket/examples <br>
# > sudo wget https://raw.githubusercontent.com/SecureAuthCorp/impacket/master/examples/GetNPUsers.py
# 
# 
# You can then run the script, be aware that the Domain needs a / at the end (Red arrow). The Blue arrow is the target IP
# ![Impacket_GetNPUsersExample.png](../images/Tools/Impacket_GetNPUsersExample.png)
# 
# ### SecretsDump.py
# Sounds fun, and it is. This script dumps the hashes of a remote device, as long as you have a login with the rights to do so. The sudo is because I'm writting a file to /opt.... I think.
# 
# > cd /opt/impacket/examples <br>
# > sudo python3 secretsdump.py
# 
# ![Impacket_SecretsDumpExample.png](../images/Tools/Impacket_SecretsDumpExample.png)
# 
# <hr>

# In[ ]:




