from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage, name='home'),
    path('repairs/', views.repairsPage, name='repairs'),
    path('towing/',views.towingPage,name='towing'),
    path('my-bills/', views.user_bills, name='user_bills'),
]
