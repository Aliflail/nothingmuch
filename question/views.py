from django.shortcuts import render, HttpResponse
from django.views import View
from django.shortcuts import redirect
from question import models, forms


# Create your views here.

def home(request):
    return render(request, 'question/Home.html')


def createTest(request):
    if (request.method == "POST"):
        form = forms.Apt_TestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    else:
        form = forms.Apt_TestForm()
    return render(request, 'question/createTest.html', {'form': form})
