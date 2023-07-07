from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djangoforms(request):
    SUFO=SingupForm()#classname
    d={'SUFO':SUFO}#dict
    if request.method=='POST':
        SUFDT=SingupForm(request.POST)# classname=SingupFrom
        if  SUFDT.is_valid(): # valid the data
            n=SUFDT.cleaned_data['name'] #collect the data one by one
        return HttpResponse(request,'cmplted')



    return render(request,'djangoform.html',d)

