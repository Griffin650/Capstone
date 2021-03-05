from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import generic
# from django.urls import reverse

from .models import GPU
from .models import populate


class HomeView(generic.ListView):
    template_name = 'client/home.html'
    context_object_name = 'gpu_list'

    populate()

    def get_queryset(self):
        """
        list all GPUs in DB
        """
        return GPU.objects.all()


class CardView(generic.DetailView):
    model = GPU
    template_name = 'client/card.html'

    def gpu_card(request, pk):
        card = get_object_or_404(GPU, pk=pk)
        return render(request, 'client/home.html', {'card': card})
