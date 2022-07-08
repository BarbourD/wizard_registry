from django.forms import ModelForm
from .models import Wand

class WandForm(ModelForm):
    class Meta:
        model = Wand
        fields = ['length', 'core', 'wood']