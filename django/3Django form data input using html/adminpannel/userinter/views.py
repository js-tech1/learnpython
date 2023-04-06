from django.shortcuts import render
from .forms import FormContactForm
# Create your views here.
def showform(request):
    form = FormContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'contactform.html', context)