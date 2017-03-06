from django.views import View
from django.views.generic import TemplateView


class QuizListView(TemplateView):
    """
    A view for listing the quizzes this user can access.
    """
    template_name = "app/quiz/attempt/list.html"


class QuizDetailView(TemplateView):
    """
    A view for listing the details of a quiz.
    """
    template_name = "app/quiz/attempt/details.html"


class AttemptQuizView(TemplateView):
    """
    A view for launching the quiz app.
    """
    template_name = "app/quiz/attempt/attempt.html"
