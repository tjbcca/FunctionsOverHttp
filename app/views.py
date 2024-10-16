from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
def hello_name(request, name):
    return HttpResponse("Hello " + (name.upper()) + "!")
def age(request, end, birthyear):
    return HttpResponse(int(end) - int(birthyear))
def food(request, burgers, fries, drinks):
    total = ((float(burgers) * 4.5) + (float(fries) * 1.5) + (float(drinks) * 1))
    return HttpResponse(str("{:.2f}".format(total)))