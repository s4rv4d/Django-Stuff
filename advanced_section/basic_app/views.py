from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from basic_app import models

# Create your views here.

# def index(request):
#     return render(request,'basic_app/index.html')

#testing out cbview

# class CBView(View):
#
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectedText'] = 'Basic injection'
        return context


class SchoolListView(ListView):
    # this can be used to make youre own context insraed of default
    context_object_name = 'schools'
    model = models.SchoolModel
    template_name = 'basic_app/school_list.html'
    # ListView creates school_list from model automatically

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.SchoolModel
    template_name = 'basic_app/school_detail.html'
