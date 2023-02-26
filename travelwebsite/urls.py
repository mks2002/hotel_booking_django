"""travelwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path


# here we import all the different views of our project...
# travelwebsite is the main project level application of this project which django by default create inside any project...
from mainapp import views as v1
from bookings import views as v2
from hotellist import views as v3
from travelwebsite import views as v4
from userreview import views as v5


admin.site.site_header = "Hotel administration and managment"
admin.site.site_title = "Hotel administration and managment"
admin.site.index_title = "Hotel administration and managment"


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', v4.homepage, name='home'),
    path('about/', v4.about, name='about'),
    path('services/', v4.services, name='service'),
    path('pricings/', v4.price, name='price'),
    path('staffs/', v4.staffs, name='staffs'),
    path('bookings/', v2.bookings, name='booking'),
    path('login/', v1.login, name='login'),
    # this is for update the password..
    path('update/', v1.update, name='update'),
    path('signup/', v1.signup, name='signup'),
    path('travel_details/', v4.travel, name='travel'),
    path('dashboard/', v2.dashboard, name='dashboard'),
    path('dashboard/delete/', v2.delete, name='delete'),
    path('hotellist/<username>/<password>/<hotelstate>',
         v3.hotellist, name='hotellist'),
    path('details/', v2.details, name='order_details'),
    path('review/<username>/<password>', v5.review, name='review'),
    path('blogs/', v5.blog, name='blog'),
    path('logout/',v1.logout,name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
