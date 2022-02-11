#!/usr/bin/env python
# coding: utf-8

# # John The Ripper
# 
# While the namesake is famous for terrorising London, John is just as well known in the Cyber Security space. It is an amazingly versatile tool used for cracking hashes.
# 
# The typical format is:
# > john --wordlist=\[wordlist] \[file]
# 
# Unfortunately, yes, you have to pass a file containing your hash(s), one per line if you have multiple.
# How the file is formatted depends on what you want to crack
