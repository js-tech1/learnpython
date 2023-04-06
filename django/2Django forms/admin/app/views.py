from django.shortcuts import render
from .forms import login , CarryData

# Create your views here.

def ShowLoginForm(request):
    if request.method=='POST':
        form=CarryData(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['fname']
            lname=form.cleaned_data['lname']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            form.save()
    template='form.html'
    form=login()
    return render(request,template,{'form':form})

