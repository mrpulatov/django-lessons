from django.shortcuts import render
from django.http import HttpResponse

def cal():
    x = 1
    y = 2
    return x + y

# Create your views here.
def say_hello(request):
    x = cal()
    return render(request, 'hello.html', {'number': x})