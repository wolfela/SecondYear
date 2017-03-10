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

    # Question functions

    # Multiple Choice Questions
    url(r'^mc/$', question.MCCreateView.as_view(), name='mc'),
    url(r'^mc/preview/$', question.MCCreateView.previewMC, name='preview'),
    url(r'^mc/save/$', question.MCCreateView.saveMC, name='save'),
    url(r'^mc/question/(?P<pk>\d+)/$', question.MCQuestionView.show_question, name='mcquestion'),

    # True or False Questions
    url(r'^tf/$', question.TFCreateView.as_view(), name='tf'),
    url(r'^tf/preview/$', question.TFCreateView.previewTF, name='preview'),
    url(r'^tf/save/$', question.TFCreateView.saveTF, name='save'),
    url(r'^tf/question/(?P<pk>\d+)/$', question.TFQuestionView.show_question, name='tfquestion'),

    # Word Matching Questions
    url(r'^wm/$', question.WMCreateView.as_view(), name='wm'),
    url(r'^wm/preview/$', question.WMCreateView.previewWM, name='preview'),
    url(r'^wm/save/$', question.WMCreateView.saveWM, name='save'),
    url(r'^wm/question/(?P<pk>\d+)/$', question.WMQuestionView.show_question, name='wmquestion'),

    # Word Scramble Questions
    url(r'^ws/$', question.WSCreateView.as_view(), name='ws'),
    url(r'^ws/preview/$', question.WSCreateView.previewWS, name='preview'),
    url(r'^ws/save/$', question.WSCreateView.saveWS, name='save'),
    url(r'^ws/question/(?P<pk>\d+)/$', question.WSQuestionView.show_question, name='wsquestion'),

    # Gap Fill Questions
    url(r'^gf/$', question.GFCreateView.as_view(), name='gf'),
    url(r'^gf/preview/$', question.GFCreateView.previewGF, name='preview'),
    url(r'^gf/save/$', question.GFCreateView.saveGF, name='save'),
    url(r'^gf/question/(?P<pk>\d+)/$', question.GFQuestionView.show_question, name='gfquestion'),


    # TODO: Admin routes
]