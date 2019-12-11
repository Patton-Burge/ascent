from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from initiative.views import InitiativeView, InitiativeCreateView

app_name = "initiatives"

urlpatterns = [
    path("", InitiativeView.as_view(), name="home"),
    path("create/", InitiativeCreateView.as_view(), name="create"),
]