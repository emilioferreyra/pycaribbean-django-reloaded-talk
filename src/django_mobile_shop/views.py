# Django core
from django.shortcuts import render
from django.utils import timezone

from pages.models import Page
# My apps
from products.models import Offer


def home(request):
    title = 'Welcome to DMS'
    now = timezone.now()
    offers = Offer.objects.filter(start_date__lte=now, expiration_date__gte=now).order_by('-id')[:6]

    for o in offers:
        if o.start_date <= now <= o.expiration_date:
            Offer.objects.filter(pk=o.id, active=False).update(active=True)
        else:
            Offer.objects.filter(pk=o.id, active=True).update(active=False)

    context = {'title': title, 'offers': offers}
    return render(request, 'index.html', context)


def about(request):
    get_about = Page.objects.get(title='About')
    title = get_about.title
    content = get_about.content
    context = {'title': title, 'content': content}
    return render(request, 'about.html', context)


def contact(request):
    get_about = Page.objects.get(title='Contact')
    title = get_about.title
    content = get_about.content
    context = {'title': title, 'content': content}
    return render(request, 'about.html', context)


def services(request):
    get_about = Page.objects.get(title='Services')
    title = get_about.title
    content = get_about.content
    context = {'title': title, 'content': content}
    return render(request, 'about.html', context)
