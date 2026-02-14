from django.shortcuts import render
from django.http import HttpResponse
from .models import product


def index(request):
    products = product.objects.all()  # main page view
    return render(request, 'index.html', {'products': products})


def new(request):  # main page view
    return HttpResponse("new products")
