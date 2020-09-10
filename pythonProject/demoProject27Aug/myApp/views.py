from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import DBConnection


def my_function(request):
    return render(request, "form.html", {})


def accessIndexFun(request):
    return render(request, "index.html", {})


def dbView(request):
    # object_obj = DBConnection(name="sovan",email="abc@gmail.com")
    # object_obj.save()
    DBConnection.objects.all().delete()
    return render(request, "db.html", {"object_obj": "object_obj"})
