from django.shortcuts import render
from googletrans import Translator
translator = Translator()

def index(request):
    suz=request.GET.get('q','')
    if suz and suz!='':
        tr=translator.translate(suz,dest='uz')
        tr1=translator.translate(suz,dest='en')
        trans=[tr,tr1]
    else:
        trans=['','']
    return render(request,'index.html',{'trans':trans})