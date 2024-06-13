from django.shortcuts import render
from django.views.generic import ListView,DetailView

# Create your views here.
from app.models import *
from django.http import HttpResponse

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(school_name='maxtonhall')
    #ordering=['school_name']

# def greet(request,n,u):
#     return HttpResponse(f'Hai {n} How are U {u}')

class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'