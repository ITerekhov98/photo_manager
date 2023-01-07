from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.http import HttpResponseNotFound
import json


def error404(request, exception):
    response_data = {
        'detail': 'Not found'
    }
    return HttpResponseNotFound(
        json.dumps(response_data),
        content_type="application/json"
    )


handler404 = error404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('photos_manager.apps.urls')),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)