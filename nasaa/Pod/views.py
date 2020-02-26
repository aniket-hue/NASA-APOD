from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    date="2018-12-28"
    url = 'https://api.nasa.gov/planetary/apod?api_key=lnjLOPvbSjjy8fBS3tHsUHtlD3qBigaxUfQe8gUW'
    r=requests.get(url).json()
    imginfo= {
    'date':r['date'],
    'explanation':r['explanation'],
    'hdurl':r['hdurl']
    }
    print(imginfo)
    context={'imginfo':imginfo}
    return render(request,'index.html',context)
