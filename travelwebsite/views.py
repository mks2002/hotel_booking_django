
# this views render all tha project level apps which are common to entire project and not required any model query ...


# import all basic rendering and redirecting modules...
from userreview.models import Review
from django.http import HttpResponse
from django.shortcuts import render


# requests module is used for dealing with api...
import requests


# Create your views here.

# this 6 are static pages...
def homepage(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def price(request):
    return HttpResponse('this is price page')


def staffs(request):
    return render(request, 'staffs.html')


# this is the traindetails page ...
# here we use api of irctc to show traindetails to a user on searching the train name...
def travel(request):
    data = {}
    try:
        if request.method == "POST":
            id1 = request.POST.get('source')
            url = "https://trains.p.rapidapi.com/"

            payload = {"search": id1}
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "a78e10f741mshff5ec54a01b89afp1e0ae3jsnfdbc5239b4a0",
                "X-RapidAPI-Host": "trains.p.rapidapi.com"
            }

            response = requests.request(
                "POST", url, json=payload, headers=headers)
            datamain = response.json()
            data = {'datamain': datamain}
            return render(request, 'travel_details.html', data)
    except Exception as e:
        pass
    return render(request, 'travel_details.html', data)



