#!/usr/bin/env python
# coding: utf-8

# # Binwalk
# 
# Binwalk is a steganography tool used for examining a file and separating data that has been hidden within it. This data is mainly extra files.
# 
# ## Installation
# 
# Binwalk comes installed on kali by default, but if you are extracting zip files, you need the JDK installed
# 
# > sudo apt install default-jdk
# 
# ## Examining a File
# You can examine a file simply by passing it to Binwalk
# 
# > binwalk cutie.png
# 
# If files are found, you can then extract them with a -e. They are then stored in a subfolder of your current location
# 
# ![Binwalk_Example.png](../images/Tools/Binwalk_Example.png)
# 
# <hr>

# In[ ]:




