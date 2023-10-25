from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return  HttpResponse("This Works - Eat no meat for the entire month") # (something : response to send back to the client) - param request - HttpResponse - 
                                       # need to import:  from django.http import HttpResponse
                                       # as an argument a respond data that can be a html page or a string

def february(requst):
    return HttpResponse("Feb Response - Walk for at least 20 minuts every day")