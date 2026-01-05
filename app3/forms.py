from django import forms
from  .models import *

class sampleform(forms.ModelForm):
    class Meta:
        model = artworker
        fields='__all__'

class sampleform1(forms.ModelForm):
    class Meta:
        model = craftworker
        fields='__all__'

class sampleform2(forms.ModelForm):
    class Meta:
        model = artproduct
        fields='__all__'

class sampleform3(forms.ModelForm):
    class Meta:
        model = craftproduct
        fields='__all__'

class sampleform4(forms.ModelForm):
    class Meta:
        model = user_register
        fields='__all__'