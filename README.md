Notes

Bug - attempted to move the js for the remove item from bag in to separate JS file - update worked ok but remove didn't. Put back in to HTML as a script tag.

Bug - bag appears in toast after review updated or added - not sorted

Bug - issues with the checkout delivery & total calculations - couldn't add a float & a decimal type numbers. 
Fix - Had to convert the order_total and total_delivery_chargable to float values with checks to make sure they had a value in the first place. This accounted for the various different scenarios.
    1. Under delivery threshold & delivery chargable on all products
    2. Under delivery threshold & delivery chargable on some but not all products
    3. Over delivery threshold

Bug - the save info checkbox on the checkout was saving the form information regardless of whether the checkbox was selected or not. After alot of testing and reserach I found out the problem was stemming from 2 places:
1. In stripe_elements.js there was an issue with the JQuery assignment of the Boolean value and the value being sent to the post_data was always true no matter whether the checkbox was selected or not. I couldn't pin point exactly why it was behaving like this but I was able to solve it by assigning the value using vanilla JavaScript.

Old Code - didn't work
var saveInfo = Boolean($('#id-save-info').attr('checked'));

New code - assigned true/false correctly
var saveInfo = document.getElementById('id-save-info').checked


2. Even after changing the above code I found that the profile details were still being saved when the box was unchecked. I discovered that the problem was related to the following code in webhook_handler.py

# Get value of 'save_info' box from payment intent
save_info = intent.metadata.save_info

# Checks if user wants to save info
if save_info:
    # updates userProfile based on data

With the help of the following posts on Slack 
https://code-institute-room.slack.com/archives/C7HS3U3AP/p1605302104469800?thread_ts=1605222094.452700&cid=C7HS3U3AP
I discovered that rather than now returning a Boolean value from the new JS code it was returning a string of "true" or "false" - which meant that when checking if save_info: it was always returning True because it always had contents. I fixed the issue by changing it to:

# Checks if user wants to save info
if save_info == "true:
    # updates userProfile based on data

In addition I noticed on Slack that previous students had had issues with the code not working once deployed if the script link was in the footer, so I moved it to the head to avoid these issues coming up later on.




Mention
using widget-tweak to add style classes to the form inputs in the auth templates
The delivery charge calculations when no delivery is chargable
