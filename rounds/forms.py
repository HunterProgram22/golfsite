from django import forms

from .models import Round

class RoundForm(forms.ModelForm):
    
    class Meta:
        model = Round
        fields = ('course', 'date', 'strokes', 'putts', 
                  'fairways_hit', 'gir')
