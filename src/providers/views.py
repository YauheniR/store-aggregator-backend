from django.views import generic
from providers.models import ProviderModel


class ProvidersView(generic.ListView):
    template_name = 'providers/Providers_List.html'
    context_object_name = 'providers_list'

    def get_queryset(self):
        return ProviderModel.objects.all()


class ProviderView(generic.DetailView):
    model = ProviderModel
    template_name = 'providers/Provider_Detail.html'
    context_object_name = 'provider'
