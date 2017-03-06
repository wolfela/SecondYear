from django.conf.urls import url
from django.views.generic import RedirectView

from coolbeans.app.views import base, user, question
from coolbeans.app.views.quiz import attempt
from coolbeans.app.views.quiz import editor

urlpatterns = [
    url(r'^$', base.IndexView.as_view()),
    # User functions
    url(r'^login/$', user.LoginView.as_view()),
    url(r'^logout/$', user.LogoutView.as_view()),
    url(r'^register/$', user.RegisterView.as_view()),
    url(r'^profile/(?P<id>[0-9]+)/$', user.ProfileView.as_view()),
    url(r'^profile/$', user.SelfProfileView.as_view()),
    url(r'^profile/edit/$', user.EditProfileView.as_view()),

    # Quiz functions
    url(r'^quiz', RedirectView.as_view(url="quiz/list")),
    url(r'^quiz/list$', attempt.QuizListView.as_view()),
    url(r'^quiz/(?P<id_or_slug>[a-z0-9]+(?:-[a-z0-9]+)*)/$', attempt.QuizDetailView.as_view()),
    url(r'^quiz/(?P<id_or_slug>[a-z0-9]+(?:-[a-z0-9]+)*)/attempt$', attempt.AttemptQuizView.as_view()),

    # Quiz editing functions
    url(r'^quiz/editor$', editor.QuizListView.as_view()),
    url(r'^quiz/editor/create$', editor.QuizCreateView.as_view()),
    url(r'^quiz/editor/(?P<id_or_slug>[a-z0-9]+(?:-[a-z0-9]+)*)/$', editor.QuestionListView.as_view()),
    url(r'^quiz/editor/(?P<id_or_slug>[a-z0-9]+(?:-[a-z0-9]+)*)/create_question$', editor.QuestionCreateView.as_view()),
    url(r'^quiz/editor/(?P<id_or_slug>[a-z0-9]+(?:-[a-z0-9]+)*)/(?P<question_id>[0-9]+)$', editor.QuestionEditView.as_view()),

    # Question editing functions
    url(r'^mcq/$', question.MCQCreateView.as_view()),
    url(r'^mcq2/$', question.MCQView.as_view()),
    url(r'^mcq/ajax/validate/$', question.validate, name='validate'),
    #url(r'^mcq/ajax/validatee/$', question.validatee, name='validatee'),

    # TODO: Admin routes
]