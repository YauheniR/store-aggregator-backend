from django.urls import path
from providers import views

urlpatterns = [
    path("", views.ProvidersView.as_view()),
    path("<int:id>/", views.ProviderView.as_view()),
]
