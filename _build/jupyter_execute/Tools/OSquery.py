#!/usr/bin/env python
# coding: utf-8

# # OS Query
# 
# OSquery is an open source terminal level sql syntax application. Odly enough, its built by facebook. It's main application is still the cyber security field however. It can be installed from the standard sources, details are here https://osquery.readthedocs.io/en/stable/installation/install-linux/<br>
# 
# Once installed, you can launch the application with 
# > osqueryi
# 
# Yes, that "i" is a part of it.... I've also taken a lot of this page from my progress in the [tryhackme OSquery room](https://tryhackme.com/room/osqueryf8). If youre on the same page, remember the questions are for the version of OSquery installed on the provided VM, not the 4.7.0 in the images. That one stumped me for a bit as I'm on my own one.
# 
# <hr>
# 

# ## Basic Syntax
# 
# OSquery is a console application based on the SQLite application. <br>
# The cmd-line flags can be found here: https://osquery.readthedocs.io/en/latest/installation/cli-flags/<br>
# "meta" commands can be identified by starting with a ".", for example <br>
# - .help will bring up the help window<br>
# - .exit will exit the program (so will .quit)<br>
# - .show gives current settings (environment)<br>
# 
# 
# 
# ### Querying the Database
# First, we will want to see what tables we have<br>
# > .tables
# 
# This will list all the tables in the database. If we wanted to filter for something helpful in the name, just add it as a string at the end<br>
# > .tables system
# 
# We can see the format, or schema of a table by querying it's schema. This will give us data such as the columns and their types<br>
# For further info on the schemas, go [here](https://osquery.io/schema/5.5.1/). It's the 5.5.1 one<br>
# > .schema table_name
# 
# As for the actual queries, we are only ever 'selecting', no update or drop here... (at least for most tables). <br>
# As with 'normal' select statements, we will also have a FROM, but all queries must end with a semicolon ';'... I'm getting C flashbacks....<br>
# > select * from system;<br>
# 
# ![OSquery_AllFromSystemInfo.png](../images/Tools/OSquery_AllFromSystemInfo.png)<br>
# 
# We can also do specific columns<br>
# > select hostname, cpu_physical_cores, physical_memory from system_info;<br>
# 
# ![OSquery_SomeFromSystemInfo.png](../images/Tools/OSquery_SomeFromSystemInfo.png)<br>
# 
# Or if its really busy, we can just get a count from the table<br>
# > select count(*) from processes;<br>
# 
# ![OSquery_Count.png](../images/Tools/OSquery_Count.png)<br>
# 
# <hr>
# 

# ## More Advanced Syntax
# 
# Matching wildcards / rules
