import django.forms as forms
from django.forms import ModelForm
from .models import Title



class AddJobForm(forms.Form):
    title = forms.CharField(max_length=50)
    minsal = forms.IntegerField(min_value=5000, max_value=10000000)

class AddTitleForm(ModelForm):
    class Meta:
        model = Title
        fields = '__all__'
