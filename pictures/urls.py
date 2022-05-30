from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#create paths
urlpatterns=[
    path('',views.index,name='index'),
    path('search/',views.search_results,name='search_results'),
    path('imagedetails/<image_id>',views.imagedetails,name='imagedetails'),
    path('category/<category_id>',views.category,name='category'),
    path('location/<location_id>',views.location,name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)