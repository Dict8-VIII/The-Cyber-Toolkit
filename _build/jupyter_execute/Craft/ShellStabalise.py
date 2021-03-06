#!/usr/bin/env python
# coding: utf-8

# # Stabilizing a shell
# 
# The problem with certain exploits, is that the reverse shell isn’t the most stable medium
# 
# * It doesn't have autofill
# * CTRL+C will kill the listener (cant kill a launched program)
# 
# <hr>
# 

# ## Method 1 - Linux w/ Python
# 
# The easiest method (if you can do it), is to simply launch a new shell on the remote machine. Being easy, it also has some requirements
# 
# * Python needs to be installed on the remote machine
# * This method is the LINUX version, because Linux tends to come with python already installed
# 
# On the remote shell, spawn a new shell
# NOTE: This may need to be python3 launched instead, depending on what is installed remotely
# > python -c 'import pty; pty.spawn("/bin/bash")'
# 
# Set Environment?
# > export TERM=xterm
# 
# Background the 'nested' shell so we can make some changes to our main one
# > CTRL+z
# 
# Turn off echo on the 'main' shell, then jump back to the 'nested' shell
# > stty raw -echo; fg
# 
# NOTE: Our own echo is gone now, if you want it back, run 'reset'
# <hr>
# 

# ## Method 2 - rlwrap
# 
# Only slightly harder than above, rlwrap needs to be installed locally (and doesn’t come with most distros)
# 
# Once its installed, instead of listening direct with Netcat, just pass it as an argument to rlwrap
# 
# > rlwrap nc -lvnp \[port]
# 
# You will still need to disable local echo, same steps as above
# 
# <i>Background the 'nested' shell so we can make some changes to our main one<br>
# 
# > CTRL+z
# 
# <i>Turn off echo on the 'main' shell, then jump back to the 'nested' shell<br>
# 
# > stty raw -echo; fg
# 
# <hr>
# 

# ## Method 3 - socat
# 
# Even harder than the other 2, as you need to install software remotely (socat). If you can install software remotely, you've probably already got some level of access
# 
# Copy the SOCAT binary to the remote machine (normally via a remote webserver)
# Follow your nose
# <hr>

# In[ ]:




