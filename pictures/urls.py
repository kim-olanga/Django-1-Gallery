from django.urls import path
from . import views

#create paths
urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('photo/<str:pk>',views.viewPhoto,name = 'photo'),
    path('add/',views.addPhoto,name = 'add'),
    path('today/',views.post_of_day,name = 'postToday'),
    path('archive/({4}-{2}-{2})/',views.past_days_post,name= 'pastPost')
]