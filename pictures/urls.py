from django.urls import path
from . import views

#create paths
urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('today/',views.post_of_day,name = 'postToday'),
]