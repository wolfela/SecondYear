from django.views import View
from coolbeans.app.forms import QuizForm
from coolbeans.app.models.quiz import QuizModel
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect


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

    def editQuiz(request, pk):
        quiz = get_object_or_404(QuizModel, pk=pk)
        return render(request, 'app/quiz/Quiz-Create.html', {'quiz': quiz})

    def saveQuiz(request, pk):
        instance = get_object_or_404(QuizModel, pk=pk)
        if request.method == 'POST':
            form = QuizForm(request.POST, instance=instance)
            if form.is_valid():
                questions = request.POST.getlist('questions')
                form.cleaned_data['questions'] = ','.join(questions)
                formcopy = QuizForm(request.POST.copy())
                formcopy.data['questions'] = ','.join(questions)
                formcopy.save()
                return HttpResponseRedirect('/')
            else:
                form = QuizForm()

class QuizAttemptView(View):

    def attemptQuiz(request, pk):
        instance = get_object_or_404(QuizModel, pk=pk)
        return HttpResponseRedirect(instance.questions[0])
