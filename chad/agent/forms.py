from django import forms
from .models import Avatar, Bot

class AvatarAdminForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'

class BotAdminForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = '__all__'