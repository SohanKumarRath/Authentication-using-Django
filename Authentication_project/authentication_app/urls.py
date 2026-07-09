from django.urls import path
from authentication_app import views
urlpatterns = [
    path('signup/',views.signupView,name='signup'),]