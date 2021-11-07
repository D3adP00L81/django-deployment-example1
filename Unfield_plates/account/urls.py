from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path
from . import views
from .views import HomeView,CustomerCreateView,CustomerUpdateView,CustomerLogout,CustomerDeleteView,CustomerLogin,CallView

app_name = 'account'

urlpatterns = [
    path('', HomeView.as_view(),name = 'home-page'),
    path('account/add/', CustomerCreateView.as_view(), name='customer-add'),
    path('account/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('account/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('account/login/',CustomerLogin.as_view(),name = 'customer-login'),
    path('account/logout/',CustomerLogout.as_view(),name = 'customer-logout'),
    path('call/', CallView.as_view(),name = 'call-page'),
]
