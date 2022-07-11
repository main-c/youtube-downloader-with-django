
from django import forms


class Downloadform(forms.Form):
    yt_link = forms.URLField(max_length=200)

    
