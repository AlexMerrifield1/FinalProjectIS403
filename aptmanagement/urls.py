from django.urls import path
from .views import IndexViewPage, LoginPage, TenantInfoPage


urlpatterns = [
    path("", IndexViewPage, name = "index"),
    path("tables/", LoginPage, name = "tables"),
    path("contact/", TenantInfoPage, name = "contact")
]   