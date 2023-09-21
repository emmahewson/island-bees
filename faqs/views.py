from django.shortcuts import render
from .models import Faq


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
