from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # add to path to get django admin site
    path('api/', include('clubs.urls'))  # add to path to get club API
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # this is for properly path to crests
