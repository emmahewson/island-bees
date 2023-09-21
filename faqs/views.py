from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Faq
from .forms import FaqForm


def faqs(request):
    """
    A view to return the FAQs
    """

    # Gets faqs from DB for featured products section
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
    }

    return render(request, 'faqs/faqs.html', context)


@login_required()
def add_faq(request):
    """
    Renders form to add FAQ.
    Admin (Superuser) Only (redirects to log in).
    Adds new faq to database.
    """

    # Checks user is superuser
    # redirects to faqs if not
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add FAQs.')
        return redirect(reverse('faqs'))

    # Handles Form Submission
    if request.method == "POST":
        form = FaqForm(request.POST)

        if form.is_valid():
            form.save()

            request.session['show_bag_summary'] = False
            messages.success(request, "New FAQ added.")
            return redirect(reverse('faqs'))
        else:
            messages.error(request, "Form invalid, please try again.")

    # Handles View Rendering
    else:
        form = FaqForm()

    # Sets page template
    template = 'faqs/add_faq.html'

    # Sets current product & form content
    context = {
        'form': form,
    }

    return render(request, template, context)
