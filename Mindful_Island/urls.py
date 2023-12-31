from django.contrib import admin
from django.urls import path, include
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meditations.urls')),
    # path('', include('register.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
