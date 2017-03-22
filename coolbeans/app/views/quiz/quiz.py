from django.views import View
from coolbeans.app.forms import QuizForm
from coolbeans.app.models.quiz import QuizModel
from coolbeans.app.views.question import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse


class QuizListView(View):
    """
    A view for listing all quizzes this user is allowed to edit.
    """
    pass


class QuizCreateView(View):
    """
    A view for creating quizzes.
    """
    template_name = "app/quiz/Quiz-Create.html"

    def load(request):
        form = QuizForm(request.POST)
        quiz = form.save()
        string = 'edit/' + str(quiz.pk)
        return redirect(string)

class QuestionEditView(View):
    template_name = "app/quiz/Quiz-Create.html"

    def submitQuiz(request, pk):
        if 'save_form' in request.POST:
            return QuestionEditView.saveQuiz(request, pk)
        elif 'add_question' in request.POST:
            return QuestionEditView.addQuestion(request, pk)

    def addQuestion(request, pk):
        quiz = get_object_or_404(QuizModel, pk=pk)
        quiz.title = request.POST.get('title')
        quiz.language = request.POST.get('language')
        quiz.save()
        type = request.POST.get('type')
        return HttpResponseRedirect('/' + type + '/' + str(pk) + '/' + str(len(quiz.questions)))

    def editQuiz(request, pk, questiontype='', questionid=''):
        quiz = get_object_or_404(QuizModel, pk=pk)
        if (questiontype is not '' and questionid is not ''):
            quiz.questions.append(questiontype + '/question/' + str(questionid))
            quiz.save()
            print('QUESTIONS:')
            print(quiz.questions)
        return render(request, 'app/quiz/Quiz-Create.html', {'quiz': quiz})

    def saveQuiz(request, pk):
        instance = get_object_or_404(QuizModel, pk=pk)
        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                instance.title = form.data['title']
                instance.language = form.data['language']
                instance.save()
                return HttpResponseRedirect('/')
            else:
                form = QuizForm()

class QuizAttemptView(View):

    def attemptQuiz(request, pk):
        instance = get_object_or_404(QuizModel, pk=pk)
        print('QUESTIONS:')
        print(instance.questions)
        return HttpResponseRedirect('/' + instance.questions[0])

    def nextQuestion(request, pk, i):
        instance = get_object_or_404(QuizModel, pk=pk)
        if (int(i)+1 < len(instance.questions)):
            if request.is_ajax():
                message = '/' + instance.questions[int(i)+1]
                return HttpResponse(message)
            else:
                return HttpResponseRedirect('/' + instance.questions[int(i)+1])
        else:
            if request.is_ajax():
                message = '/'
                return HttpResponse(message)
            else:
                return HttpResponseRedirect('/')