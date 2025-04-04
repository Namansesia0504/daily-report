from django import forms
from .models import Tweet

# class TweetForm(forms.ModelForm):
#      class Meta:
#         model = Tweet
#         fields ='__all__'

#         content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
#         image = forms.ImageField(required=False) 



from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    # Additional fields
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = Tweet
        fields = ['text', 'photo']  

class UserRegistrationForm(UserCreationForm):
   email = forms.EmailField( ) 
class Meta:
    model = User
    fields = ('username','email','password1','password2')