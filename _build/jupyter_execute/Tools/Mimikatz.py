#!/usr/bin/env python
# coding: utf-8

# # MimiKatz
# 
# Mimikatz is a post-exploit tool used for dumping user credentials once you already have access to a Windows machine. It can use these tickets.
# 
# ## Install
# Mimikatz is a part of the standard repositories so can be pulled easily
# 
# > sudo apt install mimikatz
# 
# ## Running
# From Windows CMD, just run the EXE. This will update your terminal to "mimikat #" and the below commands must be run inside this environment.<br>
# 
# If you have installed it from the standard repo, and run this in kali it will print the install directory contents, get the exe on the target, it's a post exploit tool...<br>
# ![Mimikatz_Install.png](../images/Tools/Mimikatz_Install.png)
# <hr>

# ## Pass The Ticket
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

# ## I've Got a Golden Ticket
# A golden ticket is fundamentally the ability to create a service ticket for anything. (A silver ticket is the same for a single service/client/user). If you've got a golden ticket, its fundamentally a domain admin, even if domain admin doesnt have rights. Again, we start by checking our privilege<br>
# 
# > privilege::debug
# 
# We can then dump the hash and identifier which will be used to create the Golden Ticket. The top command is for a golden ticket, the second for a silver ticket for the administrator account.
# 
# > lsadump::lsa /inject /name:krbtgt <br>
# > lsadump::lsa /inject /name:administratr <br>
# 
# ![Mimikatz_DumpedGolden.png](../images/Tools/Mimikatz_DumpedGolden.png)<br>
# 
# Next, we pass the data to mimikatz to create the ticket. There are 3 bits of data we need for this.<br>
# ![Mimikatz_DumpedData.png](../images/Tools/Mimikatz_DumpedData.png)<br>
# 
# 1. SID - This is the RED box above
# 2. NTLM - This is the ticket of the 'user'
# 3. RID - We're going to change this to 500 for a golden ticket (or the right level for the silver ticket).
# 
# Plug it into the create function and you'll have a ticket<br>
# 
# ![Mimikatz_CreateGolden.png](../images/Tools/Mimikatz_CreateGolden.png)<br>
# 
# ### How to use it?
# So, now what? You can use this directly in mimkatz now. The below will launch a cmd terminal using the ticket. Do your thing :-)
# 
# > misc::cmd
# 
# <hr>

# ## Skeleton Keys
# 
# Skeletons... Dead skeletons...<br>
# A skeleton key is a 'quieter' back door, which runs in memory on a DC. It only works on Kerberos RC4 encryption. Simply, it creates a 'second' password for the accounts in the system. Your normal login will work, but so will the password with the hash "60BA4FCADC466C7A033C178194C03DF6". Thats 'mimikatz' for those of you who dont read hashes....<br>
# 
# On the domain controller, you ened to run mimikatz with a really difficult command, its looks like this:
# 
# > misc::skeleton
# 
# I know right... So difficult. If this is all OK you can now use the password 'mimikatz' for any user in the domain... spooky<br>
# 
# ![spooky-season-skeleton-dance.gif](../images/Generic/spooky-season-skeleton-dance.gif)<br>
# 
# <hr>

# In[ ]:




