from django import forms
from .models import Post, Tag, Image, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            # 'tags': forms.CheckboxSelectMultiple(),
            'tags': forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
        }


class AddImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=True
    )

    class Meta:
        model = Image
        fields = ['image']


class CreateUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'e_mail', 'birthday', 'gender', 'bio', 'photo']
        widgets = {
            'full_name': forms.TextInput(attrs={"class": "form-control"}),
            'e_mail': forms.TextInput(attrs={"class": "form-control"}),
            'birthday': forms.DateField(),
            'gender': forms.ChoiceField(),
            'bio': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'photo': forms.ImageField(),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
