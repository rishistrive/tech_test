from django.forms import ModelForm
from .models import ResourceCollection


class ResourceCollectionForm(ModelForm):
    class Meta:
        model = ResourceCollection
        fields = "__all__"
