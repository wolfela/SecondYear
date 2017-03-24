from django.conf.urls import url
from django.views.generic import RedirectView

from coolbeans.app.views import base, question
from coolbeans.app.views.quiz import quiz

urlpatterns = [
    url(r'^$', quiz.QuizAttemptView.findQuizPage, name='indexpage'),

    # Quiz functions
    # url(r'^quiz/(?P<pk>\d+)/$', attempt.QuizView.as_view()),

    # Quiz editing functions
    url(r'^quiz/create/$', quiz.QuizCreateView.load),
    url(r'^quiz/edit/(?P<pk>\d+)/$', quiz.QuestionEditView.editQuiz, name='editquiz'),
    url(r'^quiz/edit/(?P<pk>\d+)/(?P<questiontype>.*)/(?P<questionid>\d+)/$', quiz.QuestionEditView.editQuiz, name='editquizwithquestion'),
    url(r'^quiz/edit/(?P<pk>\d+)/submit/$', quiz.QuestionEditView.submitQuiz, name='submitquiz'),
    url(r'^quiz/attempt/(?P<pk>\d+)/$', quiz.QuizAttemptView.attemptQuiz, name='attemptquiz'),
    url(r'^quiz/attempt/(?P<pk>\d+)/next/(?P<i>\d+)/(?P<score>\d+)/$', quiz.QuizAttemptView.nextQuestion, name='nextquestion'),
    url(r'^quiz/score/(?P<pk>\d+)/(?P<score>\d+)', quiz.QuizAttemptView.score, name='resultpage'),
    url(r'^quiz/(?P<pk>\d+)/showid/$', quiz.QuestionEditView.showId, name='showId'),
    url(r'^quiz/find/$', quiz.QuizAttemptView.findQuizPage, name='findQuiz'),
    url(r'^quiz/find/go/$', quiz.QuizAttemptView.findQuiz, name='findQuiz'),

    # Question functions

    # Multiple Choice Questions
    url(r'^mc/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.MCCreateView.as_view(), name='mc'),
    url(r'^mc/submit/$', question.MCCreateView.submitMC, name='submit'),
    url(r'^mc/preview/$', question.MCPreviewView.as_view(), name='preview'),
    url(r'^mc/question/(?P<pk>\d+)/(?P<score>\d+)/$', question.MCQuestionView.show_question, name='mcquestion'),
    url(r'^mc/question/(?P<pk>\d+)/(?P<score>\d+)/check/$', question.MCQuestionView.check_answer, name='checkmc'),

    # Word Matching Questions
    url(r'^wm/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.WMCreateView.as_view(), name='wm'),
    url(r'^wm/submit/$', question.WMCreateView.submitWM, name='submit'),
    url(r'^wm/preview/$', question.WMPreviewView.as_view(), name='preview'),
    url(r'^wm/question/(?P<pk>\d+)/(?P<score>\d+)/$', question.WMQuestionView.show_question, name='mcquestion'),
    url(r'^wm/question/(?P<pk>\d+)/(?P<score>\d+)/check/$', question.WMQuestionView.check_answer, name='checkmc'),

    # Word Scramble Questions
    url(r'^ws/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.WSCreateView.as_view(), name='ws'),
    url(r'^ws/submit/$', question.WSCreateView.submitWS, name='submit'),
    url(r'^ws/preview/$', question.WSPreviewView.as_view(), name='preview'),
    url(r'^ws/question/(?P<pk>\d+)/(?P<score>\d+)/$', question.WSQuestionView.show_question, name='mcquestion'),
    url(r'^ws/question/(?P<pk>\d+)/(?P<score>\d+)/check/$', question.WSQuestionView.check_answer, name='checkmc'),

    # Gap Fill Questions
    url(r'^gf/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.GFCreateView.as_view(), name='gf'),
    url(r'^gf/submit/$', question.GFCreateView.submitGF, name='submit'),
    url(r'^gf/preview/$', question.GFPreviewView.as_view(), name='preview'),
    url(r'^gf/question/(?P<pk>\d+)/(?P<score>\d+)/$', question.GFQuestionView.show_question, name='mcquestion'),
    url(r'^gf/question/(?P<pk>\d+)/(?P<score>\d+)/check/$', question.GFQuestionView.check_answer, name='checkmc'),

    # Crossword Questions
    url(r'^cw/(?P<quizid>\d+)/(?P<pos>\d+)/$', question.CWCreateView.as_view(), name='cw'),
    url(r'^cw/submit/$', question.CWCreateView.submit, name='submit'),
    url(r'^cw/preview/$', question.CWPreviewView.as_view(), name='preview'),
    url(r'^cw/question/(?P<pk>\d+)/(?P<score>\d+)/$', question.CWQuestionView.as_view(), name='cwquestion'),
    url(r'^cw/question/(?P<pk>\d+)/(?P<score>\d+)/show/$', question.CWQuestionView.show_question, name='cwquestionn'),
    url(r'^cw/question/(?P<pk>\d+)/(?P<score>\d+)/check_answer/$', question.CWQuestionView.check_answer, name='checkcw')




    # TODO: Admin routes
]