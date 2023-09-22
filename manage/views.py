from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Message
# from .forms import MessageForm


def manage(request):
    """
    A view to return the Site Management Page
    """

    # Gets messages from DB
    messages = Message.objects.all()
    context = {
        'messages': messages,
    }

    return render(request, 'manage/manage.html', context)
