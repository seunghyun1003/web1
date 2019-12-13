from django.forms import ModelForm
from .models import Entries

class CreatememoForm(ModelForm):
    class Meta:
        model = Entries
        fields = ['title','content']
