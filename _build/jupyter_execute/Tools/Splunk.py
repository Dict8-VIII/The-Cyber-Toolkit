#!/usr/bin/env python
# coding: utf-8

# # Splunk
# 
# ## Installation
# 
# 1. Head to https://www.splunk.com/ and create a free account
# 2. Download from the same location (or wget, they provide a nice link)
# 3. Chmod +x [file]
# 4. Install
# > sudo dpkg -i [file]
# 5. Its now installed in /opt/splunk
# 6. Can now launch by running the below in the /opt/splunk/bin directory (need sudo on first run)
# > ./splunk start --accept-license
# 7. You'll be asked for the first admin account. Default is 'admin' with your password
# 8. Your service is now started at localhost:8000
# 
# <hr>

# ## SPL - Search Programming Language
# 
# SPL Consists of 5 components
# 1. Search Terms
# 2. Commands
# 3. Functions
# 4. Arguements
# 5. Clauses
# 
# When running a search, you can have one or more of these. The are separated by pipes in the search (as an AND)<br>
# 
# ### Search Terms
# 
# Wildcard * are supported <br>
# Boolean (AND, OR, NOT) are supported <br>
# "Quotes" are supported <br>
# Can escape quotes in search with a \ <br>
# Can do () to make order of events (like (x and y) OR Z) <br>
# 
# When you search, it reads results into ram. Each command is a separate query so results are 'cleared' when removed.
# 
# - RENAME : renames a table result
# - DEDUP : removes duplicates based on a key (or key column)
# 
# <hr>

# ## User Accounts
# Theres multiple leves for the web portal. Main ones are Power and User.<br>
# The default account is setup during first run (above)
