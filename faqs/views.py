from django.shortcuts import render
from products.models import Product


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