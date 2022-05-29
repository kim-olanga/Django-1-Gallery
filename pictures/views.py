from django.shortcuts import render, redirect
import datetime as dt
from django.http import HttpResponse, Http404

from pictures.models import Category, Image, Location

# Create your views here.
def welcome(request):
    categories=Category.objects.all()
    locations=Location.objects.all()
    all_images=Image.get_images()
    return render(request, 'welcome.html',{"templateimages":all_images, 'categorytemplates':categories, 'locations':locations})

def viewPhoto(request, pk):
    return render(request, 'photo.html')

def addPhoto(request):
    return render(request, 'add.html')

def search(request):
    categories=Category.objects.all()
    locations=Location.objects.all()
    if 'search' in request.GET and request.GET["search"]:
        term_of_search = request.GET.get("search")
        searched_images = Image.search_image(term_of_search)
        print("___________________________________________")
        print(searched_images)
        message = f"{term_of_search}"

        return render(request, 'search.html',{"message":message,"images": searched_images, 'categories':categories, 'locations':locations})

    else:
        message = "Kindly input your search request"
        return render(request, 'search.html',{"message":message})
      
def get_location(request, location_id):
    location_images=Image.filter_by_location(location_id)
    return render(request, 'location.html', {'images':location_images})

def post_of_day(request):
    date = dt.date.today()
    
    return render(request,'all-posts/today-posts.html', {"date": date,})

def convert_dates(dates):
    #Function that gets that weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    #Returning the actual of the week
    day = days[day_number]
    return day

def past_days_post(request,past_date):
    try:
        #Converts data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(post_of_day)

    return render(request, 'all-posts/past-posts.html', {"date": date})