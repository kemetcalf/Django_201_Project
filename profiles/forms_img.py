from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ImgUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('image',)
        help_texts = {
            'image': None,
        }
        labels = {
            'image': '',
            'currently': None,
        }

        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full text-base text-gray-500 border-2 border-indigo-500 rounded-lg file:bg-white file:mr-4 file:py-2 file:px-4 file:border file:border-r file:border-1 file:border-gray-50 file:border-y-transparent file:border-l-transparent  file:text-sm file:font-semibold file:text-gray-800 hover:file:bg-green-600 hover:file:bg-green-500 hover:file:text-white'},)
        }


profile = User.objects.get(id=1)
form = ImgUpdateForm(instance=profile)
