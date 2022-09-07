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
# 
# Another Page recommends 0.9.20 + are quite unstable, try 0.9.19<br>
# https://tryhackme.com/room/attackingkerberos<br>
# 
# > cd /opt<br>
# > wget https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_19/impacket-0.9.19.tar.gz<br>
# > unpack it<br>
# > cd Impacket-0.9.19<br>
# > pip install .<br>
# 
# <hr>
# 
# And another...<br>
# 
# This is taken from https://tryhackme.com/room/zer0logon<br>
# 
# > python3 -m pip install virtualenv<br>
# > python3 -m virtualenv impacketEnv<br>
# > source impacketEnv/bin/activate<br>
# > pip install git+https://github.com/SecureAuthCorp/impacket<br>
# 
# 
# <hr>

# ## Kerberoasting
# 
# > cd/usr/share/doc/python3-impacket/examples
# > sudo python3 GetUserSPNs.py [domain]/[Machine1:Password1] -dc-ip [DC IP] -request
# > pass dumps to hashcat: hashcat -m 13100 -a 0 hash.txt wordlist.txt
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
# <hr>
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
