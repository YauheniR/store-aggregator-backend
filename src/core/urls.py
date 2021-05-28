from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('providers/', include('providers.urls')),
        path('schema/', include([
            path('', SpectacularAPIView.as_view(), name='schema'),
            path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
            path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), ]))
    ])),
]
