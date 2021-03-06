from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import generic
# from django.urls import reverse

from .models import GPU
from .models import populate
from .forms import NewUser


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


class SignUpView(generic.DetailView):
    model = GPU
    template_name = 'client/signup.html'

    def get_object(self):
        return self.model.objects.get(pk=self.request.user.pk)

    def get_queryset(self):
        return ''


# taken from, resource: https://docs.djangoproject.com/en/3.1/topics/forms/
def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewUser(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewUser()
    return render(request, 'client/new-user.html', {'form': form})
