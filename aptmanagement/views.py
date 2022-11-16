from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def IndexViewPage(request) :
    #return HttpResponse ('Welcome to Apartment Management :)')
    #We that these HttpResponses in here, but I think we'll want
    # to be using render instead
    return render(request, 'aptmanagement/index.html')

def LoginPage(result) :
    #Not sure which html file to use with this one. 
    #There is a cool login page that we could possibly use. 
    return HttpResponse ('Login Here: ')

def TenantInfoPage(request) :
    #This will connect to the table html
    return render(request, 'aptmanagement/tables.html')
