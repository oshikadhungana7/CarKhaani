from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name="Home"),
    path('Home/', views.Home, name="LoggedinHome"),
    path('signin/',views.signin,name="SignIn"),
    path('Logout/',views.Logout,name="Logout"),    
    path('register/',views.register,name="Register"),
    path('Profile/',views.Profile,name="Profile"),
<<<<<<< HEAD
    include("Owner.urls")),
=======
    path('about/', views.about_us, name="AboutUs"),
    path('contact/', views.contact_us, name="ContactUs"),
    path('search/', views.search, name="Search"),
    path('LoginAuthentication/',views.LoginAuthentication,name="LoginAuthentication"),
    path('RegisterCustomer/',views.RegisterCustomer,name="RegisterCustomer"),
    path('VehicleDetails/<str:Vehicle_license_plate>/',views.showdetails,name="VehicleDetails"),
    path('CheckAvailability/<str:Vehicle_license_plate>/',views.CheckAvailability,name="CheckAvailability"),
    path('SentRequests/',views.SentRequests,name="SentRequests"),
    path('RentVehicle',include("RentVehicle.urls")),
    path('Owner/',include("Owner.urls")),
>>>>>>> d32a1a7f101ba970f0428e742cee621ab1bb77e5
    path('Manager/',include("Manager.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)