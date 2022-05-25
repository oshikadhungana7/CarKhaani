from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name="Home"),
    path('SendRequest_toOwner/',views.SendRequest_toOwner,name="SendRequest_to_Owner"),
    path('AcceptRequest/',views.AcceptRequest,name="AcceptRequest"),
    path('DeclineRequest/',views.DeclineRequest,name="DeclineRequest"),
    path('CancelRequest/',views.CancelRequest,name="CancelRequest"),
    path('Owner/',include("Owner.urls")),
<<<<<<< HEAD
    path('Manager/',include("Manager.urls"))
=======
   
>>>>>>> f11734c1c76b04b04a6a9d2dda0bbb96b517ac68
]