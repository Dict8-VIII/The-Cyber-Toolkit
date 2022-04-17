#!/usr/bin/env python
# coding: utf-8

# # The Basics
# 
# So, you've decided to start your path in Cyber Security, or more likely, hacking sounds fun. Great! It can be! But there is more to it then getting a hoodie and balaclava and hunching over a laptop (in the dark obviously). Hacking is a career path, regardless of what popular media tells you about hackers.
# 
# ![hackerinhoodie.jpg](../images/hackerinhoodie.jpg)
# 

# ## Why Is Cyber Security Important?
# 
# <hr>

# ### Types of Hackers (By Motive)
# So that leads us to the first note, what kind of hackers are there? Hackers can be divided by 2 metrics, their knowledge/threat level and their motives. The most clearly defined is the motives;
# 
# #### White Hat
# These are the professionals who operate within the scope of law and regulation. They work for a business (or are contracted to one) to engage in a range of cyber security tasks. They have permission from an entity to perform task on a system that they own, within a 'scope' of engagement. They have well defined documentation of what they are permitted to do on a system and follow this to the letter. 
# 
# An example would be a Pen Test (Penetration Test) where an airport contracts a security company to test their publicly exposed network to attempt to gain access. They are only permitted to operate within a defined target range and DDoS attacks are not permitted.
# 
# Their motive is purely professional and within agreed terms. Any findings are reported professionally and remediation is advised.
# 
# 
# #### Black Hat
# The opposite of a White Hat is a Black Hat. They operation with no permission and their motivation is purely personal. This could range from a child sitting at home trying to guess Mum's Facebook password, to a fully underground network of hackers who operation on a global scale. Their motivation could be financial, political, anarchist or simply because they want to know if they can. The KEY definition of a Black Hat is that they attack a system without permission.
# 
# 
# #### Grey Hat
# There is a 3rd type, however personally I think it should be considered a Black Hat. A Grey hat is a Black Hat who is hacking with a positive motive but no permission. An example would be someone who hacks a website without permission, but shares the method of entry with the owner of the site, with the hope they will fix it (or they ask for \$\$\$ before they will share the method). The "Grey Hat" title should be handled with caution, I Am Not A Lawyer, but if you are caught your motivation is irrelevant and you will likely be considered a "Black Hat".
# 
# Some may put 'hacktivists' in this category. A 'hacktivist' is an activist using hacking to threaten a business. This could be from a DDoS using LOIC to defacing a website. None of this is legal in the physical world, it's not online either.
# <hr>
# 
# ### Types of Hackers (by Knowledge)
# The second metric is the knowledge of the hacker. While not clearly defined, there are levels of threat and considerations must be made for all to some extent. The below is a less -> more threat level as I see it.
# 
# > Note: some sites define 7 levels, example: https://blog.knowbe4.com/the-7-levels-of-hackers. I feel even this comes short as a "hacktivists" could also a "Script Kiddie" or a "Skilled Hacking Group".
# 
# #### "Script Kiddie"
# Even the name is an insult to many hackers. A 'script kiddie' is stereotyped as the 10yr old sitting on the family computer trying to 'hack facebook'. Another example would be a 'hacktavist' who learned hacking from a twitter post (did someone say LOIC?). Its not a sophisticated attack, but one of the things about some attacks is you don't need to be. Enough people doing something simple at the same time can still be a massive headache (see DDoS below).
# 
# 
# #### Hacking Group
# Probably the most vague group in this list, a skilled hacking group could be many things. I would define it as "an individual or groups of hackers who have enough knowledge to be dangerous". This could range from a well co-ordinated group of script kiddies to "Anonymous". These are the people who are hacking as a semi-serious hobby and don't have the finances to mount full attacks. 
# 
# 
# #### Professional Hackers
# These are the people who are skilled enough to do this as a job (legitimate or not). They are skilled with any number of attacks and are likely aware of any new or emerging exploit. They have the time and experience to be a real threat to a majority of business.
# 
# 
# #### APTs & NSAs
# I've thrown these together, as most APTs are NSAs. An APT is an "Advanced Persistent Threat". These are the people who are incredibly skilled and have all the time in the world to find a way in. The majority of these are NSAs, or "Nation State Actors", the government branches who fight wars behind a computer. If you are targeted by one of these you have 2 options.
# 
# 1. Disconnect yourself from the internet entirely, shut down all your devices and leave them in a tin foil safe in the bottom of the ocean.
# 
# 2. Accept that sooner or later, the chances are they will find a way in. No computer is perfectly secure and because of things like Zero Days, you don't even know what you need to protect against. We all thought Windows 7 was secure when it came out and even during support. That was destroyed overnight by "Eternal Blue", CVE-2017-0144. If you think the NSA didn't have that one for years before we knew about it, you havent been paying attention...
# 
# You have one lifeline though. APTs don't target randomly, just remember that nothing on the internet is ever truly secure.
# 
# #### An Automated Tool
# This is one I came across while forming my groups and I can appreciate the addition. An automated tool is 'theoretical' software that contains the skill of an APT. The reason this is more of a threat is that a well scripted tool could be run by any of the previous groups. Imagine being able to take a current MetaSploit version back to 2016 before Microsoft had been disclosed "Eternal Blue". Suddenly you have a tool that gets you Admin access on (practically) any networked Windows 7 box. Ouch.
# 
# <hr>

