from django.forms import ModelForm
from coolbeans.app.models.question import MultipleChoiceModel, TrueFalseQuestionModel, WordMatchingQuestionModel, WordScrambleQuestionModel, GapFillQuestionModel

# Create the form class.

class MCForm(ModelForm):
    class Meta:
        model = MultipleChoiceModel
        fields = '__all__'


class TFForm(ModelForm):
    class Meta:
        model = TrueFalseQuestionModel
        fields = '__all__'


class WMForm(ModelForm):
    class Meta:
        model = WordMatchingQuestionModel
        fields = '__all__'


class WSForm(ModelForm):
    class Meta:
        model = WordScrambleQuestionModel
        fields = '__all__'


class GFForm(ModelForm):
    class Meta:
        model = GapFillQuestionModel
        fields = '__all__'