from django.shortcuts import render
from django.http import HttpResponse

# added by me
from django.http import HttpResponseNotFound

# Create your views here.
# def january(request):
#     return  HttpResponse("This Works - Eat no meat for the entire month") # (something : response to send back to the client) - param request - HttpResponse - 
#                                        # need to import:  from django.http import HttpResponse
#                                        # as an argument a respond data that can be a html page or a string

# def february(requst):
#     return HttpResponse("Feb Response - Walk for at least 20 minuts every day")

def monthly_challege(request, month):
    challenge_text = None
    if month == "january" :
        challenge_text = " Jan - Eat no meat entire month!"
    elif month == "february":
        challenge_text = "Feb - Run 20 mins every day entire month"
    elif month == "march":
        challenge_text = "March - Learn Django 20 mins every day entire month"
    else :
    # from django.http import HttpResponseNotFound
        return HttpResponseNotFound("Month Not Supported")
    return HttpResponse(challenge_text)