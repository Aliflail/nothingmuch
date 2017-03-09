from django.shortcuts import render
from models import answer 
from compilation import play
from oncomp.forms import inputprogram

def prog_insert(request):
    inpp=inputprogram(request.GET)
    if inpp.is_valid():
        prog=inpp.cleaned_data['source_code']
        a=answer()
        a.uid=request.user.username
        strn=a.uid+str(a.tid)+str(a.qno)
        p=play(prog,strn,lan,"No Output")
        p.compiler()
        a.save()