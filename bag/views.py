from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    # Tells toast message which page user is on
    # To set toast bag summary button link
    context = {
        'on_bag_page': True
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Gets product from DB
    product = get_object_or_404(Product, pk=item_id)

    # Gets quantity value from form
    quantity = int(request.POST.get('quantity'))

    # Gets URL to redirect user back to previous page
    redirect_url = request.POST.get('redirect_url')

    # Gets bag from session
    bag = request.session.get('bag', {})

    # Checks if product is already in bag
    # If so updates quantity & if not adds to bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        request.session['show_bag_summary'] = True
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}'
        )
    else:
        bag[item_id] = quantity

        request.session['show_bag_summary'] = True
        messages.success(request, f'Added {product.name} to your bag')

    # Updates bag in session
    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    # Gets product from DB
    product = get_object_or_404(Product, pk=item_id)

    # Gets quantity value from form
    quantity = int(request.POST.get('quantity'))

    if quantity > 99 or quantity < 0:
        messages.error(
            request, "Please enter a value between 0-99, " +
            "quantity has not been updated.")
        return redirect(reverse('view_bag'))

    else:
        # Gets bag from session
        bag = request.session.get('bag', {})

        # Checks if quantity is more than 0
        # If so updates quantity
        # If not removes item from bag
        if quantity > 0:
            bag[item_id] = quantity
            request.session['show_bag_summary'] = True
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            request.session['show_bag_summary'] = True
            messages.success(request, f'Removed {product.name} from your bag')

        # Updates bag in session
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        # Gets product from DB
        product = get_object_or_404(Product, pk=item_id)

        # Gets bag from session
        bag = request.session.get('bag', {})

        # Removes item id from bag
        bag.pop(item_id)
        request.session['show_bag_summary'] = True
        messages.success(request, f'Removed {product.name} from your bag')

        # Updates bag in session
        request.session['bag'] = bag
        return HttpResponse(status=200)

    # Handles errors
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
