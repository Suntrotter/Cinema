from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from .models import Movies, Customer



#@api_view(['GET'])
def home(request):
    return render(request, 'home.html')
    #return Response("This is the homepage")

def see_all_movies(request):
    queryset = Movies.objects.all()
    context = {
        'movies': queryset
    }
    return render(request, 'movies.html', context)

def see_one_movie(request, slug):
    queryset = models.Movies.objects.get(slug = slug)
    context = {
        'movie': queryset
    }
    return render(request, 'one_movie.html', context)

def see_all_customers(request):
    queryset = Customer.objects.all()
    context = {
        'customer': queryset
    }
    return render(request, 'customers.html', context)

def see_one_customer(request, slug):
    queryset = models.Customer.objects.get(slug = slug)
    context = {
        'client': queryset
    }
    return render(request, 'one_customer.html', context)







