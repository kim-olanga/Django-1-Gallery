from django.urls import path
from . import views

#create paths
urlpatterns=[
    path('',views.welcome,name = 'welcome'),
]