from django.urls import path
from finance_app import views

app_name = "finance_app"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
