from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin, \
    ListModelMixin
from rest_framework.viewsets import GenericViewSet

from coolbeans.api.serializers.question import QuestionSerializer
from coolbeans.app.models import BaseQuestionModel


class QuestionSubclassesFieldsMixin:
    """
    A serializer mixin that provides Question subclass serializing via InheritanceManager.

    Inspired from http://stackoverflow.com/a/42282447/1049833
    """

    def get_queryset(self):
        return BaseQuestionModel.objects.select_subclasses()


class QuestionViewSet(GenericViewSet,
                      QuestionSubclassesFieldsMixin,
                      ListModelMixin,
                      CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin):
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        """
        Given a question ID, fetches its questions.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creates a question.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        """
        Updates a question.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially updates a question.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes a question.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().destroy(request, args, kwargs)