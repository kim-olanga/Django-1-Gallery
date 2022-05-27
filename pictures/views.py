# from django.shortcuts import render
import datetime as dt
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to the art gallery')

def post_of_day(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
       <html>
            <body>
                <h1>Post for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html> 
            '''
    return HttpResponse(html)

def convert_dates(dates):
    #Function that gets that weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    #Returning the actual of the week
    day = days[day_number]
    return day