# HttpResponse is used to
# pass the information 
# back to view
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase
  
# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def hello (request) :
  
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello my friend.")

def check(request) :
    return render(request,"check.html")
