from .models import New
from django.forms import ModelForm, TextInput, Textarea


class NewForm(ModelForm):
    class Meta:  # доп. настройки
        model = New
        fields = ["title_news", "tag_news", "text_news"]
        widgets = {
            "tag_news": TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Введитие тег',
                'size': '95'
            }),
            "title_news": TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Введитие заголовок',
                'size': '95'
            }),
            "text_news": Textarea(attrs={
                'size': '95',
                'class': 'form_control',
                'placeholder': 'Введитие текст',
                'rows': '15',
                'cols': '98',
            }),
        }

class TextsFormSecond(ModelForm):
    class Meta:
        model = New
        fields = ["text_news"]
        widgets = {
            "text_news": Textarea(attrs={
                'size': '95',
                'class': 'form_control',
                'placeholder': 'Введитие текст',
                'rows': '15',
                'cols': '98',

            })
        }
