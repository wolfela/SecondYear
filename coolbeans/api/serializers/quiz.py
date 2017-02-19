from rest_framework.relations import HyperlinkedIdentityField

from coolbeans.api.serializers.base import BaseSerializer
from coolbeans.app.models import QuizModel


class QuizSerializer(BaseSerializer):
    """
    A Serializer for the quiz model.
    """
    questions = HyperlinkedIdentityField(
        view_name='quiz-questions-list',
        lookup_url_kwarg='quiz_pk'
    )

    class Meta:
        model = QuizModel
        fields = ('id', 'slug', 'title', 'description', 'creator', 'questions')
        read_only_fields = ('creator', )
