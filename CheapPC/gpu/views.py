from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import GPUModel
from .models import populate
from .forms import UserForm


class HomeView(generic.ListView):
    template_name = 'client/home.html'
    context_object_name = 'gpu_list'

    populate()

    def get_queryset(self):
        """
        list all GPUs in DB
        """
        return GPUModel.objects.all()


class CardView(generic.DetailView):
    model = GPUModel
    template_name = 'client/card.html'


def gpu_card(request, pk):
    gpu = get_object_or_404(GPUModel, pk=pk)
    return render(request, 'client/card.html', {'gpu': gpu})


# references-
# https://www.geeksforgeeks.org/django-modelform-create-form-from-models/
# https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
def signup(request):
    context = {}
    # create object of form
    form = UserForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form'] = form
    return render(request, "client/new-user.html", {'form': form})
