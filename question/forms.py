from django import forms
from .models import Apt_Test,Apt_Qns,Answers,Options

class Apt_TestForm(forms.ModelForm):
    class Meta:
        model = Apt_Test
        fields=['name','time','startDate','endDate']