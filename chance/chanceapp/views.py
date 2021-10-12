from django.shortcuts import render
from .forms import OpinionForm,AdminForm
# Create your views here.
def index(request):
    if request.method=='POST':

        myform=OpinionForm(request.POST)
        try:
            if myform.is_valid:
                myform.save()
        except:
            myform=AdminForm(request.POST)
            if myform.is_valid:
                myform.save()


    return render(request,'index.html')