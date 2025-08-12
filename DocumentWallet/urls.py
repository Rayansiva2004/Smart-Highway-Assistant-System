from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('document-wallet/', views.documentWallet, name='document_wallet'),
    path('open-document/<int:doc_id>/', views.open_document, name='open_document'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
