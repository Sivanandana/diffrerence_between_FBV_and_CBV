from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
from django.views.generic import TemplateView,View
# Create your views here.

class Form(TemplateView):
    template_name='form.html'
    
def fbv(request):
    FBV=FbvForm()
    d={'FBV':FBV}
    if request.method=='POST':
        FBVD=FbvForm(request.POST)
        if FBVD.is_valid():
            FBVD.save()
            return HttpResponse('done')
    return render(request,'fbv.html',d)    



class Cbv(View):
    def get(self,request):
        CBV=CbvForm()
        d={'CBV':CBV}
        return render(request,'cbv.html',d)
    def post(self,request):
        CBVD=CbvForm(request.POST)
        if CBVD.is_valid():
            CBVD.save()
            return HttpResponse('done')