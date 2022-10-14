#!/usr/bin/env python
# coding: utf-8

# # Attacks
# 
# <hr>

# ## Types of Attacks - Technical
# 
# There are many types of attacks that can be employed by a hacker. While technologies come and go, the fundamentals don’t change. Many of these have been 'resolved' in certain circumstances but understanding of these attacks can still form a basis for a cyber security mindset. These are also a basic overview of the attacks, and more detail can be found in other sections.
# 
# There aren't really any clearly defined categories for attacks. Some people have tried, but I feel many fall in a larger scope. The attacks below are listed as independent but in the real world there will be many types deployed together to be successful.
# 
# ### DoS (and DDoS)
# A DoS, or Denial of Service attack is a very simple attack that can also be very powerful. While a DoS attack is technically any attack with the purpose of making a service unavailable, the most common method of this is by simply overloading the service with 'fake' data. Every service has a limit to how much data it can handle, and if we can overload this, then the service becomes unavailable to legitimate users. For a web site, this could prevent a legitimate user from accessing the site. <br>
# 
# As you could imagine, web servers are designed to handle a lot of traffic. A site like google could be handling tens of thousands of requests every second during normal operation, you're not going to be able to take it down from you home computer & internet connection. This is where a Distributed Denial of Service comes in (DDoS). Instead of a single device trying to overload the site, you have multiple devices in multiple locations pushing data to the same server. While each machine itself might not be able to take the service down, with a large enough collection of devices, a lot more damage can be done. 
# 
# > You're probably still not going to be able to take down google... sorry
# 
# ### Man In The Middle
# 
# A "Man in the Middle" attack is when data is intercepted in transit and relayed on. A good analogy would be using the mail system to send cash (there’s a reason they tell you not to do this). You might want to send a birthday letter to a niece/nephew on the other side of the country and throw in some birthday money. You drop it at the post office with a 50 inside but someone heard there was cash inside. After you send the letter, the postman opens your letter, takes out the 50 and replaces it with $5, then sends the letter on its way. The letter still reaches the destination but has been modified. Unless someone verifies the amount, no-one is going to know 90% of the value was lost. <br>
# 
# Now, with data being what it is, you don’t always need to remove data from the package. Simply knowing what data was in the package is enough in some circumstances. If you brought something online with a Credit Card and passed this data through, the attacker doesn’t need to modify the letter, they can just grab the info and pass this on.
# 
# 
# <hr>

# ## Types of Attacks - Social Engineering
# 
# ### Phishing & Spearphising
# 
# <hr>
