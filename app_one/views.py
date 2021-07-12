from django.shortcuts import render
from time import gmtime, strftime
# from time import time, strftime

    
def index(request):
    context = {
        "time": strftime("%b %d, %I:%M %p", gmtime())
        # "time": strftime("%b %d, %I:%M %p", time.localtime())

    }
    return render(request,'index.html', context)


# Create your views here.


