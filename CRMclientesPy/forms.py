from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))

    class Meta:

        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="glyphicon glyphicon-user">Debe intentar con un nombre de usuario correcto</span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<span class="glyphicon glyphicon-lock">Debe intentar con una contraseña segura</span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="glyphicon glyphicon-lock">Debe intentar con una contraseña segura</span>'