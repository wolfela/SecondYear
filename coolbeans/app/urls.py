from django.conf.urls import url
from django.views.generic import RedirectView

from coolbeans.app.views import base, question
from coolbeans.app.views.quiz import quiz

urlpatterns = [
    url(r'^$', base.IndexView.as_view()),

    # Quiz functions
    # url(r'^quiz/(?P<pk>\d+)/$', attempt.QuizView.as_view()),

    # Quiz editing functions
    url(r'^quiz/create$', quiz.QuizCreateView.load),
    url(r'^quiz/edit/(?P<pk>\d+)/$', quiz.QuestionEditView.editQuiz, name='editquiz'),
    url(r'^quiz/edit/(?P<pk>\d+)/save/$', quiz.QuestionEditView.saveQuiz, name='savequiz'),
    url(r'^quiz/attempt/(?P<pk>\d+)/$', quiz.QuizAttemptView.attemptQuiz, name='attemptquiz'),
    url(r'^quiz/attempt/(?P<pk>\d+)/next/(?P<i>\d+)/$', quiz.QuizAttemptView.nextQuestion, name='nextquestion'),

    # Question functions

    # Multiple Choice Questions
    url(r'^mc/$', question.MCCreateView.as_view(), name='mc'),
    url(r'^mc/submit/$', question.MCCreateView.submitMC, name='submit'),
    url(r'^mc/question/(?P<pk>\d+)/$', question.MCQuestionView.show_question, name='mcquestion'),

    # Word Matching Questions
    url(r'^wm/$', question.WMCreateView.as_view(), name='wm'),
    url(r'^wm/submit/$', question.WMCreateView.submitWM, name='submit'),
    url(r'^wm/question/(?P<pk>\d+)/$', question.WMQuestionView.show_question, name='wmquestion'),

    # Word Scramble Questions
    url(r'^ws/$', question.WSCreateView.as_view(), name='ws'),
    url(r'^ws/submit/$', question.WSCreateView.submitWS, name='submit'),
    url(r'^ws/question/(?P<pk>\d+)/$', question.WSQuestionView.show_question, name='wsquestion'),

    # Gap Fill Questions
    url(r'^gf/$', question.GFCreateView.as_view(), name='gf'),
    url(r'^gf/submit/$', question.GFCreateView.submitGF, name='submit'),
    url(r'^gf/question/(?P<pk>\d+)/$', question.GFQuestionView.show_question, name='gfquestion'),


    # TODO: Admin routes
]