from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(
        label='Your text',
        max_length=1800,
        widget=forms.Textarea(attrs={"cols": 80}),)
    author = forms.CharField(widget=forms.HiddenInput(), required=False)
    date = forms.DateTimeField()

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'author',
            'date'
                ]
