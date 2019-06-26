from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from myblog.models import Aritical

# class Aritical_Form(forms.Form):
#     foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

class Aritical_Form(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())
