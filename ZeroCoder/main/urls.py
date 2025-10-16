from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='new'),
    path('new2', views.new2, name='new2'),
    path('new3', views.new3, name='new3'),
    path('data', views.data),
    path('test', views.test),
    
]
