from django.forms import ModelForm
from coolbeans.app.models.question import MultipleChoiceModel

# Create the form class.

class MCQForm(ModelForm):
    class Meta:
        model = MultipleChoiceModel
        fields = '__all__'