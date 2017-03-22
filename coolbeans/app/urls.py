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
    url(r'^quiz/edit/(?P<pk>\d+)/(?P<questiontype>.*)/(?P<questionid>\d+)/$', quiz.QuestionEditView.editQuiz, name='editquizwithquestion'),
    url(r'^quiz/edit/(?P<pk>\d+)/submit/$', quiz.QuestionEditView.submitQuiz, name='submitquiz'),
    url(r'^quiz/attempt/(?P<pk>\d+)/$', quiz.QuizAttemptView.attemptQuiz, name='attemptquiz'),
    url(r'^quiz/attempt/(?P<pk>\d+)/next/(?P<i>\d+)/(?P<score>\d+)/$', quiz.QuizAttemptView.nextQuestion, name='nextquestion'),
    url(r'^quiz/score/(?P<score>\d+)', quiz.QuizAttemptView.score, name='resultpage'),
    # Question functions

    # Multiple Choice Questions
    url(r'^mc/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.MCCreateView.as_view(), name='mc'),
    url(r'^mc/submit/$', question.MCCreateView.submitMC, name='submit'),
    url(r'^mc/question/(?P<pk>\d+)/(?P<score>\d+)/$', question.MCQuestionView.show_question, name='mcquestion'),
    url(r'^mc/question/(?P<pk>\d+)/(?P<score>\d+)/check/$', question.MCQuestionView.check_answer, name='checkmc'),

    # Word Matching Questions
    url(r'^wm/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.WMCreateView.as_view(), name='wm'),
    url(r'^wm/submit/$', question.WMCreateView.submitWM, name='submit'),
<<<<<<< HEAD
    url(r'^wm/preview/$', question.WMPreviewView.as_view(), name='preview'),
    url(r'^wm/question/(?P<pk>\d+)/(?P<score>\d+)/$', question.WMQuestionView.show_question, name='wmquestion'),
=======
    url(r'^wm/question/(?P<pk>\d+)/$', question.WMQuestionView.show_question, name='wmquestion'),
>>>>>>> 32e19497fd6a808fd63a8976eb076a2a5c7b902e

    # Word Scramble Questions
    url(r'^ws/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.WSCreateView.as_view(), name='ws'),
    url(r'^ws/submit/$', question.WSCreateView.submitWS, name='submit'),
    url(r'^ws/question/(?P<pk>\d+)/$', question.WSQuestionView.show_question, name='wsquestion'),

    # Gap Fill Questions
    url(r'^gf/$', question.GFCreateView.as_view(), name='gf'),
    url(r'^gf/submit/$', question.GFCreateView.submitGF, name='submit'),
    url(r'^gf/question/(?P<pk>\d+)/$', question.GFQuestionView.show_question, name='gfquestion'),

    # Crossword Questions
    url(r'^cw/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.CWCreateView.as_view(), name='cw'),
    url(r'^cw/submit/$', question.CWCreateView.submit, name='submit'),
    url(r'^cw/preview/$', question.CWPreviewView.as_view(), name='preview'),
    url(r'^cw/question/(?P<pk>\d+)/$', question.CWQuestionView.as_view(), name='cwquestion'),
    url(r'^cw/question/(?P<pk>\d+)/show/$', question.CWQuestionView.show_question, name='cwquestionn'),




    # TODO: Admin routes
]