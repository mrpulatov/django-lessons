from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# url conf
urlpatterns = [
    path('hello/', views.say_hello)
]