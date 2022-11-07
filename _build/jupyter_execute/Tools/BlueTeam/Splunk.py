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

# ## Splunk Components
# 
# Splunk consists of 3 components, the Indexer, Search and Forwarder.
# 
# ### Forwarder
# The forwarder is simply an agent that is installed on the endpoint to be monitored. It is very lightweight and forwards events to the Splunk server. End points include
# - A web server generating/recieving web traffic
# - A windows machine with Event Logs, sysmon, powershell etc
# - A linux host with its internal logs
# - A DB server with requests, responses and errors
# 
# ### Indexer
# The indexer processes the data it recieves and converts it to a standard format (normalising). This includes creating Key/Value pairs, determining the data type and storage to its internal DB. This is in preparation for the next component.
# 
# ### Search (Search Head)
# Well whats the point in all of this data if you can't search it or apply other rules? This is where the search head comes in. It can also convert the data for visualistions, export and other such tasks.
# 
# <hr>

# ## Navigation
# 
# ### Home Page
# 
# The home page is quite straight forward. The bar at the top is refered to as the "Splunk Bar". The Navigation bar on the Left is the "Apps Panel".<br>
# ![Splunk_HomePage.png](../../images/Tools/BlueTeam/Splunk_HomePage.png)<br>
# 
# The main section above (the "explore splunk") can be replaced with a default dashboard. THe Dashboard studio can assist with this (or just update your splunk versions and you can see it on the home page)
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
