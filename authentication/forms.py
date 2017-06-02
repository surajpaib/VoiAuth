from models import SpeakerModel, AuthModel
from django import forms


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = SpeakerModel
        fields = ('name','audio',)


class AuthForm(forms.ModelForm):
    class Meta:
        model = AuthModel
        fields = ('audio',)
