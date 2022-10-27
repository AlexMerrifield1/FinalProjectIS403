from django.urls import path
from .views import IndexViewPage, LoginPage, TenantInfoPage


urlpatterns = [
    path("", IndexViewPage, name = "index"),
    path("about/", LoginPage, name = "about"),
    path("contact/", TenantInfoPage, name = "contact")
]   