from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField()
    author = forms.CharField()
    date = forms.DateTimeField()

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'author',
            'date'
                ]
