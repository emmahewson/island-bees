from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from django.contrib.auth.models import User
from .models import Review
from products.models import Product
from .forms import ReviewForm


@login_required()
def add_review(request, product_id):
    """
    Renders form to add review.
    Logged in Users Only (redirects to log in).
    Adds new review to database.
    """

    # Checks user is logged in - redirects to log in
    if not request.user.is_authenticated:
        messages.error(request,
                       'You need to be logged in to leave a review, sorry!')
        return redirect(reverse('account_login'))

    # Sets product based on product_id
    product = Product.objects.get(id=product_id)

    # Sets author based on current user
    author = User.objects.get(username=request.user)

    # Handles Form Submission
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = author
            review.save()

            # Updates product rating on product object
            product.rating = round(
                product.reviews.aggregate(Avg('rating'))['rating__avg'])
            product.save()

            messages.success(request, "New product review added.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Form invalid, please try again.")

    # Handles View Rendering
    else:
        form = ReviewForm()

    # Sets page template
    template = 'reviews/add_review.html'

    # Sets current product & form content
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
