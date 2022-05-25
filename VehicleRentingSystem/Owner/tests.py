from telnetlib import LOGOUT
from django.test import TestCase
from django.urls import *
from VehicleRentingSystem.CustomerHome.views import Logout

from VehicleRentingSystem.Owner.views import Profile

def test_register_url(self):
         url = reverse("Logout")
         self.assertEquals(resolve(url).func, Logout)

def test_signin_url(self):
         url = reverse("Profile")
         self.assertEquals(resolve(url).func, Profile)

def test_registercustomer_url(self):
         url = reverse("RegisterCustomer")
         self.assertEquals(resolve(url).func, RegisterCustomer)

def test_loginauthen_url(self):
         url = reverse("LoginAuthentication"),
         self.assertEquals(resolve(url).func, LoginAuthentication)

def test_home_url(self):
         url = reverse("LoggedinHome"),
         self.assertEquals(resolve(url).func, Home)

def test_profile_url(self):
         url = reverse("profile"),
         self.assertEquals(resolve(url).func, Profile)
def test_register_url(self):
         url = reverse("Register")
         self.assertEquals(resolve(url).func, register)
def test_register_url(self):
         url = reverse("Register")
         self.assertEquals(resolve(url).func, register)