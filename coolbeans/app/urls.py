from django.conf.urls import url
from django.views.generic import RedirectView

from coolbeans.app.views import base, quiz, user, question

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
    url(r'^quiz/list$', quiz.QuizListView.as_view()),
    url(r'^quiz/(?P<id_or_slug>[a-z0-9]+(?:-[a-z0-9]+)*)/$', quiz.QuizDetailView.as_view()),
    url(r'^quiz/(?P<id_or_slug>[a-z0-9]+(?:-[a-z0-9]+)*)/attempt$', quiz.AttemptQuizView.as_view()),

    # Quiz editing functions
    url(r'^quiz/create$', quiz.QuizCreateView.as_view()),
    url(r'^quiz/(?P<id_or_slug>[a-z0-9]+(?:-[a-z0-9]+)*)/edit$', quiz.QuizEditView.as_view()),


    # TODO: Admin routes
]