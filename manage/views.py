from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Message
# from .forms import MessageForm


@login_required
def manage(request):
    """
    A view to return the Site Management Page
    """

    # Checks user is superuser
    # redirects to home if not
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can access that page.')
        return redirect(reverse('home'))

    # Gets messages from DB
    customer_messages = Message.objects.all()
    context = {
        'customer_messages': customer_messages,
    }

    return render(request, 'manage/manage.html', context)
