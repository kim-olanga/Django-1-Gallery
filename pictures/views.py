from django.shortcuts import render, redirect
import datetime as dt
from django.http import HttpResponse, Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def post_of_day(request):
    date = dt.date.today()
    
    return render(request,'all-news/today-posts.html', {"date": date,})

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

    return render(request, 'all-news/past-posts.html', {"date": date})