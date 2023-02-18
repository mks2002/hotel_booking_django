
# import all basic rendering and redirecting modules...
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# datetime module is used for deal with dates..
from datetime import datetime as dt

# this are all our models which we used in this section..
from hotellist.models import Hotellist

# we dont required this 2 models here ...
# from mainapp.models import Login
# from bookings.models import Bookinghotel


# this is the dynamic hotellist page ...
# only admin has the access to add new hotels in this list through admin dashboard...
def hotellist(request, username, password, hotelstate):
    if hotelstate == 'all':
        data = Hotellist.objects.all()
    elif hotelstate == 'others':
        data = Hotellist.objects.filter(
            state='gujrat') | Hotellist.objects.filter(state='laddakh')
    else:
        data = Hotellist.objects.filter(state=hotelstate)

    url = '/dashboard/?name={}&pw={}'.format(username, password)

    datamain = {'un': username, 'pw': password,
                'url': url, 'data': data}
    return render(request, 'hotellist.html', datamain)
