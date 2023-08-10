from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg


from django.contrib.auth.models import User
from .models import Review
from products.models import Product
from .forms import ReviewForm


def add_review(request, product_id):
    """
    Renders form to add review.
    Adds new review to database.
    """

    if request.user:
        author = User.objects.get(username=request.user)
    else:
        author = "Anonymous"

    product = Product.objects.get(id=product_id)
    print(product.id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = author
            review.is_featured = True if review.rating > 3 else False
            review.save()

            print(product.rating)

            # Update product rating
            product.rating = round(
                product.reviews.aggregate(Avg('rating'))['rating__avg'])
            product.save()

            print(product.rating)

            messages.success(request, "New product review added.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Form invalid, please try again.")
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
