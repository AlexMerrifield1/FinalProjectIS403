from django.http import HttpResponse

# Create your views here.
def IndexViewPage(result) :
    return HttpResponse ('Welcome to Apartment Management :)')

def LoginPage(result) :
    return HttpResponse ('Login Here: ')

def TenantInfoPage(result) :
    return HttpResponse ('Here are all of the Tenants. ')