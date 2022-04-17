#!/usr/bin/env python
# coding: utf-8

# # Netcat
# 
# Another one of the very versatile fundamentals of exploitation, netcat is one of those programs that becomes second nature to an Ethical Hacker.
# 
# ## Setting up a Listener
# A number of exploits create a 'reverse shell', in which the exploited machine calls back to the attacker. Part of this, is that you must set up a listener to recieve this call.
# 
# > nc -lvnp \[port]
# 
# * l -> Listen
# * v -> verbose logging
# * n -> dont resolve DNS
# * p -> next arguement is the port to listen on
# 
# <hr>

# In[ ]:




