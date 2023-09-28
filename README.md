# Island Bees - E-Commerce Site

![Mock-up](media/docs/mp4_mockup.jpg)

#### **By Emma Hewson**
[Click here to view the live web application](https://island-bees-5e7b15194c83.herokuapp.com/)

This is the documentation for my e-commerce web application: Island Bees. It has been built using Django, Python, JavaScript, CSS3 & HTML5 for educational purposes as part of Code Institute’s Diploma in Web Application Development Course.



- - -
## Table of Contents

- [User Experience](#planning-design--user-experience)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Features](#features)
    - [Site Features](#)
    - [Future Features](#)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frontend Frameworks / Libraries](#frontend-frameworks--libraries)
    - [Backend Modules / Packages & Frameworks](#backend-modules--packages--frameworks)
    - [Other Tools](#other-tools)
    - [External Sites / Resources / Software](#external-sites--resources--software)
- [Testing & Bugs](#testing--bugs)
- [Deployment](#deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [Deploying Your App](#deploying-your-app)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Acknowledgments](#acknowledgments)




- - -

## Planning, Design & User Experience

I approached the planning & design of this project using the principles of User Experience and the 5 stages of strategy, scope, structure, skeleton & surface. This is a large, complex project and I wanted to make sure it remained on course, on time and the best it could be whilst meeting all its initial aims. 

### Strategy

#### Project Aims

The initial aims of the project were to create an e-commerce website for an imaginary company called Island Bees, a North Wales based apiary and merchants, who stock a variety of good relating to bee-keeping as well as running courses for bee keepers. The website's main purpose was to allow customers to browse the company's products and make purchases, tell the customers about Island Bees and information about their online shop and allow user interactions through reviews and messages.

#### Research

I did some research in to other similar websites as well as in the wider e-commerce world. I wanted to make sure that Island Bee's website conformed to the expectations that users have for an e-commerce site, this is extra important because it involves financial transactions and I wanted to create a feel of trustworthiness and professionalism in order to encourage users to make purchases. I also gathered design ideas for the look of this site including colour, layout and typography.

Websites visited for research:
- [BS Honey Bees](https://www.bshoneybees.co.uk/)
- [Anglesey Bees](https://www.angleseybees.co.uk/)
- [Local Honey Man](https://localhoneyman.co.uk/)
- [Bee Equipment](https://bee-equipment.co.uk/)


####  User Stories

Based on my research and the project aims I created a set of user stories that would inform all the choices made in designing and developing the site.

1. As a general user:
  - 1.1: I want to understand the purpose of the site immediately upon entering
  - 1.2: I want to be able to find what I need immediately and for the navigation to be easy to follow & intuitive
  - 1.3: I want to be able to use all features on the site on any device and for it to be fully responsive
  - 1.4: I want to be able to find answers to common questions
  - 1.5: I want to be able to contact the company with any questions or queries
  - 1.6: I want to be able to find the company on social media to find out more
  - 1.6: I want to be able to return to the main site without having to use the browser buttons if I end up on a non-existent page
  - 1.7: I want to get feedback when interacting with the site to know if my actions have been successful

2. As a shopper:
  - 2.1: I want to be able to browse products easily, with options to filter & search to find what I need
  - 2.2: I want to be able to find out information about products
  - 2.3: I want to see ratings & reviews of a product to know more about the quality and whether it's right for me
  - 2.4: I want to be able to shop for multiple items at once, from across the site
  - 2.5: I want to be able to add multiples of a single product to my bag at once
  - 2.6: I want to be able to edit my shopping bag if I change my mind
  - 2.7: I want to know what I will be charged for delivery
  - 2.8: I want my payment and order to be fully secure and trustworthy
  - 2.9: I want to be able to set up an account to save my order history

3. As a user with an account:
  - 3.1: I want my account to be secure & easy to set up
  - 3.2: I want to see my order history
  - 3.3: I want to be able to update & save my personal information
  - 3.4: I want to leave reviews of products I have purchased for the benefit of other customers
  - 3.5: I want to be able to edit my reviews
  - 3.6: I don't want admins or other customers to be able to change my reviews

4. As an admin of the site:
  - 4.1: I want to be able to add & edit products
  - 4.2: I want to be able to remove products from sale
  - 4.3: I want to view & filter customer messages and manage whether they need further action
  - 4.4: I want to approve customer reviews before they go live & delete any with inappropriate content only
  - 4.5: I want to be able to update the site FAQs
  - 4.6: I want all the admin controls to be quick and easy to find and use

- - -

### Scope

I then created a list of all the features I would like to add to the site in order to meet all these user stories, as well as some extras that I'd like to include should time allow. I rated these in terms of difficulty and importance and this would help inform the decisions throughout the next stages of planning.

| Feature                                                                 | Difficulty | Importance |
|-------------------------------------------------------------------------|------------|------------|
| Responsive Design                                                       | 1          | 5          |
| Navigation - all page links                                             | 1          | 5          |
| Navigation - search facility                                            | 3          | 3          |
| Navigation - Shopping bag & current total                               | 3          | 4          |
| Footer - company info                                                   | 1          | 3          |
| Footer - social links                                                   | 1          | 3          |
| Home Page - branding & explanatory text                                 | 1          | 4          |
| Home Page - Featured Products                                           | 2          | 2          |
| Products - Product cards with summary info                              | 2          | 5          |
| Products - Sorting/searching/filtering                                  | 5          | 4          |
| Products - Detail Page with more info                                   | 2          | 5          |
| Products - Detail Page add to bag & quantity select                     | 4          | 5          |
| Products - CRUD functionality for admins                                | 3          | 5          |
| User Reviews of products                                                | 3          | 3          |
| User Reviews - update product average ratings                           | 5          | 3          |
| User Reviews - CRUD functionality (user only)                           | 3          | 3          |
| User Reviews - Admin approval system                                    | 4          | 2          |
| Bag - Users can store items in a bag for purchase                       | 4          | 5          |
| Checkout - Page with bag summary and delivery info                      | 4          | 5          |
| Checkout - Secure payment system                                        | 5          | 5          |
| Checkout - Page to show order summary on successful checkout            | 3          | 3          |
| User accounts - all standard login/out/register functionality           | 4          | 5          |
| User accounts - secure & reliable                                       | 4          | 5          |
| Profile - User profile page showing order history & reviews             | 3          | 4          |
| Profile - Page to show historical order information                     | 2          | 3          |
| Profile - Users can save & update their personal info for future orders | 4          | 4          |
| Frequently Asked Questions Page - company info                          | 1          | 4          |
| FAQs - CRUD functionality for admins                                    | 3          | 2          |
| Contact Us Page                                                         | 1          | 4          |
| Contact Us - Creates message in DB                                      | 3          | 2          |
| Contact Us - Admins can toggle status open/closed                       | 4          | 2          |
| Blog - Company insights & stories                                       | 3          | 1          |
| Site Management - useful links to admin jobs                            | 2          | 4          |
| Site Management - Customer Messages                                     | 3          | 2          |
| Site Management - Reviews for approval                                  | 3          | 2          |


---

### Structure

#### Flow Diagram

I created a flow diagram using [Lucidchart](https://www.lucidchart.com/pages/) to map out the structure of the site. This was an important step in the user experience design process, working out the structure and skeleton of the site, to provide the best user experience whilst keeping the user stories at the heart of the decision-making process. It allowed me to think through the paths of users through the site and what would need to link to where based on the different user stories and. It would also allowe me to make sure the site functioned as expected and everything was easy to find. It was also a vital tool to manage the scope of the project during the design and development stages, a blueprint to keep everything on track.

![Website Flow Diagram](media/docs/design_flow.png)


- - -

### Skeleton

#### Database Schema

An important stage in the planning was building a database schema, planning my data clearly, from the beginning, to make the development process as easy as possible. This database schema was informed by my work in the previous planes, the user stories, my scope chart and my flow diagram. I used [DrawSQL](https://drawsql.app/) to create a visual representation of the database, which I used throughout the development process to keep track of what my database looked like, updating it and amending it as the project grew and adapted as I learned. The original schema I created also included a blog, which I ended up rejecting from the final site due to time constraints as I wanted to focus my efforts on doing the project well rather than making it bigger and bigger. I have left it in the schema to demonstrate the work I did towards this and how it would connect to the rest of the database should I add it in in the future.

![Island Bees Database Schema](media/docs/design_schema.png)

Whilst traditionally wireframes are included in the Skeleton section I have included mine in the Surface section below. I have developed a way of working where I flesh out the full design of the site in [Figma](https://www.figma.com/), including making all colour, typography and layout decisions at this stage, to make sure that during development I am free to focus on the nuts and bolts of how to build the site, rather than getting distracted by design decisions at that stage. It has been successful for me in the past and so I have chosen to develop the site in this way again. 

---

### Surface

#### Wireframes

At this point I was able to bring together all the work I had done in creating the flow diagram (which included a lot of page content and structure decisions), my user stories, my scope chart and my database schema to create full visual designs for my site. This was more than just making colour and font choices however. Every design decision creates questions about what goes where, what colour should it be, does it even need to be there or would it be better somewhere else. I was able to ask informed questions at each stage to make sure the design reflected the user stories and site aims. E.g. What does a user need to see when they arrive on a page? What is the most important thing on a page and how can the design emphasise that? etc.

I created the designs below, making sure that all pages would work just as well on mobile and tablet as on desktop devices.

**View the Wireframes/Site Designs in the Dropdowns Below**

<details><summary>HOME</summary>
<img src="media/docs/design_wireframes_home.png">
</details>
<details><summary>PRODUCTS</summary>
<img src="media/docs/design_wireframes_products.png">
*All Products*
<img src="media/docs/design_wireframes_products_filtered.png">
*Filtered Products*
</details>
<details><summary>PRODUCT DETAILS</summary>
<img src="media/docs/design_wireframes_product_details.png">
</details>
<details><summary>ADD/EDIT PRODUCT</summary>
<img src="media/docs/design_wireframes_product_add.png">
</details>
<details><summary>ADD/EDIT REVIEW</summary>
<img src="media/docs/design_wireframes_review_add.png">
</details>
<details><summary>BAG</summary>
<img src="media/docs/design_wireframes_bag.png">
</details>
<details><summary>CHECKOUT</summary>
<img src="media/docs/design_wireframes_checkout.png">
</details>
<details><summary>CHECKOUT SUCCESS</summary>
<img src="media/docs/design_wireframes_checkout_success.png">
</details>
<details><summary>PROFILE</summary>
<img src="media/docs/design_wireframes_profile.png">
</details>
<details><summary>ORDER DETAILS</summary>
<img src="media/docs/design_wireframes_profile_order_history.png">
</details>
<details><summary>FAQS</summary>
<img src="media/docs/design_wireframes_faqs.png">
</details>
<details><summary>ADD/EDIT FAQ</summary>
<img src="media/docs/design_wireframes_faq_add.png">
</details>
<details><summary>CONTACT US</summary>
<img src="media/docs/design_wireframes_contact.png">
</details>
<details><summary>SITE MANAGEMENT</summary>
<img src="media/docs/design_wireframes_manage.png">
</details>
<details><summary>SIGN IN</summary>
<img src="media/docs/design_wireframes_accounts_signin.png">
</details>
<details><summary>REGISTER</summary>
<img src="media/docs/design_wireframes_accounts_register.png">
</details>

*Please note - designs for all authorisation pages will be replicated across all AllAuth templates. Sign In and Register have been created as a template for the others.*
- - -

#### Colour

![Website Colour Scheme](media/docs/design_color.jpg)

I used a colour palette of yellows and greys with a blue highlight colour to create contrast. I also added additional colours for all success/edit/info features and delete/warning/error features as well as to help categorise different statuses of messages & reviews on the profile & manage pages. I used a number of shades of the colours to help create contrast, to make the site legible and got give more flexibility in the design. The colours changed slightly during the validation stage as the yellow & grey on the rating hexagons were causing some contrast errors, so I introduced an orange tone to replace the yellow and darkened the grey hexagons to make sure the site was fully accessible. [See design changes.](#design-changes)

- - -

#### Typography

The website uses 2 typefaces that I felt worked well together and complemented each other:
- [Oxygen](https://fonts.google.com/specimen/Oxygen) for headings & the site logo
- [Source Sans 3](https://fonts.google.com/specimen/Source+Sans+3) for the main body text

- - -

#### Images & Graphics

All images are fully credited in the [here](#credits).

##### Logo
I created a logo for the site in the shape of a simplified bee as it is a strong iconic image and gives an immediate sense of the purpose of the site and a strong brand image. I created 2 versions, one with text for larger screens and another without which works as an icon. I also created a Favicon with a yellow background using the same logo.

<details><summary>Island Bees Logo - Favicon Version</summary>
<img src="media/android-chrome-192x192.png">
</details>

##### Hexagons
There are recurring hexagon shapes and background patterns throughout the site, on the Hero image on the home page, on the bag icon in the nav bar, in the products div as a background pattern and as a rating 'star' on the products. The hexagon continues the bee theme and creates a unique graphic element that runs through the site.

<details><summary>Hex Background</summary>
<img src="media/hex-bg-tran.svg">
</details>

##### Error Bee
The error pages contain a bee cartoon from Freepik (see credits section) to make these pages tie in with the rest of the site.

<details><summary>Error Bee</summary>
<img src="media/bee-2.png">
</details>

##### No Image Graphic
I also created a 'no-image' graphic to be used whenever a product doesn't have an image using the site logo.

<details><summary>No Image</summary>
<img src="media/no_image.jpg">
</details>

- - -


#### Design Changes

During development there were a number of changes that mean the final site has deviated from the above designs slightly. These came about for a number of reasons but were usually related to technical problems during the development process which could be solved through small design changes, or to improve the User Experience, accessibility or general feel of the site once it was up and running. It is important to make a plan and stick to it, however it is also important to be flexible enough to adapt when a new and better idea comes along. All of these decisions were taken keeping the user stories and user experience in mind at all times.

##### Review / FAQ form
I had planned to make these forms appear as modals, rather than separate pages, I thought it would improve user experience to give users the sense of staying in the same area whilst filling in the form. However, I quickly realised that this would present some technical challenges, mostly relating to having multiple modals on a page, and having a modal trigger another modal. I felt that the difficultly and time that this would add to the project was not worth it, so these pages became separate pages, with a form that looks more like the other forms. In the case of the review form I kept a slightly more unique styling as this is a form for users, rather than admins and I felt it would add a nice design touch to the site.

##### Colour changes
There were a number of changes to the colour scheme during the development process. In the wireframes you can see the original colours, however the colour palette above reflects the final colours used in the site. These changes happened during the accessibility testing stage, where it flagged up a number of issues with the yellow in particular, against the white background. The biggest change that most people would notice is on the rating hexagons, which are a bright orange on the final site, rather than a soft yellow.

##### Home Page Category Hexagons
Whilst developing the site I found that using a hexagon shape in CSS is somewhat challenging, particularly when it comes to stacking, moving and repeating them in rows, they are a difficult shape to work with. However, I persevered and managed to include them in a number of different places using a variety of techniques. On the home page I created a lovely stacking set of 4 hexagons which was fully responsive, based on this excellent piece of CSS work by [Temani Afif](https://dev.to/afif/responsive-hexagon-grid-without-media-query-57g7). Sadly, during CSS Validation, it threw up an error, despite working perfectly, and I couldn't find a way around it without my project failing CSS validation, so the hexagons had to go. I replaced them with squares which do the same job. For more information and a look at the original hexagon grid in action go to CSS Validation in [TESTING.md](TESTING.md)

##### Edit / Delete Product Buttons on Cards
I made the decision to remove the CRUD functionality buttons from the product cards. This came about when I discovered there was an issue with deleting products which had previously been ordered by a customer, it caused huge problems to delete them and was not good practice as all of the orders would then be incorrect as the product and its cost would be removed from them. This led to a number of changes on the site, one of which was making delete only accessible from the product details page. I felt that it provided a better user experience to remove both buttons from the cards and provide a single point of access to site admins.

##### Discontinued Tick Box on Product Forms
Following on from the above changes I also added a 'discontinued' field to the product forms to allow admins to mark a product as 'discontinued' rather than delete it, which solved the problem of deleting products which were connected with past orders.

##### Review approval
This is a feature that I added later in the process, which gives admins the ability to approve a review before it goes live, it also removed the admin's access to editing reviews as I felt this was poor business logic and would undermine customer trust in the reviews. This led to a couple of design changes; the addition of a 'PENDING APPROVAL' flag to the reviews on the user profile page so that users could see the status of their review & adding the unapproved reviews to the site management page with a toggle switch for admins to approve them.

##### Other minor changes
There were also other small tweaks to the site in terms of layout, margins, sizing and style, which are part of the natural course of development. As with all these changes they were made whilst keeping the User Stories in mind at all times.

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

There are a number of features I would like to implement in the future, particularly if I were adapting this in to a real live site for an online shop as there is some functionality I feel it would really benefit from.

#### Blog
This was something I had actually planned for in my original designs but I soon discovered that the development would be a time consuming process and I made the decision, based on my original [project scope planning document](#scope) that the blog's low importance and the difficulty of creating the responsive hexagon grid for the blog post summaries made it the best thing to put aside for later. However it would be a great tool for a company to have to build their brand and engage their users, and I'm very keen to build the hexagon grid when time allows! I have included the original designs for a taste of what it might look like.

<details><summary>BLOG</summary>
<img src="media/docs/design_wireframes_blog.png">
</details>
<details><summary>BLOG POST</summary>
<img src="media/docs/design_wireframes_blog_post.png">
</details>
<details><summary>ADD/EDIT BLOG POST</summary>
<img src="media/docs/design_wireframes_blog_post_add.png">
</details>

#### Admin Messaging System - Expand
I would like to build on the messaging system that I included in the Site Management page, giving the site admins the ability to reply directly from the site, to be able to view the historic chain of communication, to have multiple statuses for messages e.g. in-process, and to connect messaging to the user so that users could also reply from within the site rather than via email. I would also like to add notifications to both admins and users when they receive a message, with an icon appearing in the navbar to alert them.

#### Booking and Scheduling system for Beekeeping courses
I would also like to add a live calendar for beekeeping courses where users can book a place on a course with a specific date & check availability for courses.

#### Order Tracking
I feel that an e-commerce site would also benefit from an order-tracking system which notifies admins when an order is placed and then can be tracked from within the site management area, with its status changing depending on what stage the order is at e.g. 'out for delivery' 'cancelled' etc.

#### Stock Control
I also think some sort of stock control would be useful for an e-commerce site, with products having stock supply levels and logic to hide items that are out of stock as well as notify admins when things need to be re-supplied. This would also need to be integrated with any physical shop that the owners might have and so would be a significant project.


- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## Technologies Used

### Languages

- [HTML:](https://en.wikipedia.org/wiki/HTML5) Used to build the main structure of the site
- [CSS:](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) Used to style the website (Combination of bespoke styling and Bootstrap)
- [JavaScript:](https://en.wikipedia.org/wiki/JavaScript) Used for front end interactive features
  - Bag / Product Quantity Input
  - Stripe Payment Handling
  - Message is_open toggle functionality
  - Review is_authorised toggle functionality
  - Manage page scroll on refresh
  - Product form image field text
  - Product sorting page reload
  - Countryfield on address forms
  - Review rating select interactive styling
  - Scroll to Top button
  - Remove & Update products from bag
- [Python: ](<https://en.wikipedia.org/wiki/Python_(programming_language)>) Used to build the core of the backend of the project within the Django framework


### Frontend Frameworks / Libraries

- [Bootstrap:](https://getbootstrap.com/) Used throughout the site for the styling, layout & responsiveness
- [Font Awesome:](https://fontawesome.com/) Used to add icons to the site to help with UX and to add more character
- [JQuery:](https://jquery.com/) JavaScript library for making JavaScript quicker and easier to write


### Backend Modules / Packages & Frameworks

- [Django:](https://www.djangoproject.com/) High Level Python-based Web Framework.
- [AllAuth:](https://django-allauth.readthedocs.io/en/latest/) Integrated Django authentication & sign in.
- [Django Countries:](https://pypi.org/project/django-countries/) Django application that provides country choices for forms
- [Django Widget Tweaks:](https://pypi.org/project/django-widget-tweaks/) Django form field advanced styling & customisation
- [Django Storages:](https://django-storages.readthedocs.io/en/latest/) Collection of custom storage backends for Django
- [Freezegun:](https://pypi.org/project/freezegun/) Library to aid automated testing by giving control over the datetime module
- [Gunicorn:](https://gunicorn.org/) A Python WSGI HTTP Server for UNIX
- [Pillow:](https://pypi.org/project/Pillow/) Python imaging Library for extended image handling capabilities
- [Psycopg2:](https://www.psycopg.org/) Postgres adaptor to allow smooth communication between the backend and the database
- [s3transfer:](https://pypi.org/project/s3transfer/) Python library for managing Amazon AWS S3 Transfers
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) & [Botocore:](https://github.com/boto/botocore) Used to create, configure & manage AWS services using Python
- [Stripe:](https://stripe.com/gb) Stripe package part of the Stripe ecosystem to manage secure online payments
- [dj-database-url:](https://pypi.org/project/dj-database-url/) Allows you to use DATABASE_URL env variable in settings.py
- [Coverage:](https://coverage.readthedocs.io/en/7.3.1/) Tool for measuring code coverage of Python Programs
- [oauthlib](https://pypi.org/project/oauthlib/) & [requests-oauthlib:](https://pypi.org/project/requests-oauthlib/) Handles authentication using the OAuth request signin logic
- [python3-openid:](https://pypi.org/project/python3-openid/) Set of python packages to support the use of teh OpenID decentralised identity system
- [sqlparse:](https://pypi.org/project/sqlparse/) SQL parser for Python
- [urllib3:](https://pypi.org/project/urllib3/) HTTP client for Python
 

### Other Tools

- [Git:](https://git-scm.com/) Used for version control via Code Anywhere by using the terminal to Git and Push to GitHub
- [GitHub:](https://github.com/) Used to store the project code
- [Gitpod:](https://www.gitpod.io/) Used to create, edit & preview the project's code
- [Heroku:](https://dashboard.heroku.com/apps) Used to deploy the live site


### External Sites / Resources / Software

- [Figma:](https://www.figma.com/) Used to develop the wireframes in to a full site design including colours, fonts, proportions etc
- [Google Fonts:](https://fonts.google.com/) Used to select & import the fonts to the project (Oxygen & Source Sans 3)
- [Lucidchart](https://www.lucidchart.com/pages/) To create the flow diagram of the website
- [DrawSQL](https://drawsql.app/) Used to visually design the database schema
- [ChatGPT:](https://chat.openai.com/auth/login) Used to generate copy to populate site (not used for any code)
- [Adobe Illustrator:](https://www.adobe.com/uk/products/illustrator.html) Used to create the site logo
- [Adobe Photoshop:](https://www.adobe.com/uk/products/photoshop.html) Used to crop, adjust and resize the photos to optimise them for the site
- [Bulk Photo Resize:](https://bulkresizephotos.com/en) Used to resize & convert images 
- [Tiny PNG:](https://tinypng.com/) Used to further optimise the images for the site and reduce file size
- [ezGIF:](https://ezgif.com/) Creating GIFs for the README
- [tableconvert.com:](https://tableconvert.com/csv-to-markdown) Converting CSV files to Markdown tables for README
- [Favicon.io:](https://favicon.io/favicon-converter/) Used to create and add the favicon to the browser tab
- [Google Chrome Dev Tools:](https://developers.google.com/web/tools/chrome-devtools) Used to inspect page elements, debug issues with the site & test responsiveness on different mockup devices
- [Techsini:](http://techsini.com/multi-mockup/index.php) Website mockup image generator for images in this README.
- [Temp Mail:](https://temp-mail.org/en/) Temporary email generator for testing account verification & order confirmation


- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


### Testing & Bugs

The full test results and details of bugs and their fixes can be found in the [TESTING document](TESTING.md)


- - -
[Go to Top](#island-bees---e-commerce-site)
- - -

## Deployment

### Forking the GitHub Repository

Forking the GitHub repository allows you to create a duplicate repository in order to make changes without affecting the original.

1. Log in to GitHub and go to the [Island Bees GitHub repository](https://github.com/emmahewson/island-bees)
2. Click on Fork (top right) to fork the repository
3. Give the fork a name and description if you wish and click "Create Fork"
4. You can now open the repository in your IDE of choice e.g. GitPod
5. Once in your IDE you can install the project requirements from the requirements.txt file using the command `pip3 install -r requirements.txt`

---

### Making a Local Clone

A local clone allows you to create a copy of the project to work on locally on your own computer in your code editor of choice (e.g. VS Code)

1. Log in to GitHub and go to the [Island Bees GitHub repository](https://github.com/emmahewson/island-bees)
2. Click on "Code"
3. To clone using HTTPS copy the provided link on the HTTPS tab
4. Open your own terminal for your coding environment (making sure you have Git installed)
5. Set your current directory to the location you want to store your new clone
6. Type `git clone`, followed by the copied link you copied from GitHub e.g. `git clone https://github.com/emmahewson/island-bees.git`
7. Press Enter to create your local clone of the project
8. Set up your local development environment
9. Install the project requirements from the requirements.txt file in the project using the command `pip3 install -r requirements.txt`
10. Create your own env.py file containing all the required environment variables
11. You are now ready to start working on your own clone of the project - enjoy!


For more details and information go to GitHub's useful guide to [cloning repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)

---

### Deploying Your App

Deployment allows you to transfer your project from your local environment or IDE to hosting it publicly for other people to view and enjoy. There are certain steps you will need to take to do this and they are detailed below. **These instructions are based on using an IDE like GitPod and having followed the instructions for Forking the repository above, especially installing the requirements.** For users wishing to deploy from a local clone different steps may be required which will depend on your local development environment.

#### Setting up a Database

When working on the app in GitPod a local database (sqlite) is used which will not be available on the deployed app. You will need to set up a separate database for the deployed site.

1. Go to [ElephantSQL](https://www.elephantsql.com/) and click on 'get a managed database'
2. Select 'Tiny Turtle'
3. Sign in using your GitHub account & authorise ElephantSQL to access your GitHub account
4. Set up a team and go through the login credential process or log in if you already have an account
5. Once you are logged in name your plan (usually the project name)
6. Select your nearest region
7. If you're happy click on 'create instance'
8. Go to your dashboard (click on the ElephantSQL logo) and click on the instance name
9. Copy the database URL... you will need this for the next steps

---

#### Set up Heroku & connecting your new Database


1. Go to [Heroku](https://www.heroku.com/) and log in (or set up an account if you don't have one - please note you may incur charges for using Heroku)
2. Click on the 'New' button then 'create new app'
3. Name your app and select your nearest region
4. With your app set up go to the app's settings tab and under config variable click on 'reveal config variables' and add a new variable with the Key of `DATABASE_URL` and the value as the database URL that you copied from ElephantSQL
5. Back in GitPod go to settings.py and paste the following in to your DATABASE section to tell it to connect to the new database **Note - do not push your code to GitHub whilst this value is in your settings.py, it is a secret value that must not be shared, we will remove it later**

```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('your elephanySQL database url here'))
    }
```

6. In you GitPod terminal type `python3 manage.py showmigrations` to check you are connected to the new database, if you are you will see a list of migrations with no ticks next to them
7. Run the following command `python3 manage.py migrate` to migrate the database structure from your project to the new database
8. Any data that you have added to your SQLite database will not transfer to the new one. You will need to populate the site on the deployed app once it is up and running or using Fixtures (JSON files with all your database content) if you have them. You can find out more about Fixtures and how to use them in the [Django documentation.](https://docs.djangoproject.com/en/4.2/howto/initial-data/#:~:text=you%20use%20TransactionTestCase.-,fixtures%20.,the%20manage.py%20dumpdata%20command.)
9. Create a superuser for your deployed site and new database (this will allow you to check if the database is working and access the site admin on the deployed site) using the following command in the terminal: `python3 manage.py createsuperuser` and set up login details for them following the instructions.
10. Go to the ElephanySQL site, click on your database, go to the browser tab and click on 'table queries' and select 'auth_user (public)' and click on execute, you should see your newly created user.
11. You now need to remove your new database settings from settings.py and set it up to know which version of the site you are on (development or live) to know which database to use. Go back to your GitPod dashboard, click on your avatar to go your your GitPod user settings and select 'variables'
12. Add a key of DEVELOPMENT and a value of True
13. Got to your settings.py file to the DATABASES section and replace what's there with the following code (this checks to see if there is a value called DEVELOPMENT in your environment variables - ie your development environment, rather than the deployed app and sets the database accordingly.)

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

14. Now that you have removed your ElephantSQL database url from the settings.py file it is safe to push your code to GitHub again. Your deployed database is set up and GitPod knows which one to use for which version of the site.


#### Deploying to Heroku

1. Create a Procfile in your app in the root directory with the following content `web: gunicorn island_bees.wsgi:application` and a blank line at the end.
2. Log in to Heroku using the GitPod terminal using the command `Heroku login`` and enter your Heroku email and password
  - if you have 2 factor authentication set up you will need to use `Heroku login -i` followed by your email and your Heroku API key as the password which you can find in your account settings on Heroku
4. Temporarily disable Heroku from collecting static files during deployment using the command `heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name`
5. Commit your changes to GitHub using `git add .`, `git commit` & `git push` in the terminal
6. Then to deploy your site to Heroku use the command `git push Heroku main`
7. Your site will now be deployed without any of the static files (CSS, JavaScript & Media files)
8. In Heroku go to your app, click on activity to check if it has finished deploying and once it has go to the settings tab
9. Scroll down to 'Domains' and copy the 'your app can be found at' URL
10. Back in GitPod go to settings.py and add your deployed site's URL to the ALLOWED_HOSTS list
11. `git add .`, `git commit` & `git push` again and then `git push Heroku main` to push your changes
12. Once the site has finished deploying you should be able to navigate to the deployed site's URL and see your site content, though it will be a little strange-looking without CSS & media files!
13. You now need to replace the Django secret key in your settings.py (if you included it there) with an environment variable to keep it safe. To do this you can use a Django secret key generator online e.g. [djecrety](https://djecrety.ir/), copy the key it provides.
14. Go to your Heroku app's dashboard, open settings and reveal config variables and add a new variable with a key of SECRET_KEY and a value of what you just copied.
15. In GitPod, if you have used your secret key in settings.py, go back to your GitPod dashboard, click on your avatar to go your your GitPod user settings and select 'variables'
16. Add a key of SECRET_KEY and a value of a different Django secret key from your online key generator (djecrety or similar)
17. In settings.py and change the SECRET_KEY to `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
18. Below it change the value of DEBUG to the following `DEBUG = 'DEVELOPMENT' in os.environ` to dynamically change whether the app is in DEBUG mode depending on whether it is the development or deployed site
19. `git add .`, `git commit` & `git push` again and then `git push Heroku main` to push your changes
20. You can also tell Heroku to automatically deploy so you don't need to push changes to both GitHub and Heroku each time - you'll find this under the Deploy tab on your Heroku app.


#### Setting Up Your Static Files on Your Deployed Site using Amazon Web Services (AWS)

There are many options for storing your static files for a deployed site, below are the instructions for using Amazon Web Services as a cloud storage provider.

1. Create an AWS account [here](https://aws.amazon.com/) (Select a personal account for the account type). You will need to fill in your information and card details to set up an account
2. Once your account is set up and you're signed in search for s3 in the search bar
3. Click on 'create bucket' and name it to match your Heroku app, selecting your closest region and uncheck 'block all public access' then click on create bucket to set it up
4. Click on your new bucket name and go to the properties tab
5. Scroll to the bottom and click on the edit button by 'Static Website Hosting' and select 'enable', giving default values for the index and error documents (index.html & error.html) then click save changes.
6. Go to the permissions tab and copy the ARN value at the top.
7. Scroll down to the bucket policy section, select 'edit' and 'policy generator'
8. Select 'S3 bucket policy' from the dropdown
9. In principles put a * to allow all
10. Set the action to 'Get Object'
11. Paste the earlier ARN value in the ARN input
12. Click on 'add statement' then 'generate policy'
13. Copy the policy text that the generator creates
14. Back in your bucket settings (should still be open in another tab) paste the text in to the Bucket Policy empty text area then add a '/*' to the end of the resource value (which should have your bucket name in it) this will allow access to all the resources in the bucket and click save
15. Scroll down to the access control list and grant Read and Write access to Everyone (public access) by checking the boxes
16. Scroll down to the Cross-Origin Resource Sharing (CORS) section and paste in the following and save:

```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

17. Go back to your AWS dashboard by clicking on the AWS logo at the top left and type in IAM in the search bar and select the IAM service
18. Click on the user groups tab and create a new group, with the name of your choice, ideally with your app name in it and create the group
19. Go to the policies tab and create a policy, go the JSON tab and search for the S3FullAccess policy and import it
20. Edit the policy to the following:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*",
            ]
        }
    ]
}
```

21. Click on next and then review
22. Name the policy and give it a description and then create your policy
23. Go to the User Groups tab, select your group and go to permissions and click 'add permissions' then 'attach policy' selecting your newly created policy and clicking 'Attach policies'
24. Create a user for the group by going to the User tab and clicking 'create user'
25. Name your user (you don't need to select AWS Console access) click next and add your user to your group clicking next as required and 'create user'
26. Download and save the csv file with the user's credentials - this is important, you will not be able to access this information again
27. Back in GitPod go to your settings.py file and paste in the following code which tells the app to look for an environment variable called USE_AWS and if it's there to use the following settings to access the static files.

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'island-bees'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
28. Set up the following config variables in Heroku using the information in the csv file that you downloaded:
  - AWS_ACCESS_KEY_ID: *your access key value*
  - AWS_SECRET_ACCESS_KEY: *your secret access key value*
  - USE_AWS: True
29. Remove COLLECTSTATIC from the config variables in Heroku
30. Back in GitPod create a file called custom_storages.py in the root directory and add the following:

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

```

31. In settings.py add the following to tell it to look for the new storage classes we just created in custom_storages and to override the URLS for static and media files. Put this just below the AWS code from earlier within the if `'USE_AWS' in os.environ` statement.

```
# Static and media files
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

# Override static and media URLs in production
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

32. You're nearly there! Save your settings.py then push to add/commit/push to GitHub (if you've set up automatic deploys you won't need to also push to Heroku)
33. Once the deployment has finished check your S3 bucket, there should be a static folder in there with your static files (CSS / JS folders with files inside) and the live site should now have its CSS styling and any JavaScript functionality.
34. Finally to add your media files (images & video) simply go back to AWS, create a new folder called 'media' in the same place as the new 'static' folder, click on the folder and drag and drop all your media files in to the browser window.
35. Click next and under manage public permissions select 'grant public access to these objects' and click upload
35. Your site should now contain all your images, videos, styling and JavaScript! Well done!


#### Setting up Stripe Payments on your deployed site

1. Log in to Stripe, click on the developers tab and API keys copy the API key and set them in Heroku as config variables in the following:

- STRIPE_PUBLIC_KEY: Stripe publishable key goes here
- STRIPE_SECRET_KEY: Stripe secret key goes here

2. Back in Stripe set up a new webhook for your deployed site by clicking on webhooks, click on 'add endpoint' and paste in your deployed site's URL setting it to listen for all events.
3. Click on your newly set up webhook and click on 'Signing Secret' at the top to reveal the secret value. Copy it and set it as a new config variable in Heroku:
- STRIPE_WH_SECRET: Signing secret from new webhook.


- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## Credits

### Code

I have found many useful sources in building this project, reliant on a lot of Googling and trawling through documentation and Slack channels. Any code that requires crediting has been mentioned within the code itself. However below are some projects which I have found useful for more general inspiration and to help me answer the more general questions about how to approach different aspects of the project.

- [Joy Zadan's K-Beauty CI PP5 Project](https://github.com/JoyZadan/shop-kbeauty): I found this project to be really helpful in getting started with how to approach mine, in particular how to approach the rating & reviews. I also used her automated testing files as a skeleton for how to approach this part of mine. I am very grateful for her clear and well explained project. I also found her README deployment really clear and easy to follow and got inspiration for how to approach mine.
- [NyxHexen's Game Box CI MS4 Project](https://github.com/NyxHexen/CI_MS4_GB): I also found this project's testing really useful in working out how to approach automated testing, the tests have clearly been written by a skilled and experienced automated tester and helped me as a complete beginner in automated testing to begin my learning and automated testing on my project.
- I should also credit the [Code Institute](https://codeinstitute.net/) team for their [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) project as this had a big influence on my own Island Bees site. Parts of the code are heavily inspired by and adapted from Boutique Ado. Using Django and building an e-commerce site was a huge challenge and I was grateful to have this walkthrough to follow whilst I built my confidence on my own project, using it as a starting point to expand upon to create Island Bees.

- - -

### Content

#### Text

- [ChatGPT:](https://chat.openai.com/auth/login) Used to generate text for the products, reviews, messages & FAQs to quickly populate the site so my time could be better spent on building the site and my coding knowledge. **It was not used to generate any code for the project.**

#### Graphics
- Error Page Cartoon Bee [Pixabay](https://pixabay.com/vectors/bee-insect-cartoon-honey-bee-24633/)
- Hexagon Background Pattern [FreePik](https://www.freepik.com/free-vector/modern-stylish-hexagonal-background-wallpaper_35514628.htm)

#### Images
- Hero Image - Bees on Comb [Simon Kadula on Unsplash](https://unsplash.com/photos/DIwC450lRGI)
- Product - Honey Jar [Abelo](https://www.abelo.co.uk/shop/jars/honey-jar-labels-gold/)
- Product - Beekeeping Course [13 Bees](https://www.13bees.co.uk/beekeeping-experiences)
- Product - Beekeeping Course [National Diploma Beekeeping](https://national-diploma-beekeeping.org/)
- Product - Beekeeping Course [Gwenyn Gruffydd](https://gwenyngruffydd.co.uk/collections/courses-and-workshops/products/beekeepingtraining) 
- Product - Beekeeping Course (Kids) [David and Jane Richards](https://www.djrff.org/blog/why-were-supporting-beekeeping-in-schools) Product - Beekeeping Course (Kids)
- Product - Hive[Abelo](https://www.abelo.co.uk/shop/national-hive/national-hive-cedar-1st-quality/wbc-national-hive-english-cedar/)
- Product - J-Tool [Bee Basic](https://www.beebasic.co.uk/product/j-shaped-bee-hive-tool/) 
- Product - Live Bees [Staunton Park](https://staunton-park.co.uk/cdn/shop/products/AMM-BRITISH-BLACK-BEES-Staunton-Park-1676023351.jpg?v=1676023353) 
- Product - Live Bees [South East Tagnet](https://southeastagnet.com/2021/12/20/attract-swarm-bees-property/)
- Product - Queen Bee [Gilboys] (https://gilboys.co.uk/blogs/waxing-lyrical/be-more-queen-bee-this-mothering-sunday)
- Product - Bee Suit [Old Castle Farm Hives](https://www.oldcastlefarmhives.com/product/sentinel-pro-ii-bee-suit/)
- Product - Starter Kit [Old Castle Farm Hives](https://www.oldcastlefarmhives.com/product/beekeepers-complete-starter-kit/)
- Product - Bee Brush [Old Castle Farm Hives](https://www.oldcastlefarmhives.com/product/bee-brush/)
- Product - Propolis Tincture [The Organic Pharmacy](https://www.theorganicpharmacy.com/fresh-propolis-tincture/)
- Product - Uncapping Knife [Gwenyn Gruffydd](https://gwenyngruffydd.co.uk/products/honey-uncapping-knife-for-beekeepers)
- Product - Candles [Gwenyn Gruffydd](https://gwenyngruffydd.co.uk/products/handrolledbeeswaxcandlesuk)
- Product - Pollen [Gustiamo](https://www.gustiamo.com/raw-wildflower-bee-pollen/)
- Product - Smoker [Amazon](https://www.amazon.co.uk/Smoker-Stainless-Shield-Beekeeping-Equipment/dp/B009Z1SLQK?th=1)
- Product - Tool Set [Amazon](https://www.amazon.co.uk/Beekeeping-Supplies-Equipment-Beekeeper-Uncapping/dp/B07F8R4BVQ)
- Product - Lip Balm [My Bee Balm Co.](https://mybeebalmco.com/)
- Product - Bumble Bee Box [Green Gardener](https://www.greengardener.co.uk/product/bumble-bee-nest-box/)
- Product - Solitary Bee House [Green Gardener](https://www.greengardener.co.uk/product/modular-solitary-bee-house/)
- Product - Honey Comb [Freepik](https://www.freepik.com/premium-photo/yellow-honeycomb-slices-isolated-white-background_24533816.htm)

- - -

### Acknowledgments

* My mentor [Gareth McGirr](https://github.com/Gareth-McGirr/) for all his help and advice throughout the project
* The whole team at [Code Institute](https://codeinstitute.net/) for their teaching and support

- - -

[Go to Top](#island-bees---e-commerce-site)

