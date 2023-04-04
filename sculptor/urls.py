from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "NIMSCULPS"
admin.site.site_title = "K ADMIN"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('sculptorapp.urls')),
    path('sculptorauth/',include('sculptorauth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
