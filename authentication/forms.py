from models import SpeakerModel, AuthModel
from django import forms


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = SpeakerModel
        fields = ('name','audio','label')


class AuthForm(forms.ModelForm):
    class Meta:
        model = AuthModel
        fields = ('audio',)
