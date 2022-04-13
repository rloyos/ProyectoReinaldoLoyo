from django.forms import ModelForm
from .models import Apartamento

class ApartamentForm(ModelForm):
    class Meta:
        model = Apartamento
        fields = "__all__"