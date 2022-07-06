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
    include("Owner.urls")),
    path('Manager/',include("Manager.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)