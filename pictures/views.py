from django.shortcuts import render, redirect
import datetime as dt
from django.http import HttpResponse, Http404
from .models import Category, Image, Location

# Create your views here.
def index(request):
    
    images=Image.objects.all()
    categories=Category.objects.all()

    return render(request,'index.html',{"images":images})

def location(request,location_id):
    images=Image.objects.filter(location_id=location_id)

    return render(request,'location.html',{"images":images})

def category(request,category_id):
    images=Image.objects.filter(category_id=category_id)

    return render(request,'category.html',{"images":images})


def imagedetails(request,image_id):
    image=Image.objects.get(id=image_id)
    try:
        image = Image.objects.get(id=image_id)
    except Image.DoesNotExist:
         raise Http404()
    return render(request,"image.html",{"image":image})

def copy_image(from_model, to_model):
    to_model.image.save(from_model.image.url.split('/')[-1],from_model.image.file,save=True)

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})