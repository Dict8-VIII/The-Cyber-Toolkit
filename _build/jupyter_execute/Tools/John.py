#!/usr/bin/env python
# coding: utf-8

# # John The Ripper
# 
# While the namesake is famous for terrorising London, John is just as well known in the Cyber Security space. It is an amazingly versatile tool used for cracking hashes.
# 
# The typical format is:
# > john --wordlist=[wordlist] [file]
# 
# Unfortunately, yes, you have to pass a file containing your hash(s), one per line if you have multiple.
# How the file is formatted depends on what you want to crack.. which leads us to....
# 
# ## What can we crack?
# 
# Well, a lot. Following the above format, pretty much any hash thats in your wordlist. For some hash types, they need to be converted to the format that john expects.
# There is also a useful toold for Identifying the hashes: [HashID](HashID.ipynb)
# 
# ### Linux Logins
# So, youve got a low level account and want to escalate. As linux stores its credentails across 2 files, theres a process to merge them. Oddly enough, as they are in the shadow file, the program is called 'unshadow'
# 
# > unshadow [/etc/passwd file] [/etc/shadow file] > johnready
# 
# you can now pass the "johnready" file to john as per standard
# 
# <hr>
# 
# ### Zip & Rar
# These 2 have been thrown together as they are basically the same thing. Samae as with Linux passwords, they need to be converted
# 
# > zip2john [options] [zip file] > johnready <br>
# > rar2john [options] [rar file] > johnready
# 
# Again, the "johnready" file can now be passed to john directly
# 
# <hr>
# 
# ### SSH
# This should be looking familiar by now, we have zip2john, rar2john, and now ssh2john. This one doesnt come standard though (unless you're on kali). Its also a python script (run in the python environment) so you'll need to have python installed too... which I'm sure you do by now. If you're on kali, its here:
# 
# > python /usr/share/john/ssh2john.py [id_rsa file]
# 
# This gives the passPHRASE, not passWORD.

# In[ ]:




