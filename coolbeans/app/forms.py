from django.forms import ModelForm
from coolbeans.app.models.question import MultipleChoiceModel
from coolbeans.app.models.question import WordScrambleQuestionModel

# Create the form class.

class MCQForm(ModelForm):
    class Meta:
        model = MultipleChoiceModel
        fields = '__all__'

class DNDForm(ModelForm):
    class Meta:
        model = WordScrambleQuestionModel
        fields = '__all__'