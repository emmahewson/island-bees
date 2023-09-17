from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from checkout.models import Order
from reviews.models import Review

from .models import UserProfile
from .forms import UserProfileForm, UserForm


@login_required
def profile(request):
    """
    Displays the user's profile, order history & user reviews
    Updates the User Profile Model via form
    Updates the User Model via form
    """
    # Gets user information from database
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)

    # Handles POST request (form submission)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        user_form = UserForm(request.POST, instance=profile)

        # Updates the UserProfile & User Models
        if profile_form.is_valid():
            instance = profile_form.save(commit=False)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            instance.save()
            request.session['show_bag_summary'] = False
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')

    # Handles GET request (populates page)
    else:
        # Populates the forms with the model data
        profile_form = UserProfileForm(instance=profile)
        user_form = UserForm(instance=user)

    # Gets all user's orders from DB
    orders = profile.orders.all().order_by('-date')

    # Gets all user's reviews from DB
    reviews = profile.user.reviews.all().order_by('-created_on')

    template = 'profiles/profile.html'
    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'orders': orders,
        'reviews': reviews,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ Displays the order history using the checkout_success template """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
