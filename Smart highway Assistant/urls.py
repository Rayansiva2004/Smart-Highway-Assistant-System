from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Login.urls')),
    path('document-wallet/', include('DocumentWallet.urls')),
    path('user-side/', include('UserSide.urls')),
    path('vendor-side/', include('VendorSide.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

