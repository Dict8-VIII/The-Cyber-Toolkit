#!/usr/bin/env python
# coding: utf-8

# # XSS
# XSS, or Cross Site Scripting, is a method for exploiting a website by exploiting user controlable fields.
# 
# There are 3 kinds of XSS
# - Which I
# - Cant Remeber
# - Right now
# 
# ### Type 1 - The one where you install javascript on a form
# 
# Example Payload
# > \<script>fetch(/settings?new_password="That persons new password");\</script>

# ### Modifying a DIV tag via ID
# In HTML, elements can be referenced by their ID (normally a DIV tag). To modify one when you can inject scripts, insert the below between \<script> tags
# >document.getElementById("The ID goes here").innerHTML="What I want the cell to be";

# In[ ]:




