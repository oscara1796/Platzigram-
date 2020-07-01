"""Users forms """

#Django
from django import forms

class ProfileForm(forms.Form):
    """Profile Form"""

    website = forms.URLField(max_length=200, required= True)
    biography = forms.CharField(max_length=300, required= False)
    phone_number = forms.CharField(max_length= 20, required= True)
    picture  = forms.ImageField()
