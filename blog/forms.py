from django import forms
from django.core.exceptions import ValidationError

error_messages = {
    'required': 'این فیلد باید پر شود دوست من',
    'invalid': 'قدار این فیلد صحیح نیست'
}


class CreateArticleForm(forms.Form):
    title = forms.CharField(max_length=110, label='Article Title', widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages=error_messages)
    text = forms.CharField(max_length=550, widget=forms.Textarea(attrs={'class': 'form-control'}), help_text='قدار متن شما نباید از 500 کارکتر بیشتر باشد', error_messages=error_messages)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), error_messages=error_messages)
    is_show = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), error_messages=error_messages)

    # def clean(self):
    #     cleand_data = super().clean()
    #     title = cleand_data.get('title')
    #     if "mohammad" not in title:
    #         # raise ValidationError('Mohammad is Not Here')
    #         self.add_error('title', 'mohammad is not Here')
    #     return cleand_data

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if 'mohammad' not in title:
    #         raise ValidationError('Error')
    #     return title


class ArticleEdit(forms.Form):
    title = forms.CharField(max_length=110, label='Article Title', widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages=error_messages)
    text = forms.CharField(max_length=550, widget=forms.Textarea(attrs={'class': 'form-control'}), help_text='قدار متن شما نباید از 500 کارکتر بیشتر باشد', error_messages=error_messages)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),
                             error_messages=error_messages, required=False)
    is_show = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), error_messages=error_messages)