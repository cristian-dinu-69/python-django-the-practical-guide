from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return  HttpResponse("This Works") # (something : response to send back to the client) - param request - HttpResponse - 
                                       # need to import:  from django.http import HttpResponse
                                       # as an argument a respond data that can be a html page or a string
