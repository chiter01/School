from django import forms

from django.contrib.auth.forms import AuthenticationForm

from news.models import News
from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class NewsForm(forms.Form):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название',
    }))
    image = forms.ImageField(label='Изображение', required=False, widget=forms.FileInput(attrs={
         'class': 'form-control',
    }))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '5'}))
    is_published = forms.BooleanField(label='Публичность', widget=forms.CheckboxInput(attrs={'id': 'news_is_pub'}))
    


class NewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'name',
            'description',
            'image',
            'is_published',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '8',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'id_is_published',
            }),
        }
class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}), 
        label='Имя пользователя'
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control'}),
    )
    
    class Meta:
        model = User
        

class RegisterForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 
        self.fields['email'].required = True 


    password1 = forms.CharField(label='Придумайте пароль', validators=[validate_password], widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))



    class Meta:
        model = User
        exclude = (
            'password', 
            'is_superuser', 
            'is_staff',
            'is_active',
            'user_permissions', 
            'groups', 
            'last_login', 
            'date_joined'
            )
        

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    
    def clean(self):
       
        cleaned_data = super().clean()
        
        password1 = cleaned_data.pop('password1', None)
        password2 = cleaned_data.pop('password2', None)
        if (password1 is not None and password2 is not None) and password1 != password2:
            raise forms.ValidationError({'password2': ['The passwords dont\'t match.']})

        
        password = make_password(password1)
        cleaned_data.setdefault('password', password)

        return cleaned_data


class ChangeProfileForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
    

class ChangePsswordForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user


    old_password = forms.CharField(
        label='Current paassword', 
        widget=forms.PasswordInput({'class': 'form-control'}),
        )
    new_password = forms.CharField(
        label='New paassword', 
        widget=forms.PasswordInput({'class': 'form-control'}),

        )
    
    confirm_password = forms.CharField(
        label='Confirm paassword', 
        widget=forms.PasswordInput({'class': 'form-control'}),
        )
    

    def clean(self):

        cleaned_data = super().clean()

        errors = {}

        old_password = cleaned_data.get('old_password', None)
        new_password = cleaned_data.get('new_password', None)
        confirm_password = cleaned_data.get('confirm_password', None)

        if old_password:
            if not self.user.check_password(old_password):
                errors['old_password'] = ['The current password is incorrect']
       
        if (new_password is not None and confirm_password is not None) \
            and new_password != confirm_password:
            errors['confirm_password'] = ['The passwords dont\'t match.']


        if len(errors) > 0:
            raise forms.ValidationError(errors)

        return cleaned_data