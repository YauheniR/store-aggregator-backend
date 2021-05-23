from django.urls import path
from providers import views


urlpatterns = [
    path('', views.ProvidersView.as_view(), name='ProvidersList'),
    path('<pk>/', views.ProviderView.as_view(), name='ProviderDetail'),
]
