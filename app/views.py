from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def Student_V(request):
    SFO=Student()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=Student(request.POST)
        if SFD.is_valid():
            return HttpResponse('Valid Data')
        else:
            return HttpResponse('In valid')
    return render(request,'form.html',d)



def Student_K(request):
    SFO=Student_R()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=Student_R(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('In valid')
    return render(request,'form.html',d)

