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


from django.contrib import admin
from django.urls import path
from mainapp import views



admin.site.site_header = "Hotel administration and managment"
admin.site.site_title = "Hotel administration and managment"
admin.site.index_title = "Hotel administration and managment"

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='service'),
    path('pricings/', views.price, name='price'),
    path('staffs/', views.staffs, name='staffs'),
    path('bookings/', views.bookings, name='booking'),
    path('login/', views.login, name='login'),
    # this is for update the password..
    path('update/',views.update,name='update'),
    path('signup/', views.signup, name='signup'),
    path('blogs/', views.blog, name='blog'),
    path('travel_details/', views.travel, name='travel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/delete/', views.delete, name='delete'),
    path('hotellist/<username>/<password>/<hotelstate>',
         views.hotellist, name='hotellist'),
    path('details/',views.details,name='order_details'),     
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)