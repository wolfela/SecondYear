from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from coolbeans.api.serializers.user import PublicUserSerializer
from coolbeans.app.models import UserModel


class UserViewSet(GenericViewSet,
                  ListModelMixin,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin):
    """
    A ViewSet for user-related operations.
    """
    queryset = UserModel.objects.all()

    def get_serializer_class(self):
        """
        Returns the proper user to return, depending on the authentication status.
        :return:
        """
        # TODO Actually implement this
        return PublicUserSerializer

    def list(self, request, *args, **kwargs):
        """
        Lists all users.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creates an user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        """
        Updates an user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially updates an user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().create(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes an user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().destroy(request, args, kwargs)