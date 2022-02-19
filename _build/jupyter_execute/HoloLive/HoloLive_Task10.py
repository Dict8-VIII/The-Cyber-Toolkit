#!/usr/bin/env python
# coding: utf-8

# # HoloLive Walkthrough - Task 10
# 
# So, its time to fuzz some directories. But what does that mean?
# Fuzzing has a few definitions, depending on who you ask.
# * From a known string, modify some characters and try again. This is normally password related in our context. From "Password123"; try "password123", "P@ssw0rd123" etc
# * Brutforce subdomains on a website. From "google.com"; try "admin.google.com", "dev.google.com", "dev.admin.google.com" etc
# 
# For this room, the second option is our goal

# In[ ]:




