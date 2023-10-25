# create a list called urlpatterns
# in the list we will put all the URLs we want to support and the view function that should be triggered 
# when a request reaches that url

# we use path(), we need to import it - for that we need to import it from views.py
# first argument (url*,function index)
# if a request reaches /january then execute the function index

# but this is not enought ---until now we create a URLconfig
# this is done only in the challenges module (app) of the monthly_challenges project
# we need to connect this app to the entire project
# we go into the monthly_challegies/urls.py
# there we have already urlpatterns list, and already a path ...admin
# add here , but the url is not pointing to the app challenges - only and I want to load all the urls defined for challehges app

# we can do this with another function .. include..
# that we need to import it ..

# from django.urls import include
# path("challenges",include("challenges.urls"))

from django.urls import path
# from . views import index
from . import views

urlpatterns = [
    path("january", views.january),
    path("february", views.february)

]


