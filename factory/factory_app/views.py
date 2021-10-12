from django.shortcuts import render
from .forms import MesssageForm
# Create your views here.
def index(request):
    if request.method=='POST':
        form=MesssageForm(request.POST)
        if form.is_valid:
            form.save()

    return render(request,'index.html')