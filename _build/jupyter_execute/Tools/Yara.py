#!/usr/bin/env python
# coding: utf-8

# # Yara
# 
# Yet Another Ridiculous Acronym.... I think I'm going to like this software :-)<br>
# 
# <hr>
# 

# ## The Basics
# 
# ### What Is Yara?
# 
# Yara is a defensive software that can be used to analyse 'data' to assist with detection of possible threats. In this case, data refers to 'files'. This is achieved via pattern matching.
# 
# <hr>
# 
# ### Installation
# 
# Standard for linux:
# > sudo apt install yara
# 
# For everyone else, visit the repo on Github: https://github.com/virustotal/yara/releases
# 
# <hr>
# 
# ### How Does it Work?
# 
# Yara is a system to create rules in the file system. It can also run these rules against a defined directory. In general,  you create a group of rules and then use these to 'audit' a destination as required. There are many rules available publicly, we'll get to this a bit shortly.<br>
# 
# The rules themselves are quite simple, however the strength of Yara is how these rules are applied by the technical team. A rule itself is a file, and must also include a 'destination. This can be a path, directory or ProcessID. The format is:
# 
# > yara [rule].yar [destination]
# 
# 
# A .yar file is a rule file. When the rule is 'met', it reports with the name of the rule defined in the file. An example rule, shown below, is taken from [https://tryhackme.com/room/yara](TryHackMe's Yara Room)
# 
# ![Yara_BasicRule.png](../images/Tools/Yara_BasicRule.png)
# 
# <hr>
# 

# ## Rules
# 
# The rule file can be populated with many different kinds of 'checks', he full list of rules can be found [here](https://yara.readthedocs.io/en/stable/writingrules.html)<br>
# 
# On the rules note, there also a great infograph available: https://blog.securitybreak.io/security-infographics-9c4d3bd891ef#18dd
# 
# ![Yara_BasicRule.png](https://miro.medium.com/max/1400/1*gThGNPenpT-AS-gjr8JCtA.png)
# 
# <hr>

# ## The Expansion Packs
# 
# So, we've covered the basics about Yara, but Yara also has a lot of friends that really help it shine. Oddly enough, these are all by the same person. Thanks :-). Each of these could be their own page, but I dont know enough about them... yet...
# 
# ### LOKI
# 
# ### THOR
# 
# ### FENRIR
# 
# ### YAYA
# 
# ### YarGen
