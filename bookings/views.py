
# import all basic rendering and redirecting modules...
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# datetime module is used for deal with dates..
from datetime import datetime as dt

# this are all our models which we used in this section..

from bookings.models import Bookinghotel

# we dont required  this 2 models here ...
# from hotellist.models import Hotellist
# from mainapp.models import Login


# this page is for bookign hotels....
def bookings(request):
    data = {}
    data1 = {}
    bool = False
    # this get values are come from the hotellist page..
    if request.method == "GET":
        un1 = request.GET.get('name')
        password1 = request.GET.get('pw')
        hname1 = request.GET.get('hname')
        hcity1 = request.GET.get('hcity')
        hstate1 = request.GET.get('hstate')
        hcost1 = request.GET.get('hcost')
        # we use this url as a variable so that we can access this as a value in this  page as well as we can use this to take this value to dashboard page and by using this user can go to the dashboard page from the booking page...
        url = '/dashboard/?name={}&pw={}'.format(un1, password1)
        data = {'un1': un1, 'pw1': password1, 'hname1': hname1,
                'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1, 'url': url}
        return render(request, 'booking.html', data)
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            last = request.POST.get('last')
            email = request.POST.get('email')
            contact = request.POST.get('contact')
            person = request.POST.get('person')
            username = request.POST.get('username')
            password = request.POST.get('password')
            start = request.POST.get('startdate')
            end = request.POST.get('lastdate')
            hotelname = request.POST.get('hotelname')
            hotelcity = request.POST.get('hotelcity')
            hotelstate = request.POST.get('hotelstate')
            hotelcost = request.POST.get('hotelcost')

            #  this are all the get method variable....
            un1 = request.GET.get('name')
            password1 = request.GET.get('pw')
            hname1 = request.GET.get('hname')
            hcity1 = request.GET.get('hcity')
            hstate1 = request.GET.get('hstate')
            hcost1 = request.GET.get('hcost')

            if end < start:
                class_name = 'alert-warning'
                bool = 50
                n = 'your starting date must be less than ending date'

                # url = '/dashboard/?name={}&pw={}'.format(username, password)
                url = '/dashboard/?name={}&pw={}'.format(un1, password1)
                data1 = {'cname': class_name,
                         'bool': bool,
                         'n': n, 'un': username, 'pw': password, 'url': url, 'un1': un1, 'pw1': password1, 'hname1': hname1,
                         'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
                return render(request, 'booking.html', data1)
            else:
                data = Bookinghotel(firstname=name, lastname=last,
                                    email=email, contact_no=contact, no_people=person, username=username, userpassword=password, start=start, end=end, hotelname=hotelname, city=hotelcity, state=hotelstate, current_cost=hotelcost)
                data.save()
                class_name = 'alert-success'
                bool = True
                n = 'your bookings has been done now'
                url = '/dashboard/?name={}&pw={}'.format(username, password)
                data1 = {'cname': class_name,
                         'bool': bool,
                         'n': n, 'un': username, 'pw': password, 'url': url, 'un1': un1, 'pw1': password1, 'hname1': hname1,
                         'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
                return render(request, 'booking.html', data1)
    except Exception as e:
        pass
    # if there is no post request which means user does not do any booking then it will render and by using this user can also go to the dashboard page...
    # this is not neccesary because if the request is not post then it must be get and we already handle get request....
    return render(request, 'booking.html', data1)


# this is for user dashboard page....
def dashboard(request):
    data = {}
    if request.method == "GET":
        un = request.GET.get('name')
        password = request.GET.get('pw')
        tabel = Bookinghotel.objects.filter(username=un, userpassword=password)
        hotelurl = '/hotellist/{}/{}/{}'.format(un, password, 'all')
        reviewurl = '/review/{}/{}'.format(un, password)
        data = {'un': un, 'pw': password,
                'maindata': tabel, 'hotelurl': hotelurl, 'reviewurl': reviewurl}
        return render(request, 'dashboard.html', data)

    return render(request, 'dashboard.html', data)


# this is for order details page..
def details(request):
    data = {}
    if request.method == "GET":
        un = request.GET.get('name')
        password = request.GET.get('pw')
        id = request.GET.get('id1')
        url = '/dashboard/?name={}&pw={}'.format(un, password)
        maindata = Bookinghotel.objects.get(id=id)
        start = str(maindata.start)
        end = str(maindata.end)
        res = (dt.strptime(end, "%Y-%m-%d") -
               dt.strptime(start, "%Y-%m-%d")).days
        total_cost = res*maindata.current_cost
        data = {'un': un, 'pw': password,
                'maindata': maindata, 'url': url, 'cost': total_cost}
        return render(request, 'order_details.html', data)
    return render(request, 'order_details.html', data)



# this page is for deleting the order...
def delete(request):
    id1 = request.GET.get('id1')
    un = request.GET.get('name')
    pw = request.GET.get('pw')
    Bookinghotel.objects.filter(id=id1).delete()
    url = '/dashboard/?name={}&pw={}'.format(un, pw)
    return HttpResponseRedirect(url)



