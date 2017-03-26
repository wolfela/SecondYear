from django.forms import ModelForm
from coolbeans.app.models.question import MultipleChoiceModel, WordMatchingModel, WordScrambleQuestionModel, GapFillQuestionModel
from coolbeans.app.models.quiz import QuizModel

class MCForm(ModelForm):
    """
    Multiple Choice Question Form made from the model
    """
    class Meta:
        model = MultipleChoiceModel
        fields = '__all__'


class WMForm(ModelForm):
    """
    Word Matching Question Form made from the model
    """
    class Meta:
        model = WordMatchingModel
        fields = '__all__'


class WSForm(ModelForm):
    """
    Word Scramble Question Form made from the model
    """
    class Meta:
        model = WordScrambleQuestionModel
        fields = '__all__'


class GFForm(ModelForm):
    """
    Gap Fill Question Form made from the model
    """
    class Meta:
        model = GapFillQuestionModel
        fields = '__all__'


class QuizForm(ModelForm):
    """
    Quiz Form made from the model
    """
    class Meta:
        model = QuizModel
        fields = '__all__'
