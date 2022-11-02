#!/usr/bin/env python
# coding: utf-8

# # Passwords
# 
# We all know what passwords are, but the art of creating strong passwords and cracking them is what a large part of Cyber Security is about. Without strong passwords, the CIA triangle breaks down, OWASP issues are bypassed and encryption is rendered largely redundant. Social engineering is largely about breaking passwords, OSINT assists in breaking them and forced password changes are to mitigate brute force attacks. MFA can be deployed to mitigate some of these issues, but we cant MFA everything. Imagine if you had to authorise MFA every time someone tried to log into your site (WebApp -> SQL). 
# <br>
# This page looks at both sides of the 'password' landscape for both Blue teams trying to create strong passwords, and the Red team trying to break them.
# 
# <hr>

# ## Blue - Creating Strong Passwords
# If it's no immediately obvious, passwords are kind of important for security and maintaining any business. A strong password policy and training to prevent social engineering is a great state to be in. Theres more topics, but it's all about making it harder for someone to break in. The harder it is to attack you or your business, the more likely the attackers are to move on to the next target. So, how do we do this. Lets start with understanding what a strong password really is... Heres a great example from [XKCD](https://xkcd.com/936/)<br>
# ![XKCDPasswordStrength](https://imgs.xkcd.com/comics/password_strength.png)<br>
# 
# So, lets break this down with some simple comments, first about making a password stronger
# - The length of a password is correlated to its strength, the longer the better
# - Special characters are a 'multiplier' on this by increasing the number of possibilities per character
# - Humans are bad at remembering passwords
# 
# Theres also some caveats to add to this, which I'd like to highlight
# - All lower case characters are still a small set
# - Using only dictionary words is still a bad idea, theres and estimate that there is only about 65000 likely words. Thats how many guesses if you do this. The same applies to personal details such as name, dates, hobbies etc.
# - If it's too hard to remember a password, its going to be written down
#    - This one has flip/flopped being a good or bad thing a few times over the past few decades. It's one of my favourite cyber security topics. Right now I'll keep it as a negative
# - Adding special character / case requirements without understanding why they are needed is still bad. How many passwords do you think
#    - Start with an upper case letter
#    - Are a dictionary word or similar
#    - End with a number or special character found on the 1,2 or 3 keys (!, @, #)
#    - Are a dictionary word, with an s replaced with $ or a h with a #, I->! etc...
# - It may sound like youre increasing the security, which you technically are, but it's also a false sense of security
# - Reusing passwords is really dangerous. You could have the best password ever, but if you use it on a site/service that gets leaked, it can also be reused by an attacker. Just don't...
# 
# Theres a lot huh... So what's an IT expert to do? A key point to remember is that a password should be hard to guess but easy to remember. Thats all. Everything else is just to support that. If what you're doing goes against this then its counter productive.

# In[ ]:




