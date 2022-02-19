#!/usr/bin/env python
# coding: utf-8

# # Gobuster
# 
# Gobuster is great software for bruteforcing directories. Naturally its only as good as the wordlists you provide.
# 
# ### Webserver Directories
# You can use GoBuster in the Enum stage for directories, as well as files.
# 
# For Directories
# > gobuster dir -u http://\[IP] -w [wordlist]
# * -u: The URL
# * -w: Path to a wordlist of directories
# 
# For files
# > gobuster dir -u http://\[IP] -w \[wordlist] -x \[extensions]
# * -x: Extension to search for. Can be a comma separated list
# 
# ![GoBuster-DirectoryScanpng.png](../images/GoBuster-DirectoryScanpng.png)

# ### Mode: Webserver vHosts
# A vHost is a second 'virtual' website hosted on your one server. I think technically the first host is a vHost as well, but dont quote me on that... Something to find out....
# 
# Gobuster can scan for these too
# 
# > Gobuster vhost -u http://\[url\] -w \[wordlist\]

# In[ ]:




