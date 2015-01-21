from __future__ import absolute_import

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password',
#                                 widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat your password',
#                                 widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ('email', 'name', 'image')

#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
        
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Passwords do not match')
#         return password2

#     def clean_image(self):
#         image = self.cleaned_data['image']
#         return image

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         password = self.cleaned_data['password1']
#         user.set_password(password)
#         if commit:
#             user.save()
#         return user

class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat your password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name', 'image')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        if commit:
            user.save()
        return user
        
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial['password']
