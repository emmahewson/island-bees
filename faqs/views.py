from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Faq
from .forms import FaqForm


def faqs(request):
    """
    A view to return the FAQs
    """

    # Gets faqs from DB for featured faqs section
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

    # Sets current faq & form content
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """ Edit a FAQ """

    # Checks user is superuser
    # redirects to FAQS if not
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can edit FAQS.')
        return redirect(reverse('faqs'))

    # Get faq from DB
    faq = get_object_or_404(Faq, pk=faq_id)

    # Handle Form Submission
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=faq)

        if form.is_valid():
            form.save()

            request.session['show_bag_summary'] = False
            messages.success(request, 'Successfully updated FAQ!')

            # Redirects to 'faqs'
            return redirect(reverse('faqs'))

        else:
            messages.error(
                request, 'Failed to update FAQ. Please check the form.')

    # Handles View Rendering
    else:
        form = FaqForm(instance=faq)
        messages.info(request, f'You are editing {faq.question}')

    # Sets page template
    template = 'faqs/edit_faq.html'

    # Sets current faq & form content
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a FAQ """

    # Checks user is superuser
    # redirects to FAQS if not
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can delete FAQS.')
        return redirect(reverse('faqs'))

    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    message = 'FAQ deleted!'

    messages.success(request, message)
    return redirect(reverse('faqs'))
