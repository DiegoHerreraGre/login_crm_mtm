from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="glyphicon glyphicon-user">Debe intentar con un nombre de usuario correcto</span>'

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


# Creating a Add Record form

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone Number', max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))
    city = forms.CharField(label='City', max_length=100, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(label='State', max_length=100, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    rut = forms.IntegerField(label='RUT', max_value=20, required=True, )

    class Meta:
        model = Record
        exclude = ('user',)


class UploadExcel(forms.Form):
    file = forms.FileField(label='Excel File', required=True)
    exclude = ('user',)


class AvatarForm(forms.ModelForm):
    avatar = forms.ImageField(label='Avatar', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Record
        fields = ('avatar',)
