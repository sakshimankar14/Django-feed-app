from django import forms
from .models import Feed

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'What\'s on your mind?'
            })
        }