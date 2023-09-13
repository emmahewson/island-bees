Notes

Bug - attempted to move the js for the remove item from bag in to separate JS file - update worked ok but remove didn't. Put back in to HTML as a script tag.

Bug - bag appears in toast after review updated or added - not sorted

Bug - issues with the checkout delivery & total calculations - couldn't add a float & a decimal type numbers. 
Fix - Had to convert the order_total and total_delivery_chargable to float values with checks to make sure they had a value in the first place. This accounted for the various different scenarios.
    1. Under delivery threshold & delivery chargable on all products
    2. Under delivery threshold & delivery chargable on some but not all products
    3. Over delivery threshold

Mention - using widget-tweak to add style classes to the form inputs in teh auth templates
