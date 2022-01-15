from .models import Question
from django.forms import ModelForm, TextInput

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title"]
        widgets = {"title": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'input text'})}
