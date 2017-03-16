from django.views import View


class QuizListView(View):
    """
    A view for listing all quizzes this user is allowed to edit.
    """
    pass


class QuizCreateView(View):
    """
    A view for creating quizzes.
    """
    pass # TODO: Implement this along with QuizEditView


class QuizEditView(View):
    """
    A view for editing quizzes.
    """
    pass # TODO: Implement this along with QuizCreateView


class QuestionListView(View):
    """
    A view for listing the questions in a quiz.
    """
    pass


class QuestionCreateView(View):
    """
    A view for creating a single question.
    """
    pass


class QuestionEditView(View):
    """
    A view for editing a single question.
    """
    pass