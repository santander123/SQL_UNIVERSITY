from django.urls import path
from . import views

app_name="prestamos"

urlpatterns = [
    path('',views.homePrestamos,name='home'),
]