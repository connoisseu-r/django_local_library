from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'title', 'text': 'text'}
        widgets = {'text': forms.Textarea(attrs={'rows':30, 'cols':100})}