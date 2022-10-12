from wsgiref.validate import validator
from django import forms

# class SignUp(forms.Form):
#     first_name = forms.CharField(initial= 'First Name',)
#     last_name = forms.CharField(initial= 'Last Name',)
#     mail = forms.EmailField(help_text= 'Write your mail',)
#     address = forms.CharField(required= False, )
#     technology = forms.CharField(initial= 'django', disabled= True, )
#     age = forms.IntegerField()
#     password = forms.CharField(widget= forms.PasswordInput, validators=[validator.MinLenthValidator(6)])
#     re_password = forms.CharField(help_text= 're-enter your password', widget= forms.PasswordInput)

def clean_password(self):
    password = self.cleaned_data['password']
    if len(password) < 4:
        raise forms.ValidationError('Password is too short ~!')
    return password

def check_size(value):
    if len(value)<6:
        raise forms.ValidationError("The password is too short!")
class SignUp(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    mail = forms.EmailField(help_text= 'Write your mail',)
    address = forms.CharField(required= False, )
    technology = forms.CharField(initial= 'django', disabled= True, )
    age = forms.IntegerField()
    password = forms.CharField(widget= forms.PasswordInput, validators=[check_size, ])
    re_password = forms.CharField(help_text= 're-enter your password', widget= forms.PasswordInput)