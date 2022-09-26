#!/usr/bin/env python
# coding: utf-8

# # Recon-ng
# 
# This is a framwork for automating (some of) the common OSINT tasks. It comes at a base level and modules are added on to increase the functionality. Some modules require an API key as well. If you ever get stuck in a 'context', type 'back' to return one level
# 
# ## The Basics
# 
# ### Install
# It's part of the standard repositories
# > sudo apt install recon-ng
# 
# ### Run
# Nice and easy
# 
# > recon-ng
# 
# If its your first time running, there wont be any modules installed. You'll also see your terminal swap to the recon-ng name (with your workspace)<br>
# ![Recon-ng_Run.png](../images/Tools/Recon-ng_Run.png)
# 
# ### Workspaces
# As with many tools, you can set workspaces to isolate investigations.
# 
# - Create a workspace
#   - workspaces create [workspace_name]
#   
# <hr>

# ## General Process
# 
# In a workspace, you will want to start with known data and use that to populate more relevant data. Sounds simple, right? Well..... not really. There's a DB sitting underneath and you can see its schema with
# 
# >db schema
# 
# ### Inserting a Domain
# So, lets say we start with a domain name, we will want to drop that into the db.
# 
# > db insert domains<br>
# > [enter your domain]<br>
# 
# ![Recon-ng_InsertDomain.png](../images/Tools/Recon-ng_InsertDomain.png)<br>
# 
# ### Finding More Modules (marketplace)
# Like many OS, Recon-ng comes with its own marketplace for finding more modules. Modules are split into categories such as discover, import, recon and reporting. Some of these also have subcategories. The modules are named based on the source and resulting data.
# 
# - Marketplace search [query]
#   - search for modules (a blank query gives all)
# - marketplace info [module]
#   - get info about a module
# - marketplace install [module]
#   - install a module
# - marketplace remove [module]
#   - uninstall a module
# 
# ### Loading a Module
# Once you have a module installed, you can now load it into memory
# 
# - modules search [query]
#   - list installed modules, again an empty query is all
# - modules load [module]
#   - loads the module to memory to provide arguements to
# - options list
#   - lists all options
# - options set [option] [value]
#   - set an option to a value
# - run
#   - runs the module
#   
# <hr>

# In[ ]:




