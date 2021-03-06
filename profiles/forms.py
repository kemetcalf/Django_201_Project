from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        help_texts = {
            'username': None,
            'email': None,
        }
        labels = {
            'email': 'Email',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'flex flex-col border border-indigo-500 rounded-lg '}),
            'first_name': forms.TextInput(attrs={'class': 'flex flex-col border border-indigo-500 rounded-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'flex flex-col border border-indigo-500 rounded-lg'}),
            'email': forms.TextInput(attrs={'class': 'flex flex-col border border-indigo-500 rounded-lg'}),
        }


profile = User.objects.get(id=1)
form = UpdateForm(instance=profile)
