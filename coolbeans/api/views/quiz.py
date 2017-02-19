from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from coolbeans.api.serializers.quiz import QuizSerializer


class QuizViewSet(GenericViewSet,
                  ListModelMixin,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin):
    """
    A ViewSet for quiz-related operations.
    """
    serializer_class = QuizSerializer

    def list(self, request, *args, **kwargs):
        """
        Lists all quizzes.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creates a quiz.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        """
        Updates a quiz.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially updates a quiz.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes a quiz.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().destroy(request, args, kwargs)