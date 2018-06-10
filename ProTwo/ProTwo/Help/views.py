from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {"insert_me":"Help Page"}
    return render(request,'Help/help.html',context=my_dict)
