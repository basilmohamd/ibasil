from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def grew(request):
    return render(request,"home.html")