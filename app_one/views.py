from django.shortcuts import render
from time import gmtime, strftime
# from datetime import datetime, timezone

# current_date = datetime.now().date()
# print(current_date)
# utc_current_time = datetime.now(timezone.utc).time()
# print(utc_current_time)
    
def index(request):
    context = {
        "time": strftime("%b %d, %Y %I:%M %p", gmtime())
    }
    return render(request, 'index.html', context)

# def index(request):
#     context = {
#         "date": current_date,
#         "time": utc_current_time
#     }
#     return render(request, 'index.html', context)

# Create your views here.


