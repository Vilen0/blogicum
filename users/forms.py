from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser


class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('username', 'bio')