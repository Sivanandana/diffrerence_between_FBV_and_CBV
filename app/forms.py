from django import forms
from app.models import *
class FbvForm(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'

class CbvForm(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'