# Island Bees - E-Commerce Site

![Mock-up]()

#### **By Emma Hewson**
[Click here to view the live web application](https://island-bees-5e7b15194c83.herokuapp.com/)

This is the documentation for my e-commerce web application: Island Bees. It has been built using Django, Python, JavaScript, CSS3 & HTML5 for educational purposes as part of Code Institute’s Diploma in Web Application Development Course.

DETAILS OF SITE HERE???

- - -
## Table of Contents

1. [User Experience](#)
    * [Project Aims](#)
    * [User Stories](#)
    * [Design](#)
        * [Wireframes](#)
        * [Colour](#)
        * [Typography](#)
        * [Images & Graphics](#)
        * [Database Schema](#)
        * [Flow Diagram](#)
        * [Design Changes](#)
2. [Features](#)
    * [Site Features](#)
    * [Future Features](#)
3. [Technologies Used](#)
    * [Languages Used](#)
    * [Python Modules, Packages & Frameworks Used](#)
    * [Programs and Tools Used](#)
4. [Testing](#)
    * [Bugs](#)
        * [Fixed Bugs](#)
        * [Remaining Bugs](#)
5. [Deployment](#deployment)
  * [Forking the GitHub Repository]()
  * [Making a Local Clone]()
  * [Deploying with Heroku]()
6. [Credits]()
  * [Online resources]()
  * [Code]()
  * [Media]()
  * [Acknowledgments]()


- - -

## User Experience

### Project Aims

- - -

###  User Stories


- - -

### Design

#### Wireframes

- - -

#### Colour

- - -

#### Typography

- - -

#### Images & Graphics

- - -

#### Database Schema

- - -

#### Flow Diagram

- - -

#### Design Changes

- - -
[Go to Top](#island-bees---e-commerce-site)
- - -

## Features

### Site Features

Mention
using widget-tweak to add style classes to the form inputs in the auth templates
The delivery charge calculations when no delivery is chargeable
Additional titles and description meta tags on each page
Reviews - superuser cannot edit, only delete
Reviews - approval
Product rating only takes in to account approved reviews & is updated upon add, edit, delete & toggle

- - -

### Future Features

In Original Design
- Blog

Admin notification when a review / message is submitted 
A more comprehensive system for messages with admins able to review chain of communication and reply on the site
A booking system for courses with a calendar and tracking of availability on courses
A stock control system for products

- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## Technologies Used

### Languages Used

- - -

### Python Modules, Packages & Frameworks Used

- - -

### Programs and Tools Used

- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## Testing

Linting Errors
- checkout/apps.py - checkout.signals is imported but unused - signals is being passed in and used elsewhere so can be disregarded
- checkout/webhooks.py - local variable e is assigned to but never used - have investigated this and it appears to be an industry standard way of assigning this particular error checking. I also passed this code through the CI Python Linter and it didn't raise an issue. https://pep8ci.herokuapp.com/
- remaining linting errors are in files that are automatically created by Django such as migration files & vscode/arctictern.py

### Bugs

Bug - attempted to move the js for the remove item from bag in to separate JS file - update worked ok but remove didn't. Put back in to HTML as a script tag.

Bug - issues with the checkout delivery & total calculations - couldn't add a float & a decimal type numbers. 
Fix - Had to convert the order_total and total_delivery_chargeable to float values with checks to make sure they had a value in the first place. This accounted for the various different scenarios.
    1. Under delivery threshold & delivery chargeable on all products
    2. Under delivery threshold & delivery changeable on some but not all products
    3. Over delivery threshold

Bug - the save info checkbox on the checkout was saving the form information regardless of whether the checkbox was selected or not. After a lot of testing and research I found out the problem was stemming from 2 places:
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


Bug - the shopping bag summary was showing in the toast after accounts functionality e.g. login, change password, confirm emails etc & for review & product add/edit/delete - bad user experience as it was irrelevant to the user action. I removed it by firstly adding an additional conditional statement to the message_success template to check whether the referring page url contained the word 'accounts' to stop the bag showing when any messages.success were called by the built-in allauth code. Then in addition, I added a session variable called show_bag_summary to true or false each time I called messages.success and an additional conditional value in the template tag to check this value:

{% if grand_total and request.session.show_bag_summary and "accounts" not in request.META.HTTP_REFERRER %}
    

Bug - add product form - wanted to have different styling on the labels for the text & textarea labels compared to the checkbox labels. I couldn't find a way to add class attributes to the labels themselves within the forms.py logic so I separated the fields out to individual tags and styled them in this way. However I discovered that this had the unintended result of not showing any form error messages e.g. if the price had too many digits. I got around this by explicitly including the error messages below the labels as separate tags:
e.g.
{% for error in form.price.errors  %}
    <span class="text-ib-warning weight-semibold ib-lh-2">{{error}}</span>
{% endfor %}


Bug - during deployment my products page wouldn't load and returned a 400 error. I turned debug back on and discovered that it couldn't load the sort_box.js file and was throwing up a suspicious operation error and blocking the page. I fixed this error with the help of this page https://stackoverflow.com/questions/43529912/suspicious-operation-attempted-access-to-denied-while-loading-static-files by removing the leading '/' on the script tag in the template.


Bug - Whilst initially working correctly I found that my checkout began to create duplicates when placing an order - one in the view and another in the webhook. After extensive research and testing using print statements I discovered that the problem was at the point where the webhook searches for the order in the database and if it didn't find it, creates the order. The problem stemmed from the form fields which were not required and so could be empty - phone number and street address 2. I fixed the problem by removing these fields from the search parameters in the webhook query.


Bug - When attempting to delete a product that is linked to a previous order as a line item in the OrderLineItem model it throws an error because, due to the CASCADE setting on the field, by deleting the product you are also then deleting all references to it. This posed a problem because I wanted to give superusers the ability to delete a product to remove it from sale, but keeping all old order information is also very important. I solved this problem with an idea from this CI Slack channel [post](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1598004199059700?thread_ts=1597961336.047800&cid=C7HS3U3AP) by stopping store owners deleting products using model.PROTECT but allowing them to remove them from sale with a 'discontinued' Boolean field.

This meant additional changes had to be made to the site to ensure smooth running and good user experience:
- added a conditional check to the delete_product view to see if the product appears on any OrderLineItems and if so rather than deleting it, to mark it as 'discontinued'
- Dynamically changing the text in the delete product modal depending on whether the product has associated OrderLineItems and if so removing the ability to delete it and offering the admin the chance to 'discontinue' it instead.
- Only displaying cards products that are not 'discontinued' on the products & home pages
- Adding a check on the product_detail view to redirect users who link to it directly using the url or back button to the 'products' page
- Adding an additional field to the add/edit product form to mark a product as 'discontinued'
- Removing the edit/delete buttons from the product cards to improve user experience and keep the site logic as simple and bug free as possible
- When a form is submitted with the 'discontinue' input checked, if that product is in the shopping bag, remove it.
- Added a conditional check on the add_to_bag view to only add if the product was not discontinued.

- Broken image links showing when image is missing, rather than the 'no-image' backup. This meant that if there was an error getting the product image the product cards were hard to click on to link to the product detail page as the image is the link element. In order to fix this I added an 'onerror' to the image tags to show the no-image if there was an error displaying the image.
`onerror="this.onerror=null;this.src='{{ MEDIA_URL }}no_image.jpg'"`

#### Fixed Bugs

- - -

#### Remaining Bugs


- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## Deployment

### Forking the GitHub Repository

- - -

#### Making a Local Clone

- - -

#### Deploying with Heroku

- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## Credits

### Online resources

CHATGPT to produce the text for the products & reviews. It was not used for any code production or problem solving, just as a quick way to produce text content to populate the site.

- - -

### Code

- - -

### Media

- - -

### Acknowledgments

- - -

[Go to Top](#island-bees---e-commerce-site)

