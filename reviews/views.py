from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse

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

    # Sets product based on product_id
    product = get_object_or_404(Product, pk=product_id)

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
            if product.reviews.filter(is_approved=True).count() > 0:
                product.rating = round(
                    product.reviews.filter(is_approved=True).aggregate(
                        Avg('rating'))['rating__avg'])
            else:
                product.rating = 0
            product.save()

            request.session['show_bag_summary'] = False
            messages.success(
                request,
                "Your review has been created. " +
                "It will appear on the site once it has been approved. " +
                "You can see your review on your profile page until then. " +
                "We value your feedback and only " +
                "reject reviews with inappropriate content."
            )

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


@login_required()
def edit_review(request, review_id):
    """
    Renders form to edit review.
    Logged in Users Only (redirects to log in).
    Updates review on database.
    """

    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.filter(reviews=review)[0]

    # Checks user is author of review
    # redirects to product detail if not
    if request.user != review.user:
        messages.error(request, 'You can only edit your own reviews.')
        return redirect(reverse('product_detail', args=[product.id]))

    # Handles Form Submission
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)

        if form.is_valid():
            review = form.save()
            review.is_approved = False
            review.save()

            # Gets URL to redirect user back to previous page
            redirect_url = request.POST.get('redirect_url')

            # Updates product rating on product object
            if product.reviews.filter(is_approved=True).count() > 0:
                product.rating = round(
                    product.reviews.filter(
                        is_approved=True).aggregate(
                            Avg('rating'))['rating__avg'])
            else:
                product.rating = 0
            product.save()

            request.session['show_bag_summary'] = False
            messages.success(
                request,
                "Your review has been updated. " +
                "It will appear on the site once it has been approved. " +
                "You can see your review on your profile page until then. " +
                "We value your feedback and only " +
                "reject reviews with inappropriate content."
            )
            return redirect(redirect_url)
        else:
            messages.error(request, "Form invalid, please try again.")

    # Handles View Rendering
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing... "{review.title}"')

    # Sets page template
    template = 'reviews/edit_review.html'

    # Sets current product & form content
    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review """

    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.filter(reviews=review)[0]

    # Gets the previous page URL for redirect
    next = request.GET.get('next', '')

    # Checks user is author of review or superuser
    # redirects to product detail if not
    if not request.user.is_superuser:
        if request.user != review.user:
            messages.error(request, 'You can only delete your own reviews.')
            return redirect(reverse('product_detail', args=[product.id]))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()

    # Updates product rating on product object
    if product.reviews.filter(is_approved=True).count() > 0:
        product.rating = round(
            product.reviews.filter(
                is_approved=True).aggregate(Avg('rating'))['rating__avg'])
    else:
        product.rating = 0
    product.save()

    request.session['show_bag_summary'] = False
    messages.success(request, 'Review successfully deleted!')
    return redirect(next)


@login_required
def toggle_review(request, review_id):
    """
    A View to toggle the approved status of the review
    """

    # Checks user is superuser
    # redirects to home if not
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    try:
        # Gets the review from DB
        review = get_object_or_404(Review, id=review_id)

        # Gets value of hidden input
        review_approved = request.POST.get('is_approved')

        # Sets value of is_approved field on DB
        if review_approved == "True":
            review.is_approved = True
        else:
            review.is_approved = False
        review.save()

        # Updates product rating on product object
        product = Product.objects.filter(reviews=review)[0]

        if product.reviews.filter(is_approved=True).count() > 0:
            product.rating = round(
                product.reviews.filter(
                    is_approved=True).aggregate(Avg('rating'))['rating__avg'])
        else:
            product.rating = 0
        product.save()

        messages.success(
            request,
            "Review approved successfully. " +
            "The review will now appear on the product page. " +
            "You can update the approval status " +
            "of the review in the admin area if required."
        )
        return redirect(reverse('manage'))

    # Handles errors
    except Exception as e:
        messages.error(
            request,
            'Sorry, the review status could not be updated. ' +
            'Please try again later.'
        )
        return HttpResponse(content=e, status=400)
