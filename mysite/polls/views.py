<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
>>>>>>> 23a1c38d477b787d7a5c9b1e340f92341a2f5aa6
