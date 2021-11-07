from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView
from .models import Customer
from django.contrib.auth import views as auth_views
from . import forms



class HomeView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'account:home-page'

class CustomerCreateView(CreateView):
	model = Customer
	template_name = 'form_add.html'
	fields = ('username','first_name','last_name','email','password')

class CustomerUpdateView(UpdateView):
	model = Customer
	template_name = 'form_update.html'
	fields = ('username','first_name','last_name','email','password')

class CustomerDeleteView(DeleteView):
	template_name = 'form_delete.html'
	model = Customer
	success_url = reverse_lazy('account:home-page')

class CustomerLogin(auth_views.LoginView):
    template_name = 'login.html'
    redirect_field_name = 'account:home-page'
    authentication_form = forms.CustomerAuthenticationForm

class CustomerLogout(auth_views.LogoutView):
    redirect_field_name = 'account:home-page'
    next_page = 'account:home-page'
    template_name = 'logout.html'

class CallView(TemplateView):
    template_name = 'call.html'
    context_object_name = 'account:call-page'
