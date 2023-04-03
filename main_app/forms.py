from django.forms import ModelForm
from .models import Boss

class BossForm(ModelForm):
    class Meta:
        model = Boss
        fields = ['name', 'description']