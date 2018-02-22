from django.shortcuts import render
from products.models import Offer
from pages.models import Page


def home(request):
    title = 'Welcome to DMS'
    offers = Offer.objects.filter(active=True).order_by('id')[:6]
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
