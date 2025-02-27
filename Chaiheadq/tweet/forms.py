from django import forms
from .models import Tweet

class Tweetform(forms.ModelForm):
     class Meta:
        model = Tweet
        fields =['text','photo']

        content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
        image = forms.ImageField(required=False) 