from django.forms import ModelForm, Form, CharField
from coolbeans.app.models.question import MultipleChoiceModel, WordMatchingModel, WordScrambleQuestionModel, GapFillQuestionModel

# Create the form class.


class MCForm(ModelForm):
    class Meta:
        model = MultipleChoiceModel
        fields = '__all__'


class WMForm(ModelForm):
    class Meta:
        model = WordMatchingModel
        fields = '__all__'


class WSForm(ModelForm):
    class Meta:
        model = WordScrambleQuestionModel
        fields = '__all__'


class GFForm(ModelForm):
    class Meta:
        model = GapFillQuestionModel
        fields = '__all__'

class TestForm(Form):
    title = CharField()