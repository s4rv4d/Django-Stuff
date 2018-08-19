from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import (
                                    TemplateView,
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
)
# Create your views here.

class SignUp(CreateView):
    # pass
    #using pass so that i can deal wih forms first
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'







# class MODELNAMECreateView(CreateView):
#     model = MODELNAME
#     form_class = FORM_CLASS
#     success_url = 'SUCCESS_URL'
#     template_name = 'TEMPLATE_NAME'
