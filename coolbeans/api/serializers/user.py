"""
Serializers for user-models.

NB: Fields in user models, for security reasons, are serialized on a white-list basis.
"""
from coolbeans.api.serializers.base import BaseSerializer
from coolbeans.app.models import UserModel


class PublicUserSerializer(BaseSerializer):
    """
    A serializer for public view.
    """
    class Meta:
        model = UserModel
        fields = ('id', 'url', 'first_name', 'last_name')


class SelfUserSerializer(BaseSerializer):
    """
    A serializer for view of the owner or authorised personnel.
    """
    class Meta:
        model = UserModel
        fields = ('id', 'url', 'first_name', 'last_name', 'email')
