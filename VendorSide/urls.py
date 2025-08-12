from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.service_details, name='bookings'),
    path('history/', views.history, name='history'),
    path('generate-bill/<int:entry_id>/', views.generate_bill_view, name='generate_bill'),
     path('view-bill/<int:bill_id>/', views.view_bill, name='view_bill'),
]
    