# Island Bees - E-Commerce Site - Testing

![Mock-up](media/docs/mp4_mockup.jpg)

#### **By Emma Hewson**
[Click here to view the live web application](https://island-bees-5e7b15194c83.herokuapp.com/)

This is the testing documentation for my e-commerce web application: Island Bees.

- - -
## Table of Contents

- [Introduction](#introduction)
- [Automated Testing](#automated-testing-using-test-driven-development)
- [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Linting](#javascript-linting)
    - [Python Linting](#python-linting)
    - [Accessibility Testing](#accessibility)
    - [Performance Testing](#performance)
- [Feature Testing](#feature-testing)
    - [Responsiveness/Device Testing](#responsiveness--device-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Feature Testing Results](#feature-testing-results)
- [User Stories Testing](#user-stories-testing)
- [Bugs and Fixes](#bugs--fixes)


---

## Introduction

In my testing I developed a comprehensive testing plan to make sure that the site was functioning correctly. I used a combination of automated testing using Django's built in test functionality and manual testing. The site was tested throughout the process, both in the development and deployed version of the sites. All the test results detailed below are based on the [deployed site](https://island-bees-5e7b15194c83.herokuapp.com/).

---

## Automated Testing using Test Driven Development

During development I tried to maintain a test driven development approach. This was my first experience of using automated testing on a project so I kept things simple and wrote and ran tests appropriate to my experience level (backed up by rigorous manual testing both during the development process and at the end - see [feature testing](#feature-testing)) This allowed me to try my hand at automated testing and build my knowledge within the scope and time restraints of the project and course requirements. As part of the TDD (test driven development) approach; all automated tests were written either alongside or immediately after each stage of development and were run at regular intervals to make sure that subsequent features had not affected earlier ones.

I managed to achieve 83% coverage with my tests. I would have liked to reach 100% but as this was my first time doing any automated testing in a project, and with limitations on my time and experience, I was happy with this result, especially as the automated testing is backed up with comprehensive manual testing.

I found it to be a challenging but useful process, a number of times during development automated tests were able to flag up issues much earlier than I would have noticed them with manual testing alone. With large, complex project with inter-woven features and dependencies I can completely see the benefit of this approach and I look forward to expanding my knowledge and delving more in to the world of automated testing in the future.

### Automated testing coverage and results

**Automated Testing - Test Results**

<img src="media/docs/test_auto_results.jpg">

**Coverage Report - Total Coverage**

<img src="media/docs/test_auto_all.jpg">


**Coverage For Individual Apps**

<details><summary>Home App</summary>
<img src="media/docs/test_auto_home.jpg">
</details>

<details><summary>Bag App</summary>
<img src="media/docs/test_auto_bag.jpg">
</details>

<details><summary>Checkout App</summary>
<img src="media/docs/test_auto_checkout.jpg">
</details>

<details><summary>FAQs App</summary>
<img src="media/docs/test_auto_faqs.jpg">
</details>

<details><summary>Island Bees App</summary>
<img src="media/docs/test_auto_ib.jpg">
</details>

<details><summary>Manage App</summary>
<img src="media/docs/test_auto_manage.jpg">
</details>

<details><summary>Products App</summary>
<img src="media/docs/test_auto_products.jpg">
</details>

<details><summary>Profiles App</summary>
<img src="media/docs/test_auto_profiles.jpg">
</details>

<details><summary>Reviews App</summary>
<img src="media/docs/test_auto_reviews.jpg">
</details>



- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## Validation


### HTML Validation

I ran the code for all the pages through the [W3C HTML Validator](https://validator.w3.org/nu/) using the textarea input by generating the source code from the deployed site (right click and select 'View Page Source' in Chrome) and pasting it in to allow me to check all pages whether requiring log in or not. All code passed the validation tests. Results below.


<details><summary>HTML Validation Results Table</summary>

| **Feature** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|
| **HOME** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **PRODUCTS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **PRODUCT DETAILS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **ADD PRODUCT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Form table errors & custom clearable fit input issue - resolved | PASS |
| **EDIT PRODUCT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Form table errors & custom clearable fit input issue - resolved | PASS |
| **ADD REVIEW** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **EDIT REVIEW** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **BAG** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Duplicate ID error - resolved | PASS |
| **CHECKOUT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **CHECKOUT SUCCESS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **PROFILE** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **FAQS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **ADD FAQ** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Form table errors - resolved | PASS |
| **EDIT FAQ** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Form table errors - resolved | PASS |
| **CONTACT US** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **MANAGE** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **ALLAUTH TEMPLATES** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | contact_us tag error - resolved | PASS |
| **400** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **403** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **404** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **500** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |


</details>




#### Issues resolved during validation:

- Django forms renders its form inputs as a table and there were multiple errors about stray `<tr>` tags in the code, which I couldn't access as the form was added by using just `{{form}}`. I got around this based on a [post](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1548669436265400) I found on the CI Slack Channel suggesting rendering them as `<p>` elements instead using `{{form.as_p}}` and amending the styling as necessary.

- Image selection in the custom_clearable_file_input on the product form was throwing an error as it had 2 ID attributes, one that I had set which was used in the JavaScript to display the filename and another that was added by the `{% include "django/forms/widgets/attrs.html" %}` tag. I solved this problem by changing the JavaScript to get an element using a class name rather than ID and removing the class.

- The shopping bag was throwing an error about duplicate IDs, this came down to the 2 versions of the shopping bag, one for large screens one for mobile, which used the same include template from quantity-form.html, effectively putting 2 versions of the same code on the page. I solved this by changing the ID attribute to a data-id attribute, and adjusting the relevant JavaScript code.

- adding url tag to allauth email templates threw an error when these templates were rendered as they had `{% blocktrans %}` tags in which don't allow tags inside the translated area. I solved this issue by removing the contact us links.


<details><summary>Validation Final Results Screenshot</summary>

<img src="media/docs/docs_val_html.jpg">

</details>

*I have only included 1 screenshot of the results as an example because they are identical for every page and give no indication of which page is being checked.*

---

### CSS Validation

I ran the CSS code through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input). All code passed the validation tests. Results below.


<details><summary>CSS Validation Results Table</summary>

| **Feature**    | **Expected Outcome**                  | **Test Performed**                                   | **Result**                                                                                                              | **Pass / Fail** |
|----------------|---------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| CSS Validation | Page passes validation with no errors | Ran CSS through https://jigsaw.w3.org/css-validator/ | 2 issues - both resolved (see below) | PASS            |

</details>


#### Issues resolved during validation:

- I was getting Parse errors on various parts where I had nested elements within a hover element which worked perfectly but the validator didn't like:
e.g.
```
.lower-nav-link:hover {
    .lower-nav-link-text {
        -webkit-text-decoration-color: rgba(20, 12, 0, 0);
        text-decoration-color: rgba(20, 12, 0, 1);
    }
}
```
I solved this by refactoring all of them to the below syntax:

```
.lower-nav-link:hover .lower-nav-link-text {
        -webkit-text-decoration-color: rgba(20, 12, 0, 0);
        text-decoration-color: rgba(20, 12, 0, 1);
}
```

- The responsive hex grid with the category links on the homepage that I had taken from [this page](https://dev.to/afif/responsive-hexagon-grid-without-media-query-57g7) was throwing an error on use of pixel values rather than % values in the following code:

```
.container-hex-grid::before {
    shape-outside: repeating-linear-gradient(#0000 0 calc(var(--f) - 3px), #000 0 var(--f));
}
```

- This code uses some advanced mathematical and CSS skills. I have been unable to come up with a way of avoiding this error. It works perfectly in the browser and creates an elegant responsive hexagon grid but due to the need to resolve all errors I have removed this hexagon grid section and replaced it with a simpler layout. I am including a video of the hexagon grid in action below as I was disappointed to have to remove it.

**Hex grid buttons video**



https://github.com/emmahewson/island-bees/assets/116887840/659c7dd3-2a47-493f-8910-bd3ab84ba567




#### CSS Warnings

There were some warnings thrown up by the CSS Validator.

- Vendor extension warnings: refer to browser specific CSS classes such as `-webkit-transition`. These classes are best practice to make sure that certain CSS elements perform correctly in different browsers and so I have disregarded these warnings.
- Imported style sheets: This refers to Google's font import, again this is a standard way to import fonts directly in to the CSS.
- CSS Variables are not checked: This refers to the :root directory of colours and is just a warning that it cannot check these. They all performed as expected during testing and so I'm happy with this CSS code.
- Border and Background Colour are the same: whilst this is a legitimate warning about what could be an oversight in the code, in this case it was intentional as I was using it to restyle some Bootstrap elements, which often requires some fiddly CSS hacks, in this case I needed to specify the border colour rather than get rid of the border to make the button look the way I wanted.


<details><summary>Validation Final Results Screenshot</summary>

<img src="media/docs/docs_val_css.jpg">

</details>

---

### JavaScript Linting

I ran the JavaScript code through [JSHint](https://jshint.com/). For full results see the dropdowns below.

<details><summary>JavaScript Results Table</summary>

| **Feature** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|
| **quantity_input.js (bag)** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | No Errors | PASS |
| **stripe_elements.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. Undeclared variable (Stripe - declared elsewhere) | PASS |
| **message_toggle.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **review_toggle.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **scroll_messages.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | No Errors | PASS |
| **form-image.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | No Errors | PASS |
| **quantity_input.js (products)** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | No Errors | PASS |
| **sort_box.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **countryfield.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Unnecessary semi-colon. All fixed. No errors remaining | PASS |
| **rating_select.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **scroll_top.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **Script tag - bag.html** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |


</details>

<details><summary>JavaScript Results Images</summary>

<details><summary>quantity_input.js (Bag)</summary>
<img src="media/docs/docs_val_js_1.jpg">
</details>

<details><summary>stripe_element.js</summary>
<img src="media/docs/docs_val_js_2.jpg">
</details>

<details><summary>message_toggle.js</summary>
<img src="media/docs/docs_val_js_3.jpg">
</details>

<details><summary>review_toggle.js</summary>
<img src="media/docs/docs_val_js_4.jpg">
</details>

<details><summary>scroll_message.js</summary>
<img src="media/docs/docs_val_js_5.jpg">
</details>

<details><summary>form-image.js</summary>
<img src="media/docs/docs_val_js_6.jpg">
</details>

<details><summary>quantity_input.js (Products)</summary>
<img src="media/docs/docs_val_js_7.jpg">
</details>

<details><summary>sort_box.js</summary>
<img src="media/docs/docs_val_js_8.jpg">
</details>

<details><summary>countryfield.js</summary>
<img src="media/docs/docs_val_js_9.jpg">
</details>

<details><summary>rating_select.js</summary>
<img src="media/docs/docs_val_js_10.jpg">
</details>

<details><summary>scroll_top.js</summary>
<img src="media/docs/docs_val_js_11.jpg">
</details>

<details><summary>Script Tag in bag.html</summary>
<img src="media/docs/docs_val_js_12.jpg">
</details>


</details>

---

### Python Linting

I ran the app.py code through [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/) to check the Syntax. GitPod also has a built in Python Linter which was used throughout the development process (see below). All code passed the validation tests. For full results see the dropdowns below.

<details><summary>Python Results Table</summary>

| **App** | **File** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|---|
| island_bees | settings | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| island_bees | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| bag | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| bag | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| bag | contexts | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| bag | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | signals | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | webhook_handler | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | webhooks | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | test_forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | test_models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| faqs | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| faqs | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| faqs | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| faqs | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| faqs | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| faqs | test_forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| faqs | test_models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| faqs | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| home | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| home | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| home | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| manage | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| manage | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| manage | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| manage | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| manage | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| manage | test_forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| manage | test_models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| manage | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | widgets | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | test_forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | test_models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | test_forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | test_models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| reviews | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| reviews | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| reviews | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| reviews | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| reviews | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| reviews | test_forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| reviews | test_models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| reviews | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |


</details>


#### Additional Linting Using Flake8 in GitPod

I used the inbuilt linting in GitPod (Flake8) to check my code and keep it as clean as possible. All code was cleaned up, errors dealt with and any suggested changes made apart from the following issues which I was unable to solve:

- **checkout/apps.py - checkout.signals is imported but unused** - signals is being passed in and used elsewhere so can be disregarded
- **checkout/webhooks.py - local variable e is assigned to but never used** - have investigated this and it appears to be an industry standard way of assigning this particular error checking. I also passed this same code through the [CI Python Linter](https://pep8ci.herokuapp.com/) and it didn't raise an issue so I am disregarding this.
- remaining linting errors are in files that are automatically created by Django such as migration files & vscode/arctictern.py


---


### Accessibility

I ran the site through the [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/). There were some minor warnings which are detailed in the notes below.


<details><summary>Accessibility Results Table</summary>

| Feature           | Expected Outcome                      | Test Performed                            | Results - Fixed                                                                                                                                                 | Results - issues remaining (see notes) | Pass / Fail |
|-------------------|---------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-------------|
| HOME              | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Added aria label to search box • Added sr-only text to search button • Increased size & contrast of rating hexes                                                | Recurring warnings (see below)         | PASS        |
| PRODUCTS          | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Added an aria-label to the select input                                                                                                                         | Recurring warnings (see below)         | PASS        |
| PRODUCT DETAILS   | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Added an aria-label to the quantity input • Added sr-only spans to + / - buttons • Changed heading level order                                                  | Recurring warnings (see below)         | PASS        |
| ADD PRODUCT       | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Added an aria-label to the select image input button                                                                                                            | Recurring warnings (see below)         | PASS        |
| EDIT PRODUCT      | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Added an aria-label to the select image input button                                                                                                            | Recurring warnings (see below)         | PASS        |
| ADD REVIEW        | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |
| EDIT REVIEW       | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |
| BAG               | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Added an aria-label to the quantity input • Added sr-only spans to + / - buttons • Fixed the alt value on the product image / Increased contrast of Update Link | Recurring warnings (see below)         | PASS        |
| CHECKOUT          | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Added aria labels to the form inputs using Widget Tweaks                                                                                                        | Recurring warnings (see below)         | PASS        |
| CHECKOUT SUCCESS  | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Fixed contrast error on ‘Order Details’ heading                                                                                                                 | Recurring warnings (see below)         | PASS        |
| PROFILE           | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Rendered form as individual fields with aria labels using Widget Tweaks • Fixed contrast error on Toasts • Changed heading level order                          | Recurring warnings (see below)         | PASS        |
| FAQS              | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Changed heading level order                                                                                                                                     | Recurring warnings (see below)         | PASS        |
| ADD FAQ           | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |
| EDIT FAQ          | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |
| CONTACT US        | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |
| MANAGE            | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Changed heading level order • Increased contrast on delete button                                                                                               | Recurring warnings (see below)         | PASS        |
| ALLAUTH TEMPLATES | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | Added aria labels to the form inputs using Widget Tweaks                                                                                                      | Recurring warnings (see below)         | PASS        |
| 400               | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |
| 403               | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |
| 404               | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |
| 500               | Page passes validation with no errors | Ran page through https://wave.webaim.org/ | No fixes required                                                                                                                                               | Recurring warnings (see below)         | PASS        |


</details>



#### Notes on Accessibility Results

There were some recurring warnings which are detailed below:

**Possible headings**

Lots of references to text that is a possible heading - all checked and confirmed that the tag type best reflects the content in them (ie changed to a heading if text is a heading or left as a p element if not)


**Underlined text**

One of the hover effects I have used on the nav bar involves an underline on any link text on hover. Wave threw up a warning about these saying that underline tends to suggest a link, however as these are all links they can be safely disregarded.

**Redundant link**

Warning about links to the same place next to each other. All were checked to make sure that the site layout and links made sense in terms of user experience and to make sure that they couldn’t cause any confusion.

<details><summary>Accessibility Sample Screenshot</summary>

<img src="media/docs/docs_val_acc.jpg">

</details>

*As the alerts are repeated across many of the pages (they are generally on elements in the nav bar) I have just included a single screenshot as an example.*


- - -


### Performance

I ran the site through Google Chrome Dev Tools' Lighthouse to check on its performance scores. All pages passed the validation tests. For full results see the dropdowns below.

<details><summary>Performance Results Table</summary>


| **Feature**                             | **Expected Outcome**                          | **Test Performed**                | **Change / Final Result**               | **Pass / Fail** |
|-----------------------------------------|-----------------------------------------------|-----------------------------------|-----------------------------------------|-----------------|
| **HOME**                                | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Tinified Hero image • All scores 90+    | PASS            |
| **PRODUCTS**                            | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **PRODUCT DETAILS**                     | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **ADD PRODUCT**                         | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **EDIT PRODUCT**                        | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **ADD REVIEW**                          | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **EDIT REVIEW**                         | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **BAG**                                 | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **CHECKOUT**                            | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **CHECKOUT SUCCESS**                    | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **PROFILE**                             | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **FAQS**                                | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **ADD FAQ**                             | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **EDIT FAQ**                            | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **CONTACT US**                          | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **MANAGE**                              | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **SIGN IN (login)**                     | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **REGISTER (signup)**                   | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **MANAGE EMAIL (email)**                | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **CHANGE PASSWORD (password/change)**   | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **FORGOT PASSWORD (password/reset)**    | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **SIGN OUT (logout)**                   | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **VERFICATION SENT (confirm-email)**    | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **CONFIRM EMAIL (confirm-email/(key))** | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |


</details>


<details><summary>Performance Results Images</summary>

<details><summary>HOME</summary>
<img src="media/docs/docs_val_perf_1.jpg">
</details>

<details><summary>PRODUCTS</summary>
<img src="media/docs/docs_val_perf_2.jpg">
</details>

<details><summary>PRODUCT DETAILS</summary>
<img src="media/docs/docs_val_perf_3.jpg">
</details>

<details><summary>ADD PRODUCT</summary>
<img src="media/docs/docs_val_perf_4.jpg">
</details>

<details><summary>EDIT PRODUCT</summary>
<img src="media/docs/docs_val_perf_5.jpg">
</details>

<details><summary>ADD REVIEW</summary>
<img src="media/docs/docs_val_perf_6.jpg">
</details>

<details><summary>EDIT REVIEW</summary>
<img src="media/docs/docs_val_perf_7.jpg">
</details>

<details><summary>BAG</summary>
<img src="media/docs/docs_val_perf_8.jpg">
</details>

<details><summary>CHECKOUT</summary>
<img src="media/docs/docs_val_perf_9.jpg">
</details>

<details><summary>CHECKOUT SUCCESS</summary>
<img src="media/docs/docs_val_perf_10.jpg">
</details>

<details><summary>PROFILE</summary>
<img src="media/docs/docs_val_perf_11.jpg">
</details>

<details><summary>FAQS</summary>
<img src="media/docs/docs_val_perf_12.jpg">
</details>

<details><summary>ADD FAQ</summary>
<img src="media/docs/docs_val_perf_13.jpg">
</details>

<details><summary>EDIT FAQ</summary>
<img src="media/docs/docs_val_perf_14.jpg">
</details>

<details><summary>CONTACT US</summary>
<img src="media/docs/docs_val_perf_15.jpg">
</details>

<details><summary>MANAGE</summary>
<img src="media/docs/docs_val_perf_16.jpg">
</details>

<details><summary>SIGN IN (AllAuth Name - login)</summary>
<img src="media/docs/docs_val_perf_17.jpg">
</details>

<details><summary>REGISTER (AllAuth Name - signup)</summary>
<img src="media/docs/docs_val_perf_18.jpg">
</details>

<details><summary>MANAGE EMAIL (AllAuth name - email)</summary>
<img src="media/docs/docs_val_perf_19.jpg">
</details>

<details><summary>CHANGE PASSWORD (AllAuth name - password/change)</summary>
<img src="media/docs/docs_val_perf_20.jpg">
</details>

<details><summary>FORGOT PASSWORD (AllAuth name - password/reset)</summary>
<img src="media/docs/docs_val_perf_21.jpg">
</details>

<details><summary>SIGN OUT (AllAuth name - logout)</summary>
<img src="media/docs/docs_val_perf_22.jpg">
</details>

<details><summary>VERFICATION SENT (AllAuth name - confirm-email)</summary>
<img src="media/docs/docs_val_perf_23.jpg">
</details>

<details><summary>CONFIRM EMAIL (AllAuth name - confirm-email/(key))</summary>
<img src="media/docs/docs_val_perf_2.jpg">
</details>

</details>


#### Issues resolved during performance validation:

- Console Error about one of the Favicon icons being missing returning a 404, the site appeared to be looking in the wrong location for the file. I fixed this by explicitly naming all the icons in the `<head>` element and removing the web manifest.

<details><summary>Screenshot</summary>

<img src="media/docs/docs_val_perf_issue_1.jpg">

</details>


- - -
[Go to Top](#island-bees---e-commerce-site)
- - -

## Feature Testing

The whole site and all its features were tested thoroughly throughout the development process and at the end of development. This testing covered content, style, interactive feature functionality as well as making sure all backend processes worked as expected including testing of all CRUD functionality and routing.

### **Responsiveness / Device Testing**

The site was tested on the following devices
* Apple Macbook Pro 16inch
* LG Ultrafine Display 27inch External Monitor
* Apple iMac 5K 27-inch
* Apple iPhone SE 2020
* Apple iPhone SE 2022
* Google Chrome Developer Tools - simulator for all different device options as well as using the adjustable sizing options

### **Browser Compatibility**

The site was tested on the following browsers.
* Google Chrome
* Mozilla Firefox
* Apple Safari


__ __

### **Feature Testing Results**


<details><summary>All Pages</summary>


</details>

<details><summary>Home</summary>


</details>

<details><summary>Products</summary>


</details>

<details><summary>Product Details</summary>


</details>

<details><summary>Add / Edit / Delete Products</summary>


</details>

<details><summary>Add / Edit / Delete Reviews</summary>


</details>

<details><summary>Bag</summary>


</details>

<details><summary>Checkout & Checkout Success</summary>


</details>

<details><summary>Profile & Order History</summary>


</details>

<details><summary>FAQs</summary>


</details>

<details><summary>Contact</summary>


</details>

<details><summary>Site Management</summary>


</details>

<details><summary>Authentication</summary>


</details>




- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## User Stories Testing

The site was built from the outset with user stories at its core. The site was tested against each of the user stories, running through the steps a user would take to achieve their goal. The results can be found below.

| **No.** | **User type**             | **User Story**                                                                                                            | **How is it achieved**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------|---------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1  | As a general user         | I want to understand the purpose of the site immediately upon entering                                                    | The home page is the first place that a user will land and contains the logo of the site in the nav, a large hero image with bees on honeycomb, making it clear what the subject of the site is, a large shop now button making it clear it’s a shop and explanatory welcome text. The featured products on the home page also make it clear the kind of products the site sells.                                                                                                                                                                                                                                         |
| 1.2  | As a general user         | I want to be able to find what I need immediately and for the navigation to be easy to follow & intuitive                 | All pages contain a nav which is highly intuitive and had links which lead to the main pages of the site. There are also many user journeys that the site leads users on e.g. home -> products (with multiple ways to do this), products -> product details, product details -> add review, product details -> add to bag -> checkout -> checkout success. The footer also contains links to secondary pages such as FAQs and contact us.                                                                                                                                                                                 |
| 1.3  | As a general user         | I want to be able to use all features on the site on any device and for it to be fully responsive                         | All pages of the site have been designed and built to be fully responsive using a combination of Bootstrap classes and custom CSS, as well as thoroughly tested on multiple devices and browsers. All functionality works for all devices, no matter the screen size.                                                                                                                                                                                                                                                                                                                                                     |
| 1.4  | As a general user         | I want to be able to find answers to common questions                                                                     | The footer of the site contains a link to the FAQs page (this is a standard place for links to pages such as this so it is intuitive to find.) Users can then browse questions and click on them to see answers.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1.5  | As a general user         | I want to be able to contact the company with any questions or queries                                                    | The footer of the site contains a link to the contact us page (this is a standard place for links to pages such as this so it is intuitive to find.) Users can either fill in a form to contact the company or get in touch via post, phone or email, with the email and phone links being clickable to access call or email clients. Messages appear on the site management page with their status set to open so that site admins can see who has got in touch and respond accordingly.                                                                                                                                 |
| 1.6  | As a general user         | I want to be able to find the company on social media to find out more                                                    | The footer of the site contains links to social media sites which are clickable with a hover effect and open the relevant site in a new browser tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 1.7  | As a general user         | I want to be able to return to the main site without having to use the browser buttons if I end up on a non-existent page | If a user navigates to a page that doesn’t exist they arrive at a bespoke 404 page with brand styling and a ‘home’ button to take them back to the home page.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 1.8  | As a general user         | I want to get feedback when interacting with the site to know if my actions have been successful                          | The site implements Django’s ‘messaging’ functionality using Bootstrap ‘Toasts’ to provide user feedback at all times for all user actions. Users are informed of successful actions with a success message, a failed action with an error message, and a neutral action with an info message. The success message also includes a bag summary which appears when the user amends their bag contents.                                                                                                                                                                                                                     |
| 2.1  | As a shopper              | I want to be able to browse products easily, with options to filter & search to find what I need                        | Users can navigate to the products page in a number of ways, using the nav and various links across the site. There they can view products cards with summary information about the products. The products page allows users to filter products by category as well as by a search term that they input in the nav bar. Filters are easily reset using the ‘all products’ link. Users are informed about how many products they are seeing at all times. They also have the ability to sort products by rating, category, price and name.                                                                                 |
| 2.2  | As a shopper              | I want to be able to find out information about products                                                                  | Users can click on a product card to reach the product details page, this gives more information about a product as well as user reviews of that product to help a user find out more and make their purchasing decision. The product detail page is also available from various points around the site by clicking on the product image when it appears.                                                                                                                                                                                                                                                                 |
| 2.3  | As a shopper              | I want to see ratings & reviews of a product to know more about the quality and whether it's right for me                 | On the product details page users can scroll down to view product reviews. These all provide details about a user’s opinion on a product, they are sorted to put the highest rated reviews near the top to encourage users to buy the product but lower rated reviews are also visible. All reviews are approved by an admin to avoid inappropriate content appearing on the site. Every product has a rating which is the average of all the approved reviews.                                                                                                                                                           |
| 2.4  | As a shopper              | I want to be able to shop for multiple items at once, from across the site                                              | Users are able to add items to their shopping bag from across the site by storing the bag contents in the session cookie. This is all handled in the bag functionality, as long as the user doesn’t sign out of the site then this information will carry from page to page, allowing them to add multiple products.                                                                                                                                                                                                                                                                                                      |
| 2.5  | As a shopper              | I want to be able to add multiples of a single product to my bag at once                                                  | On the product details and bag pages users have the ability to add multiples of a single product to their bag, they are also able to amend that quantity in the bag page. If a user already has a product in their bag and they add another from the product detail page that product’s quantity is updated accordingly.                                                                                                                                                                                                                                                                                                  |
| 2.6  | As a shopper              | I want to be able to edit my shopping bag if I change my mind                                                             | Users are able to navigate to their shopping bag via the nav or bag summary message and edit the items. They can either input a number in to the quantity box or use the +/- buttons. They can then click ‘update’ to update the quantity and refresh the bag totals. They can also remove items by clicking ‘remove’.                                                                                                                                                                                                                                                                                                      |
| 2.7  | As a shopper              | I want to know what I will be charged for delivery                                                                        | On the bag page users can see what the delivery charge will be under the bag contents, broken down in the the total, delivery charge and grand total (which is the total + the delivery charge.) They are also informed how much more they need to spend to get free delivery (if they are under the threshold).                                                                                                                                                                                                                                                                                                           |
| 2.8  | As a shopper              | I want my payment and order to be fully secure and trustworthy                                                            | The site uses Stripe to process payments which has built in security. The site doesn’t receive any card information, that is all sent to Stripe securely. Stripe is a well established, respected payment provider with excellent security credentials.                                                                                                                                                                                                                                                                                                                                                                   |
| 2.9  | As a shopper              | I want to be able to set up an account to save my order history                                                           | Users can set up an account by navigating to the ‘register’ link in the accounts dropdown menu in the nav. There is also a link on the checkout page prompting users to sign up prior to purchasing to save their order information. All authentication is handled by Django allauth which has strong security and solid functionality for setting up an account.                                                                                                                                                                                                                                                           |
| 3.1  | As a user with an account | I want my account to be secure & easy to set up                                                                           | All site authentication is handled by Django allauth which has strong security and solid well-tested functionality for setting up an account. The process is very simple. Users navigate to register, provide email, username and password (with repetition to ensure accuracy). Users then need to verify their email by clicking on a link in an email they receive from the site before signing in with their new credentials. It is a quick and easy process.                                                                                                                                                         |
| 3.2  | As a user with an account | I want to see my order history                                                                                            | Users with an account can navigate to their profile page to view a list of their historic orders, which are clickable to provide more detailed information about that particular order.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3.3  | As a user with an account | I want to be able to update & save my personal information                                                                | On the profile page users are able to fill in a form to update their personal information including their name and their default delivery information. The profile page also provides links to pages where they can change their password and manage their email addresses. Users can also save their information when placing an order by checking the ‘update my profile’ checkbox in the checkout.                                                                                                                                                                                                                       |
| 3.4  | As a user with an account | I want to leave reviews of products I have purchased for the benefit of other customers                                   | Users who are logged in can navigate to the product details page and click ‘add review’ to add a review of that product. They need to provide a title, content and a rating using a simple clickable rating (an alternative input is provided for screen readers to make it fully accessible.) This review is then sent for approval but visible on the user’s profile page in the mean time for them to view, edit or delete.                                                                                                                                                                                            |
| 3.5  | As a user with an account | I want to be able to edit my reviews                                                                                      | Users can edit their own reviews by clicking on the EDIT button anywhere the review appears. This will take them to a pre-populated review form which can be easily edited. After editing a review will be sent back for approval to the site admins.                                                                                                                                                                                                                                                                                                                                                                       |
| 3.6  | As a user with an account | I don't want admins or other customers to be able to change my reviews                                                    | Site admins cannot edit reviews, only delete them or approve them. This stops the site admins from changing negative reviews to positive ones. This helps to show that the company values their customers’ opinions and builds trust.                                                                                                                                                                                                                                                                                                                                                                                     |
| 4.1  | As an admin of the site   | I want to be able to add & edit products                                                                                  | Site admins can navigate to the site management page to add a product using the ADD PRODUCT button which takes them to a form where they can add all the details about the product including. This information can be edited by navigating to that product’s details page and clicking on EDIT.                                                                                                                                                                                                                                                                                                                             |
| 4.2  | As an admin of the site   | I want to be able to remove products from sale                                                                            | Site admins can remove any product from sale by clicking on DELETE on the product details page. If the product has never been sold they are able to delete it. If it has been sold this will instead mark the product as discontinued and remove it from sale but leave it on the database. This means that the order history of the online store is preserved (removing the product would remove it from historic orders too.) Admins can also edit any product and change it to ‘discontinued’ on the edit product form. They can also go to the admin panel and uncheck discontinued to add it back to the site later on. |
| 4.3  | As an admin of the site   | I want to view & filter customer messages and manage whether they need further action                                     | Site admins can access the site management page which has a messaging dashboard showing all customer messages sent using the contact us form. The messages are styled by the status of ‘open’ or ‘closed’ and they filterable using buttons above the messages. Admins can toggle a message’s status using a simple toggle switch.                                                                                                                                                                                                                                                                                          |
| 4.4  | As an admin of the site   | I want to approve customer reviews before they go live & delete any with inappropriate content only                       | Site admins can access the site management page to view any reviews which are unapproved. These messages are automatically marked as ‘unapproved’ when they are added or updated by a user. Admins can approve a review using a simple toggle switch. They can also delete reviews from here if they contain inappropriate content.                                                                                                                                                                                                                                                                                         |
| 4.5  | As an admin of the site   | I want to be able to update the site FAQs                                                                                 | On the FAQs page site admins have functionality to add, edit and delete FAQs using the ADD FAQ button and each FAQ’s EDIT/DELETE buttons.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 4.6  | As an admin of the site   | I want all the admin controls to be quick and easy to find and use                                                        | The site management page gives site admins a single point to access the main site management controls including adding products, navigating to the FAQs page to update them, navigating to the Django admin panel for more complex administrative tasks, seeing and toggling the status of customer messages and approving user reviews.                                                                                                                                                                                                                                                                                  |



### User Stories Testing Screen Recordings / Images

#### As a General User...


<details><summary>1.1: I want to understand the purpose of the site immediately upon entering</summary>



https://github.com/emmahewson/island-bees/assets/116887840/b619ac4f-28eb-4cce-a394-2ba86ac13b9f



</details>


<details><summary>1.2: I want to be able to find what I need immediately and for the navigation to be easy to follow & intuitive
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/a7c744bf-d28a-4b9d-9d4a-b38a6ee1ba7a


</details>

<details><summary>1.3: I want to be able to use all features on the site on any device and for it to be fully responsive</summary>



https://github.com/emmahewson/island-bees/assets/116887840/7d281cf6-b00a-4552-a3b0-ab1bcbc0b168


</details>

<details><summary>1.4: I want to be able to find answers to common questions
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/ccae7869-2909-4656-ac5b-5c538a0635b3


</details>

<details><summary>1.5: I want to be able to contact the company with any questions or queries
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/4af9daa6-1cfb-40f8-b595-df38d9cbdd03


</details>

<details><summary>1.6: I want to be able to find the company on social media to find out more
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/aedae15b-b638-4552-9fe2-3ebf44483c59


</details>

<details><summary>1.7: I want to be able to return to the main site without having to use the browser buttons if I end up on a non-existent page
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/b0cd0113-681f-4b97-9a37-14ac0f795631


</details>

<details><summary>1.8: I want to get feedback when interacting with the site to know if my actions have been successful
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/ee50dff5-43d2-428b-9ebb-99ad21eaabcc



</details>

#### As a Shopper...


<details><summary>2.1: I want to be able to browse products easily, with options to filter & search to find what I need
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/690452d5-091f-4050-b54e-b6709dc698fa



</details>

<details><summary>2.2: I want to be able to find out information about products
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/9e522065-e8ec-4ca5-8cbd-85314b7de0fd


</details>

<details><summary>2.3: I want to see ratings & reviews of a product to know more about the quality and whether it's right for me
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/f9a4a14f-4fc6-46f8-a308-290831982f05


</details>


<details><summary>2.4: I want to be able to shop for multiple items at once, from across the site
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/a705c3d0-0656-45f4-a8e8-873e3b442242


</details>

<details><summary>2.5: I want to be able to add multiples of a single product to my bag at once
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/1f62c0d1-ec10-44ab-87fc-ded1997fd2ae



</details>

<details><summary>2.6: I want to be able to edit my shopping bag if I change my mind
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/5dd67ef6-1a9f-48a4-bc90-50b9613feca2



</details>

<details><summary>2.7: I want to know what I will be charged for delivery
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/94210b62-89d2-4d40-b54f-c6c4762a91c3



</details>

<details><summary>2.8: I want my payment and order to be fully secure and trustworthy
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/9b659047-466d-4d64-9730-38eea8a2b842


</details>

<details><summary>2.9: I want to be able to set up an account to save my order history
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/ce6923d5-0773-4d8e-b3fa-5283345cbc9c



</details>

#### As a user with an account...


<details><summary>3.1: I want my account to be secure & easy to set up
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/822129d6-9a2c-4118-a15f-da1f2c9f3ba5


</details>

<details><summary>3.2: I want to see my order history
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/cd5b5659-b080-4c16-8bc3-e276217d2bba



</details>

<details><summary>3.3: I want to be able to update & save my personal information
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/9e92fee7-bce8-4e6b-852b-cb1ce2e3257a



</details>

<details><summary>3.4: I want to leave reviews of products I have purchased for the benefit of other customers
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/d45de283-3a92-448e-80d6-32dcd9b20867


</details>


<details><summary>3.5: I want to be able to edit my reviews
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/c3e8f94e-7236-4d8b-a987-fe1fb1b29f62


</details>

<details><summary>3.6: I don't want admins or other customers to be able to change my reviews
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/685facb5-57ea-42e2-807b-c2cdf3e5527d


</details>

#### As an admin of the site...

<details><summary>4.1: I want to be able to add & edit products
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/3eb7c7d1-0ed3-46a5-9d8b-b30dad708191



</details>

<details><summary>4.2: I want to be able to remove products from sale
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/cd02ad3f-3ba1-4eca-9aef-23dba5f5fe1b



</details>

<details><summary>4.3: I want to view & filter customer messages and manage whether they need further action
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/f1cab167-d25d-4ab5-9c97-08d86674c936



</details>

<details><summary>4.4: I want to approve customer reviews before they go live & delete any with inappropriate content only
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/c5c6b38e-5c68-4f47-bf39-cbed611b8cb2



</details>

<details><summary>4.5: I want to be able to update the site FAQs
</summary>


https://github.com/emmahewson/island-bees/assets/116887840/80e3f530-6989-4d70-a4bf-1f865503efaa



</details>

<details><summary>4.6: I want all the admin controls to be quick and easy to find and use
</summary>



https://github.com/emmahewson/island-bees/assets/116887840/d2503e0b-2ee0-449c-a204-c47e31914644


</details>




- - -
[Go to Top](#island-bees---e-commerce-site)
- - -


## Bugs & Fixes

I encountered the following significant or interesting bugs during development. All of these were fixed and I am unaware of any remaining bugs on the site.

#### Bug 1 - Remove Bag Item JS - move to external JS file

**Issue:** I attempted to move the JavaScript for the remove item from bag in to an external static file - update worked ok but remove didn't work once in the external file. I was not able to work out why this behaved in this way.

**Fix:** Put back in to HTML file as a script tag.

#### Bug 2 - Checkout delivery & total calculations - type errors

**Issue:** The checkout delivery & total calculations threw an error about not being able to add a float & a decimal type numbers together. 

**Fix:** Had to convert the order_total and total_delivery_chargeable to float values with checks to make sure they had a value in the first place. This accounted for the various different scenarios.
1. Under delivery threshold & delivery chargeable on all products
2. Under delivery threshold & delivery changeable on some but not all products
3. Over delivery threshold


#### Bug 3 - Save Info checkbox on checkout form not working properly

**Issue:** The save info checkbox on the checkout was saving the form information regardless of whether the checkbox was selected or not.

**Fix:** After a lot of testing and research I found out the problem was stemming from 2 places:
1. In stripe_elements.js there was an issue with the JQuery assignment of the Boolean value and the value being sent to the post_data was always true no matter whether the checkbox was selected or not. I couldn't pin point exactly why it was behaving like this but I was able to solve it by assigning the value using vanilla JavaScript.

    - Original Code: `var saveInfo = Boolean($('#id-save-info').attr('checked'));`
    - Final Working Code: `var saveInfo = document.getElementById('id-save-info').checked`

2. Even after changing the above code I found that the profile details were still being saved when the box was unchecked. With the help of this [post](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1605302104469800?thread_ts=1605222094.452700&cid=C7HS3U3AP) on the Code Institute Slack Channel I discovered that the problem was related to code in webhook_handler.py which checked if save_info was true. Rather than now returning a Boolean value from the new JS code it was returning a string of "true" or "false" - which meant that when checking if save_info: it was always returning True because it always had contents. I fixed the issue by changing this code to check for a string instead.

- Original Code:

```
save_info = intent.metadata.save_info
if save_info:
    # code to update userProfile based on data
```

- Final Working Code

```
save_info = intent.metadata.save_info
if save_info == "true:
    # code to update userProfile based on data
```

#### Bug 4 - Toast showing shopping bag summary after user actions not related to shopping bag

**Issue:** This was more of a user experience issue than a bug. I had followed the Boutique Ado walkthrough for the Toasts & user feedback messages and whilst the little shopping bag summary was a great touch it was showing after every successful user action apart from on the profile page where there was code to stop this happening. I needed to find a more comprehensive way to hide the summary when users added reviews, FAQs, filled in the Contact Us form etc.

**Fix:** I removed it by firstly adding an additional conditional statement to the message_success template to check whether the referring page url contained the word 'accounts' to stop the bag showing when any messages.success were called by the built-in allauth code. Then in addition, I added a session variable called show_bag_summary to true or false each time I called messages.success and an additional conditional value in the template tag to check this value: 

`{% if grand_total and request.session.show_bag_summary and "accounts" not in request.META.HTTP_REFERRER %}`
    

#### Bug 5 - Label styling on Django Form Checkboxes - add product

**Issue:** I wanted to have different styling on the labels for the text & textarea labels compared to the checkbox labels. I couldn't find a way to add class attributes to the labels themselves within the forms.py logic or by using template logic.

**Fix:** I separated the fields out to individual tags and styled them in this way. However I discovered that this had the unintended result of not showing any form error messages e.g. if the price had too many digits. I got around this by explicitly including the error messages below the labels as separate tags:
```
{{ form.category.label_tag }}
{{ form.category }}
{% for error in form.category.errors  %}
    <span class="text-ib-warning weight-semibold ib-lh-2">{{error}}</span>
{% endfor %}
```

#### Bug 6 - Products page wouldn't load after deployment

**Issue:** After initial deployment my products page wouldn't load and returned a 400 error.

**Fix:** I turned debug back on in the deployed site and discovered that it couldn't load the sort_box.js file and was throwing up a suspicious operation error and blocking the page. I fixed this error with the help of this [Slackoverflow Post](https://stackoverflow.com/questions/43529912/suspicious-operation-attempted-access-to-denied-while-loading-static-files) by removing the leading '/' on the script tag in the template.


<details><summary>Screenshots</summary>
    <img src="media/docs/docs_bug_6.jpg">
</details>

#### Bug 7 - Checkout creating duplicate orders

**Issue:** Whilst initially working correctly I found that my checkout began to create duplicates when placing an order - one in the view and another in the webhook.

**Fix:** After extensive research and testing using print statements I discovered that the problem was at the point where the webhook searches for the order in the database and if it didn't find it, creates the order. The problem stemmed from the form fields which were not required and so could be empty - phone number and street address 2. I fixed the problem by removing these fields from the search parameters in the webhook query.

<details><summary>Screenshots</summary>
    <img src="media/docs/docs_bug_7.jpg">
</details>

#### Bug 8 - Deleting Products with associated OrderLineItems

**Issue:** When attempting to delete a product that is linked to a previous order as a line item in the OrderLineItem model it throws an error because, due to the CASCADE setting on the field, by deleting the product you are also then deleting all references to it. This posed a problem because I wanted to give superusers the ability to delete a product to remove it from sale, but keeping all old order information is also very important.

**Fix:** I solved this problem with an idea from this CI Slack channel [post](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1598004199059700?thread_ts=1597961336.047800&cid=C7HS3U3AP) by stopping store owners deleting products using model.PROTECT on the OrderLineItem foreign key field but allowing them to remove them from sale with a 'discontinued' Boolean field. This meant additional changes had to be made to the site to ensure smooth running and good user experience:
- added a conditional check to the delete_product view to see if the product appears on any OrderLineItems and if so rather than deleting it, to mark it as 'discontinued'
- Dynamically changing the text in the delete product modal depending on whether the product has associated OrderLineItems and if so removing the ability to delete it and offering the admin the chance to 'discontinue' it instead.
- Only displaying cards products that are not 'discontinued' on the products & home pages
- Adding a check on the product_detail view to redirect users who link to a discontinued product directly using the url or back button
- Adding an additional field to the add/edit product form to mark a product as 'discontinued'
- Removing the edit/delete buttons from the product cards to improve user experience and keep the site logic as simple and bug free as possible
- When a form is submitted with the 'discontinue' input checked, if that product is in the shopping bag, remove it.
- Added a conditional check on the add_to_bag view to only add it if the product is not discontinued.

#### Bug 9 - Broken Image Links show icon rather than backup no-image

**Issue:** Broken image links showing when image is missing, rather than the 'no-image' backup which provides a better user experience. This also meant that if there was an error getting the product image the product cards were hard to click on to link to the product detail page as the image is the link element.

**Fix:** I added an 'onerror' to the image tags to show the no-image if there was an error displaying the image.

`onerror="this.onerror=null;this.src='{{ MEDIA_URL }}no_image.jpg'"`

<details><summary>Screenshots</summary>
    <img src="media/docs/docs_bug_9.jpg">
    <img src="media/docs/docs_bug_9b.jpg">
</details>


#### Bug 10 - No feedback on AllAuth forms with error

**Issue:** When using the AllAuth forms to login, register, change email etc there was no feedback to the user when the form failed verification e.g. if an email address already existed on another account, and the page would reset with no indication of whether it had worked or not. I had used the AllAuth forms as provided and had simply adapted the styling to make it look like the rest of the site.

**Fix:** I added the error messages for each input as separate template tags with bespoke styling as I had done with the other forms using the following syntax:

```
{% for error in form.email.errors  %}
    <span class="text-ib-warning weight-semibold d-block mb-1">{{error}}</span>
{% endfor %}
```

**Additional Fix:** For the login form I discovered that the error messages weren't showing as the errors were linked to the whole form rather than the individual fields, I found the answer to this problem [here](https://stackoverflow.com/questions/39183479/django-all-auth-form-errors-not-displaying) and added code to display the whole form errors. I added this to the other forms too to make sure that all errors were displayed.

```
{% if form.errors %}
    {% for error in form.non_field_errors %}
        <span class="text-ib-warning weight-semibold d-block mb-1">{{error}}</span>
    {% endfor %}
{% endif %}
```

#### Bug 11 - Non logged in user placing order with invalid payment info - failure in validation

**Issue:** During testing I discovered that if a non-logged in user attempted to place an order with incomplete or incorrect card details that the form validation didn't work properly, the loading animation appeared but the user wasn't being sent back to the checkout with an error message about the form and so they were stuck on the loading page with no indication of whether their order had gone through.

**Fix:** I realised that this issue must stem from something that was unique to logged-out users as it was working correctly for logged-in users. Using logic and the console I narrowed it down to an error in getting the value of the 'saveInfo' box which, for logged out users, had been hidden and the stripe_elements.js was unable to progress to the stage of returning the user to the form to correct the error. I fixed this by putting the code in a try/catch block which set the value explicitly to false if the attempt to find the value failed.

```
var saveInfo;
try {
    saveInfo = document.getElementById('id-save-info').checked;
}
catch(err) {
    saveInfo = false
}
```

#### Bug 12 - Search bar dropdown on medium and smaller screens has glitch in animation

**Issue:** When the searchbar dropdown is triggered there is a glitch in the styling, the bar has grey padding at the sides initially which then disappears.

**Fix:** I attempted to resolve this issue using various CSS techniques but as it has been built using a combination of Bootstrap styling and bespoke CSS I have been unable to find the cause of the glitch. As this is purely an aesthetic issue and not a problem with functionality I have left it as it is, so this is a remaining bug.


#### Bug 13 - Bag quantity input doesn't validate max & min values

**Issue:** During testing I noticed that whilst the product detail page input worked exactly as expected with the max/min values (0-99), on the bag page the user was able to enter a value higher than 99 and successfully update their bag. This could feasibly cause problems with large numbers in the order process as the totals on the orders are limited by the number of digits.

**Fix:** I worked out that this was because the form submission was handled differently in the bag than with the product details input. Rather than being handled by a submit button it was being controlled with JavaScript, which meant the front end validation didn't work. I solved this by putting an if statement in to the 'adjust_bag' view to check if the value was over 99, or under 0 (to avoid negative numbers) and if so returning the user to the page with an error message and not updating the bag until the value was within the accepted range.

```
quantity = int(request.POST.get('quantity'))

if quantity > 99 or quantity < 0:
    messages.error(
        request, "Please enter a value betweeen 0-99, " +
        "quantity has not been updated.")
    return redirect(reverse('view_bag'))

else:
# Code to update bag...

```


#### Bug 14 - Various styling issues on mobile

**Issue:** During testing on a mobile (rather than dev tools mobile emulator) I discovered that some of the site styling was being over-ridden by the mobile browers on both Safari and Chrome. This included form inputs (the inner shadow and the dropdowns had lost their styling), the FAQs accordian question styling & the products sort selector.

**Fix:** I fixed these by adding explicit CSS styling to elements, including adding the -webkit-appearence to 'none' to over-ride the browser styling.


#### Bug 15 - Site Management - messages scroll on mobile not working

**Issue:** During device testing I discovered that the JavaScript I had written to save the scroll position on the site management page wasn't working on mobile. The page would scroll to the top on reload, either when clicking on a filter or on a message toggle. No console errors were logged and the page behaved correctly otherwise.

**Fix:** I did some investigation in to this issue but I was unable to come up with a solution within the timeframe I had to complete the project, so this is a remaining bug.


- - -


### Known & Remaining Bugs

All information about remaining bugs is included in the information above. Click on the links below to find out more details:

[Bug 12: Search bar dropdown on medium and smaller screens has glitch in animation](#bug-12---search-bar-dropdown-on-medium-and-smaller-screens-has-glitch-in-animation)

[Bug 15 - Site Management - messages scroll on mobile not working](#bug-15---site-management---messages-scroll-on-mobile-not-working)


- - -

[Go to Top](#island-bees---e-commerce-site)

- - -
