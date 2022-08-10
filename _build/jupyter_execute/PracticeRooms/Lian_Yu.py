#!/usr/bin/env python
# coding: utf-8

# # Lian_Yu
# 
# This one is an archer themed room. Its still in the 'easy' category but has quite a bit going on. Not a fan of the show but quite enjoyed this room.
# 
# 
# Tried
# - anonymous
# - Lian_Yu
# - LianYu
# - vigilante
# ![Lian_Yu_FTPTesting.png](attachment:0e80cb24-205b-45e8-9f3b-5b44bda5f321.png)
# 
# 

# ## First Steps
# 
# As normal. Lets start with an Nmap scan.<br>
# ![Lian_Yu_nmapResults.png](../../images/PracticeRooms/Lian_Yu_nmapResults.png)<br>
# 
# So we've got:
# - 21 : FTP
# - 22 : SSH
# - 80 : HTTP
# - 111 : 
# 
# The theme tends to be starting with the web site, bring it up.<br>
# ![Lian_Yu_DefaultPage.png](../../images/PracticeRooms/Lian_Yu_DefaultPage.png)<br>
# 
# This looks to be a bit of flavour text and background. It makes the room a bit more interesting but not so helpful for breaking and entering. At this stage we can spin up GoBuster. I also spin up Nikto but it's more a 'cover all bases' step.<br>
# ![Lian_Yu_GoBuster.png](../../images/PracticeRooms/Lian_Yu_GoBuster.png)<br>
# 
# Looks like we've found a /island page.<br>
# ![Lian_Yu_FoundPage.png](../../images/PracticeRooms/Lian_Yu_FoundPage.png)<br>
# 
# On first glance it looks useless as its missing the code word (but does have a rather bold name). Quickly checking the page source (or just highlighting the whole page) gives what we're after though.<br>
# ![Lian_Yu_HiddenTxt.png](../../images/PracticeRooms/Lian_Yu_HiddenTxt.png)<br>
# 
# That looks like the end of our /island journey. Time to looks for more sub directories<br>
# ![Lian_Yu_SecondGoBuster.png](../../images/PracticeRooms/Lian_Yu_SecondGoBuster.png)<br>
# 
# After a bit of time, look what we get. A new subdirectory and the answer to our first actual question.<br>
# ![Lian_Yu_2100Source.png](../../images/PracticeRooms/Lian_Yu_2100Source.png)

# In[ ]:




