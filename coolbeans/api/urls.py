from django.conf.urls import url
from rest_framework.compat import include
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter

from coolbeans.api.views.question import QuestionViewSet
from coolbeans.api.views.quiz import QuizViewSet
from coolbeans.api.views.user import UserViewSet

router = SimpleRouter()

# User routes
router.register(r'users', UserViewSet, base_name='user')

# Quiz routes
router.register(r'quizzes', QuizViewSet, base_name='quiz')

# Question routes
quiz_router = NestedSimpleRouter(router, r'quizzes', lookup='quiz')
quiz_router.register(r'questions', QuestionViewSet, base_name='quiz-questions')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(quiz_router.urls))
]