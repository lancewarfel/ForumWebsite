from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Post, AppUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['name', 'username', 'email', 'password1', 'password2']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ['avatar','name','username', 'email', 'bio']
