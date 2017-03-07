from django import forms

class inputprogram(forms.Form):
    program=forms.TextField()
    pid=forms.IntegerField()
    uid=forms.CharecterField()
    tid=forms.IntegerField()