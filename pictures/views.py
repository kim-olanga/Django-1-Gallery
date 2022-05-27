# from django.shortcuts import render
import datetime as dt
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to the art gallery')

def post_of_day(request):
    date = dt.date.today()
    html = f'''
       <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html> 
            '''
    return HttpResponse(html)

