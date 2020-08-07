import datetime

from django import forms
from .models import User,Community,Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
        ]