from models import SpeakerModel
from django import forms


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = SpeakerModel
        fields = ('name','audio',)
