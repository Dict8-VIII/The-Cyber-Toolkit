#!/usr/bin/env python
# coding: utf-8

# # SQL Injection
# Source: https://tryhackme.com/room/sqlinjectionlm
# 
# ## The Basics of SQL
# SQL, or "structured query language" is a scripting language used where querying a database.<br>
# What is a database? Its a collection of tables (and a few extra things) which are used to store data.<br>
# What is a table? Think of it like an excel sheet, with columns and rows. Instead of the columns being A,B,C etc however, they are each named. <br>
# 
# How do you write SQL?
# 
# > Carefully! A query in the wrong spot is not going to be fun for anyone.
# 
# - A SELECT statement is used to ask for data
# - A INSERT statement is used to add data
# - A UPDATE statement is used to modify existing data
# - A UNION statement is used to join 2 tables for a response
# - A DELETE statement is used to remove data
# - A DROP statement is used to ruin someone's day......
# 
# ![south-park-its-gone.gif](../images/Generic/south-park-its-gone.gif)
# 
# <hr>

# ## How Do We Test for Injection?
# A SQL injection is when you can modify a query for a purpose it wasn’t intended for. Therefore, the test for an Injection vulnerability is to add something that will break a normal query. This could be a single quote \', Double quote \" or a semicolon early \;
# 
# > In general, all of your injections should end with ';--'. The semicolon instructs the server to run the command, and the -- comments out the rest of the line
# 
# <hr>
# 
# ## Types of SQL Injection 
# 
# ### In Band
# This is the easiest injection to work with. This is when the query can be extracted easily from the site (i.e. pulled directly from the URL) and the result is displayed to the screen.
# 
# ### Error-Based
# Next on the list is 'error based'. Maybe you don’t see the query result on the screen, but you can enumerate using the error codes in response. While this is harder than In-Band, it can be scripted to make the journey much easier.
# 
# ### Union-Based
# Source: https://tryhackme.com/room/sqlinjectionlm <br>
# When we want the site to run normally, but give us more data, a UNION based injection is the way to go.
# 
# Let's start with an example. Let’s say we have a shopping site where the item number is shown in the URL. I'll use Amazon as an example but I'm pretty sure this won’t work in the live site...
# 
# > https://amazon.com/shopping?product=1337
# 
# In this example URL, we can see the parameter "product" is passed through. If we were to take a guess, somewhere in the code of this site is a query 'select * from products where product = 1337'. First, we would perform our tests to confirm this. Once we know this is an injection location, we can try it out.
# 
# > https://amazon.com/shopping?product=1337 UNION SELECT 1
# 
# This query is used to determine the number of columns in the guessed 'products' table above. 1 is simply a placeholder for how many columns we have (as the first column). The chances are there is more than one column in the 'products' table, we would just keep adding more columns until we there were no more errors.
# 
# > https://amazon.com/shopping?product=1337 UNION SELECT 1,2,3,4,5,6
# 
# Etc, Etc, Etc. Once we have the correct number of columns, we won't get the error anymore and can proceed to add fun things. First, we need to make sure the original query fails so only our injection is shown (especially if the site only uses the first response). I've just set it to 0 here
# 
# > https://amazon.com/shopping?product=0 UNION SELECT 1,2,3,4,5,database()
# 
# With this injection, wherever the data from column 6 would be, we would instead have our Database schema type. You could also just add this for all the column placeholders.
# 
# ### Fun Unions
# 
# > 0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = \'sqli_one\'
# 
# This statement will give us all the table names in the DB (replace sqli_one with the schema type from above).
# 
# > 0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'
# 
# Similar to the previous, this instead gets all column names of a defined table.
# 
# >  0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users
# 
# If you're lucky enough to find passwords stored in the DB, this union will help you extract them. The concat function just adds strings together, and the SEPARATOR changes concat's delimiter, in this case making it a HTML break (new line)
# 
# <hr>
# 
# ### Binary/Boolean Injection
# 
# A Boolean injection case exists when we can modify the response, we receive, based on if an injected query succeeds or fails. It is called binary/boolean as we can only change the response in one way, a yes/no, true/false, etc etc. An example would be if we try to create a user, and we get back a 'user already exists'.
# 
# 
# Continuing down the username path. Without knowing any information about the database, we can now enumerate to determine this. How? By combining the 'like' comparator and iterating through all possible values, one at a time. The basic format is
# 
# > UNION select [1,2,3,n...] from [standard info] where [known info] and [unknown info] like 'x%'
# 
# - [1,2.3,n...], This is the same as the unions we have above, where we are just completing our select statement. Not sure why you can’t just use a * here...
# - [standard info], Standard SQL queries
# - [known info], pretty straight forward, something we already know
# - [unknown info], as above. More on these below

# ## General Process
# 
# So, we know what we need to run, but what info do we know and need? Below is the format to 'drill down' into databases. Remember to end the injections with ";--"
# 
# 1. The database name. This one is an exception to the above where we don’t know the database name but also don’t need any 'known info'. We also don’t need to. The database is our first step <br>
# UNION SELECT [1,2,3] where [database() like '%']
# 
# 2. Once we have a database name (or names), our next step is to iterate the tables. <br>
# UNION SELECT [1,2,3] FROM [information_schema.tables WHERE table_schema = '\<db name here>'] and [table_name like '%']
# 
# 3. After tables comes the columns <br>
# UNION SELECT [1,2,3] FROM [information_schema.COLUMNS WHERE TABLE_SCHEMA='\<db name here>' and TABLE_NAME='\<table name here>'] and [COLUMN_NAME like '%']
# 
# 4. Once we have the columns, the queries get easier again. We are still following the process now, but instead of enumerating the structure, we can now query data. <br>
# UNION SELECT [1,2,3] from [\<table name here>] where [\<column name here> like 'a%]
# 
# 5. With many fields, we will want to match these by rows as well. Knowing a user and password isn’t much help if you don’t know which one belongs to which. An example for a users table with the columns 'user' and 'password'<br>
# UNION SELECT [1,2,3] from [users] where [user] = 'admin' and password like '%'
# 
# <hr>
