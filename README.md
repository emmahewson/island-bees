Notes

Bug - attempted to move the js for the remove item from bag in to separate JS file - update worked ok but remove didn't. Put back in to HTML as a script tag.

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

With the help of the following post on the Code Institute Slack Channel
https://code-institute-room.slack.com/archives/C7HS3U3AP/p1605302104469800?thread_ts=1605222094.452700&cid=C7HS3U3AP
I discovered that rather than now returning a Boolean value from the new JS code it was returning a string of "true" or "false" - which meant that when checking if save_info: it was always returning True because it always had contents. I fixed the issue by changing it to:

# Checks if user wants to save info
if save_info == "true:
    # updates userProfile based on data

In addition I noticed on Slack that previous students had had issues with the code not working once deployed if the script link was in the footer, so I moved it to the head to avoid these issues coming up later on.


Bug - the shopping bag summary was showing in the toast after accounts functionality e.g. login, change password, confirm emails etc & for review & product add/edit/delete - bad user experience as it was irrelevant to the user action. I removed it by firstly adding an additional conditional statement to the message_success template to check whether the referring page url contained the word 'accounts' to stop the bag showing when any messages.success were called by the built-in allauth code. Then in addition, I added a session variable called show_bag_summary to true or false each time I called messages.success and an additional conditional value in the template tag to check this value:

{% if grand_total and request.session.show_bag_summary and "accounts" not in request.META.HTTP_REFERER %}
    

Bug - add product form - wanted to have different styling on the labels for the text & textarea labels compared to the checkbox labels. I couldn't find a way to add class attributes to the labels themselves within the forms.py logic so I separated the fields out to individual tags and styled them in this way. However I discovered that this had the unintended result of not showing any form error messages e.g. if the price had too many digits. I got around this by explicitly including the error messages below the labels as separate tags:
e.g.
{% for error in form.price.errors  %}
    <span class="text-ib-warning weight-semibold ib-lh-2">{{error}}</span>
{% endfor %}


Bug - during deployment my products page wouldn't load and returned a 400 error. I turned debug back on and discovered that it couldn't load the sort_box.js file and was throwing up a suspicious operation error and blocking the page. I fixed this error with the help of this page https://stackoverflow.com/questions/43529912/suspicious-operation-attempted-access-to-denied-while-loading-static-files by removing the leading '/' on the script tag in the template.


Bug - Whilst initially working correctly I found that my checkout began to create duplicates when placing an order - one in the view and another in the webhook. After extensive research and testing using print statements I discovered that the problem was at the point where the webhook searches for the order in the database and if it didn't find it, creates the order. The problem stemmed from the form fields which were not required and so could be empty - phone number and street address 2. I fixed the problem by removing these fields from the search parameters in the webhook query.




Mention
using widget-tweak to add style classes to the form inputs in the auth templates
The delivery charge calculations when no delivery is chargable


Linting Errors
- checkout/apps.py - checkout.signals is imported but unused - signals is being passed in and used elsewhere so can be disregarded
- checkout/webhooks.py - local variable e is assigned to but never used - have investigated this and it appears to be an industry standard way of assigning this particular error checking. I also passed this code through the CI Python Linter and it didn't raise an issue. https://pep8ci.herokuapp.com/
- remaining linting errors are in files that are automatically created by Django such as migration files & vscode/arctictern.py
