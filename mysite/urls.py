from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
]
