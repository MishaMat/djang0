import datetime

from django import forms
from django.core.exceptions import ValidationError
from forms6.models import *


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birthday = forms.DateField()

    def clean_birthday(self):
        data = self.cleaned_data['birthday']
        today = datetime.date.today()
        print(data, '   ', today)
        year_delta = (today - data).days / 365
        print(today - data)
        if year_delta < 18:
            raise ValidationError('you arent 18 years old')
        return data


class CommentForm(forms.ModelForm):
    news = forms.ModelChoiceField(queryset=NewsModel.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = CommentModel
        fields = ['username', 'comment']


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['title', 'main_info', 'flag']
