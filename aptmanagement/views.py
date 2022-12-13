from django.http import HttpResponse
from django.shortcuts import render
from aptmanagement.models import Tennant, Admin, Apartments

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
    
    tennants = Tennant.objects.all()
    apartments = Apartments.objects.all()

    context = {
        "tennants" : tennants,
        "apartments" : apartments,
    }

    return render(request, 'aptmanagement/tennants.html', context)

def AddTennant(request) :
    if request.method == 'POST':
        apartment = Apartments()
        apartment.house = request.POST['house']
        apartment.rent = request.POST['rent']
        apartment.save()

        tennant = Tennant()
        tennant.first_name = request.POST['first_name']
        tennant.last_name = request.POST['last_name']
        tennant.rent_start = request.POST['rent_start_date']  
        tennant.rent_end = request.POST['rent_end_date']
        tennant.phone = request.POST['phone'] 
        tennant.appartment = apartment
        tennant.save()

        

    return TenantInfoPage(request)