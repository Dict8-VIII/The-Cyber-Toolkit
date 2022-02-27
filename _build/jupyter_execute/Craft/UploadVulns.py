#!/usr/bin/env python
# coding: utf-8

# # Upload Vulnerabilities
# 
# Upload vulnerabilities are when a site requests an upload from the user (for example a profile picture) and the file inputs are not restricted. Why would a profile picture upload allow a PHP file for example?
# 
# There are many checks than can be performed, some are better than others, and there are workarounds for many.
# 
# ### Check based on file extension
# The most trivial is simply to check the extension. A profile picture should be a PNG, JPG, JPEG, BMP etc.
# 
# How this is implimented can vary however. Listing what is allowed (like I have done above) is a whitelist (or allow list), while picking others to block, such as PHP, would be a blacklist/blocklist (or deny list). Whitelists are easier to implement but can be annoying for a legitimate user. Blacklists require you to list all extensions you want to block but you can easily miss some as listed.
# 
# 1. Try an alternate file extension. The obvious one to block on a PHP server is the .PHP extension. However PHP can exist in other extensions. PHP3,PHP4,PHP5,PHP7,PHP-S,PHAR,PHTML etc. <br>
# 
# 2. You may be thinking "OK, blocklists arent a good way to go, I'll just allow files containing my extensions". Sure, what if I presented a file "file.PNG.PHP". If youre just looking to allow extensions, would this pass your filter? It contains the allowed extension but is still a .PHP file. <br>
# 
# 3. "Fine! Easy fix, I'll only allow files that have a .PHP then nothing afterwards." What about a file name "file.PNG .PHP"? Does a space terminate your filter? <br>
# 
# 4. "HA! I've got you now! I'll just make a filter where the last 4 characters must be .PNG!". Ok, ignoring the fact that you can have extensions larger than 3 characters, filters based on positions can also be fooled sometimes. If you've already looked at LFI then you will know about the NULL Byte. With this we can create a file like "file.PNG%00.PHP". If your filter is terminated by the NULL byte, then this will pass but the file is STILL a .PHP.
# 
# If you're thinking this is getting a bit silly, I couldn't agree more. 
# 
# ![biggerGuns.gif](../images/biggerGuns.gif)
# 
# <hr>

# ### Magic Numbers
