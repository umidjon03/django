from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def loginview(request):
    print(request)

    if request.method=='POST':
        my_form=LoginForm(request.POST)
        if my_form.is_valid():
            my_form.save()
    return render(request,'index.html')

def typography(request):
    return render(request,'typography.html')

def post_single(request):
    return render(request,'post-single.html')
