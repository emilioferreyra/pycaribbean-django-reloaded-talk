from django.shortcuts import render
from products.models import Offer


def home(request):
    title = 'Welcome to DMS'
    offers = Offer.objects.filter(active=True).order_by('-id')[:6]
    context = {'title': title, 'offers': offers}
    return render(request, 'index.html', context)
