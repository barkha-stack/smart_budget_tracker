from django.urls import path
from . import views

urlpatterns = [
    # URL: /accounts/signup/
    path('signup/', views.signup, name='signup'),
]
