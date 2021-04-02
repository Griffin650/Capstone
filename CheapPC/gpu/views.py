from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
# import matplotlib.pyplot as pyplot
import requests

from .models import GPUModel, populate


def home_view(request):
    populate()

    gpu_list = GPUModel.objects.all()
    btc_price = get_btc_price()
    eth_price = get_eth_price()
    ltc_price = get_ltc_price()
    current_user = request.user
    return render(request, 'client/home-test.html', {'gpu_list': gpu_list,
                                                     'btc_price': btc_price,
                                                     'eth_price': eth_price,
                                                     'ltc_price': ltc_price,
                                                     'user': current_user})


def gpu_card(request, pk):
    card = get_object_or_404(GPUModel, pk=pk)
    btc_price = get_btc_price()
    eth_price = get_eth_price()
    ltc_price = get_ltc_price()
    return render(request, 'client/card.html', {'gpu': card,
                                                'btc_price': btc_price,
                                                'eth_price': eth_price,
                                                'ltc_price': ltc_price})


# API: https://min-api.cryptocompare.com/documentation?key=Price&cat=multipleSymbolsFullPriceEndpoint
def get_btc_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()['USD']


def get_eth_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()['USD']


def get_ltc_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD').json()['USD']

'''
def plot(graphtitle, xtitle, xvals, ytitle, yvals):
    pyplot.plot(xvals, yvals)
    pyplot.xlabel(xtitle)
    pyplot.ylabel(ytitle)
    pyplot.title(graphtitle)
    pyplot.show()
'''


# references-
# https://www.geeksforgeeks.org/django-modelform-create-form-from-models/
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/gpu')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
