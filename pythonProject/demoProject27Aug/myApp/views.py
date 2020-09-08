from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_function(request):
    return render(request, "form.html", { })

def accessIndexFun(request):
    return render(request, "index.html", { })