from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer


class BaseSerializer(DynamicModelSerializer, HyperlinkedModelSerializer):
    """
    A Base Serializer all serializers inherit.
    """
    pass
