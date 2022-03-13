#!/usr/bin/env python
# coding: utf-8

# # SQL Injection
# 
# ## The Basics of SQL
# SQL, or "structured query language" is a scripting language used where quering a database.<br>
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
# ![south-park-its-gone.gif](../images/south-park-its-gone.gif)
# 
# ### How Do We Test for Injection?
# A SQL injection is when you can modify a query for a purpose it wasnt intended for. Therefore, the test for an Injection vulnerability is to add something that will break a normal query. This could be a single quote \', Double quote \" or a semicolon early \;
# 
# <hr>
# 
# ## Types of SQL Injection - In Band
# 
# This is the easiest injection to work with. This is when the query can be extracted easily from the site (i.e. pulled directly from the URL) and the result is displayed to the screen.
# 
# ### Error-Based
# Next on the list is 'error based'. Maybe you dont see the query result on the screen, but you can ennumerate using the error codes in response. While this is harder than In-Band, it can be scripted to make the journey much easier.
# 
# ### Union-Based
# Source: https://tryhackme.com/room/sqlinjectionlm <br>
# When we want the site to run normally, but give us more data, a UNION based injection is the way to go.
# 
# Let's start with an example. Lets say we have a shopping site where the item number is shown in the URL. I'll use Amazon as an example but I'm pretty sure this wont work in the live site.....
# 
# > https://amazon.com/shopping?product=1337
# 
# In this example URL, we can see the parameter "product" is passed through. If we were to take a guess, somewhere in the code of this site is a query 'select * from products where product = 1337'. First we would peform our tests to confirm this. Once we know this is an injection location, we can try it out.
# 
# > https://amazon.com/shopping?product=1337 UNION SELECT 1
# 
# The chances are there is more than one column in the 'products' table, we would just keep adding more columns until we got no more errors
# 
# > https://amazon.com/shopping?product=1337 UNION SELECT 1,2,3,4,5,6
# 
# Etc, Etc, Etc. Once we have the correct number of columns, we dont get errors any more and can proceed to add fun things. First we need to make sure the original query fails so only our injection is shown (especially if the site only uses the first response). I've just set it to 0 here
# 
# > https://amazon.com/shopping?product=0 UNION SELECT 1,2,3,4,5,database()
# 
# With this injection, wherever the data from column 6 would be, we would instead have our Database schema type.
# 
# 
# #### Fun Unions
# 
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

# In[ ]:




