from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
#        fields = ['text', 'owner']
        fields = ['text']
        labels = {'text': ''}
#        labels = {'text': '', 'owner': 'owner'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
