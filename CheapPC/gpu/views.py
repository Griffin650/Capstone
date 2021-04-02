from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
import requests

import yfinance as yf
import plotly.graph_objs as go
from plotly.offline import plot


from .models import GPUModel, populate


def graphs(request):
    return render(request, 'client/graphs.html', {'btc_price_graph': crypto_graph('BTC'),
                                                  'eth_price_graph': crypto_graph('ETH'),
                                                  'ltc_price_graph': crypto_graph('LTC')})


def home_view(request):
    populate()

    gpu_list = GPUModel.objects.all()
    return render(request, 'client/home.html', {'gpu_list': gpu_list,
                                                'btc_price': get_btc_price(),
                                                'eth_price': get_eth_price(),
                                                'ltc_price': get_ltc_price(),
                                                'user': request.user})


def gpu_card(request, pk):
    card = get_object_or_404(GPUModel, pk=pk)
    return render(request, 'client/card.html', {'gpu': card,
                                                'btc_price': get_btc_price(),
                                                'eth_price': get_eth_price(),
                                                'ltc_price': get_ltc_price()})


# API: https://min-api.cryptocompare.com/documentation?key=Price&cat=multipleSymbolsFullPriceEndpoint
def get_btc_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()['USD']


def get_eth_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()['USD']


def get_ltc_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD').json()['USD']


# Reference:
# https://medium.datadriveninvestor.com/python-how-to-get-live-cryptocurrency-data-less-than-0-1-second-lag-7f23d854314a
def crypto_graph(ticker):
    # Get Bitcoin data
    data = yf.download(tickers=ticker+'-USD', period='1wk', interval='60m')
    # declare figure
    fig = go.Figure()
    # Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'], name='market data'))
    # Add titles
    fig.update_layout(
        title=ticker+' Price Over Past Week',
        yaxis_title=ticker+' Price USD')
    # X-Axes
    fig.update_xaxes(rangeslider_visible=True)
    return plot(fig, output_type='div')


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
