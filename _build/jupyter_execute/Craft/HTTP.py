#!/usr/bin/env python
# coding: utf-8

# # HTTP
# 
# HTTP, or HyperText Transfer Protocol is the most common web protocol. It is unencrypted and stateless, meaning each request is handled independently of each other. Request a page and an image on the page are 2 separate requests. For sites that require a login to access a page, this is managed by cookies.
# 
# While web browsers are commonly used for retrieving pages, this isn’t a requirement. A telnet client could also request these (or curl). HTTP servers are normally hosted on port 80, but don’t have to be.
# 
# ## HTTP Methods (Verb)
# An HTTP method is the action type requested on communication to a server. These are called methods or verbs. The most common are:
# 
# GET
# POST
# PUT
# DELETE
# 
# ## Request process
# The easiest verb to show is a get request. To do this over telnet
# 
# >Telnet [serverIP] 80
# >Get / HTTP/1.1
# >host: telnet
# > press enter a couple of times
# 
# In the first line, we are simply creating a TCP handshake to the server on port 80.<br>
# In the second line, we are getting the "/" file, normally index.html, and providing a protocol to use<br>
# In the last line, we need to tell the server our host, this could really be anything but must be provided.<br>
# 
# If this all goes well, you will receive the page code to your terminal. Simple.
# 
# <hr>
# 
