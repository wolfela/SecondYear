from coolbeans.api.serializers.base import BaseSerializer
from coolbeans.app.models import QuestionModel


class QuestionSerializer(BaseSerializer):
    """
    A Question serializer.
    """

    class Meta:
        model = QuestionModel
        fields = '__all__'
        read_only_fields = ('creator', )

    def to_representation(self, instance):
        # TODO: Add different question types here
        pass
