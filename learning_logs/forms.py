from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": "text is : "}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "text is "}
        widgets = {"text": forms.Textarea(attrs={'cols': 80})}


class edit_entry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text edite": "text is "}
        widgets = {"text": forms.Textarea(attrs={'cols': 80})}