# ### Types of Attacks
# 
# There are many types of attacks that can be employed by a hacker. While technologies come and go, the fundamentals dont change. Many of these have been 'resolved' in certain circumstances, but understanding of these attacks can still form a basis for a cyber security mindset. These are also a basic overview of the attacks, and more detail can be found in other sections.
# 
# There aren't really any clearly defined categories for attacks. Some people have tried, but I feel many fall down in a larger scope. The attacks below are listed as independant but in the real world there will be many types deployed to be successful.
# 
# #### DoS (and DDoS)
# A DoS, or Denial of Service attack is a very simple attack that can also be very powerful. While a DoS attack is technically any attack with the purpose of making a service unavailable, the most common method of this is by simply overloading the service with 'fake' data. Every service has a limit to how much data it can handle, and if we can overload this, then the service becomes unavailable to legitimate users. For a web site, this could prevent a legitimate user from accessing the site. <br>
# 
# As you could imagine, web servers are designed to handle a lot of traffic. A site like google could be handling tens of thousands of requests every second during normal operation, you're not going to be able to take it down from you home computer & internet connection. This is where a Distributed Denial of Service comes in. Instead of a single device trying to overload the site, you have multiple devices in multiple locations pushing data to the same server. While each machine itself might not be able to take the service down, with a large enough colleciton of devices, a lot more damage can be done. 
# 
# > You're probably still not going to be able to take down google... sorry
# 
# #### Man In The Middle
# 
# A "Man in the Middle" attack is when data is intercepted in transit and relayed on. A good analogy would be using the mail system to send cash (theres a reason they tell you not to do this). You might want to send a birthday letter to a niece/nephew on the other side of the country and throw in some birthday money. You drop it at the post office with $50 inside but someone heard there was cash inside. After you send the letter, the postman opens your letter, takes out the $50 and replaces it with $5, then sends the letter on its way. The letter still reaches the destination, but has been modifed. Unless someone verifies the amount, no-one is going to know 90% of the value was lost. <br>
# 
# Now, with data being what it is, you dont always need to remove data from the package. Simply knowing what data was in the package is enough in some circumstances. If you brought something online with a Credit Card and passed this data through, the attacker doesnt need to modify the letter, they can just grab the info and pass this on.
# 
# #### Social Engineering
# 
# #### Phishing & Spearphising
# 
# <hr>

# In[ ]:




