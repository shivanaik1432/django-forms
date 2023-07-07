from django import forms
g=[('male','MALE'),('femlae','FEMALE')]
class SingupForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    gender=forms.ChoiceField(choices=g)
    pw=forms.CharField(max_length=15,widget=forms.PasswordInput)
    