from django.views import View
from coolbeans.app.forms import QuizForm
from coolbeans.app.models.quiz import QuizModel
from coolbeans.app.models.question import MultipleChoiceModel, WordScrambleQuestionModel, WordMatchingModel, GapFillQuestionModel, CrosswordQuestionModel, BaseQuestionModel
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
        """
        Load the right quiz edit page with an id
        :return: redirect to quiz edit page
        """
        form = QuizForm(request.POST)
        quiz = form.save()
        string = '/quiz/edit/' + str(quiz.pk)
        return redirect(string)

class QuestionEditView(View):
    """
    A view for editing quizzes
    """
    template_name = "app/quiz/Quiz-Create.html"

    def submitQuiz(request, pk):
        """
        Method for handling different submit quiz types
        :param pk: primary key
        :return: redirect to save quiz, add question or cancel
        """
        if 'save_form' in request.POST:
            return QuestionEditView.saveQuiz(request, pk)
        elif 'add_question' in request.POST:
            return QuestionEditView.addQuestion(request, pk)
        elif 'cancel_form' in request.POST:
            return QuestionEditView.cancel(request, pk)

    def addQuestion(request, pk):
        """
        Method for adding questions to quizzes
        :param pk: primary key
        :return: http response redirect back to quiz edit page
        """
        quiz = get_object_or_404(QuizModel, pk=pk)
        quiz.title = request.POST.get('title')
        quiz.language = request.POST.get('language')
        quiz.author = request.POST.get('author')
        quiz.save()
        type = request.POST.get('type')
        return HttpResponseRedirect('/' + type + '/' + str(pk) + '/' + str(len(quiz.questions)))

    def editQuiz(request, pk, questiontype='', questionid=''):
        """
        Method for displaying edit quiz page with the updated question list
        :param pk: primary key
        :param questiontype: type of a question
        :param questionid: question id
        :return: updated view
        """
        quiz = get_object_or_404(QuizModel, pk=pk)
        if questiontype is not '' and questionid is not '':
            if questiontype == 'mc':
                questiontitle = "Multiple Choice"
            elif questiontype == 'ws':
                questiontitle = "Word Scramble"
            elif questiontype == 'wm':
                questiontitle = "Word Match"
            elif questiontype == 'cw':
                questiontitle = "Crossword"
            elif questiontype == 'gf':
                questiontitle = "Gapfill"
            quiz.questions.append(questiontype + '/question/' + str(questionid))
            quiz.questiontitles.append(questiontitle)
            quiz.save()
        return render(request, 'app/quiz/Quiz-Create.html', {'quiz': quiz})

    def saveQuiz(request, pk):
        """
        Method for saving the quiz
        :param pk: primary key
        :return: http response redirect to show id page
        """
        instance = get_object_or_404(QuizModel, pk=pk)
        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                instance.title = form.data['title']
                instance.language = form.data['language']
                instance.save()
                return HttpResponseRedirect('/quiz/' + pk + '/showid/')
            else:
                form = QuizForm()

    def showId(request, pk):
        """
        Method for displaying the show id page
        :param pk: primary key
        :return: return the quiz id page with form data
        """
        quiz = get_object_or_404(QuizModel, pk=pk)
        return render(request, 'app/quiz/Quiz-ID.html', {'quiz': quiz})

    def cancel(request, pk):
        return HttpResponseRedirect('/')


class QuizAttemptView(View):
    """
    A view for attempting quizzes
    """

    def score(request, pk, score):
        """
        Method for displaying the results page
        :param pk: primary key
        :param score: final score
        :return: upadated results view with the forms data
        """
        quiz = get_object_or_404(QuizModel, pk=pk)
        questioncount = len(quiz.questions)
        return render(request, 'app/quiz/Quiz-Result.html', {'score': score, 'quiz': quiz, 'questioncount': questioncount})

    def attemptQuiz(request, pk):
        """
        Method for starting the quiz attempt
        :param pk: primary key
        :return: redirect to the first question
        """
        instance = get_object_or_404(QuizModel, pk=pk)
        return HttpResponseRedirect('/' + instance.questions[0] + '/0')

    def nextQuestion(request, pk, i, score):
        """
        Method that returns the next question
        :param pk: primary key
        :param i: position in the quiz
        :param score: current score
        :return: http response redirect to the next question
        """
        instance = get_object_or_404(QuizModel, pk=pk)
        if (int(i)+1 < len(instance.questions)):
            if request.is_ajax():
                message = '/' + instance.questions[int(i)+1] + '/' + score
                return HttpResponse(message)
            else:
                return HttpResponseRedirect('/' + instance.questions[int(i)+1] + '/' + score)
        else:
            if request.is_ajax():
                message = '/quiz/score' + score
                return HttpResponse(message)
            else:
                return HttpResponseRedirect('/quiz/score/' + pk + '/' + score)

    def findQuizPage(request):
        """
        Main/Find quiz page display
        :return: find quiz template
        """
        return render(request, 'app/quiz/Quiz-Find.html')

    def findQuiz(request):
        """
        Method for redirecting to the searched quiz or making an alert if it doesnt exist
        :return: http response redirect to the quiz attempt for that quiz
        """
        pk = request.POST.get('pk')
        if(pk.isdigit()):
            quiz = QuizModel.objects.filter(pk=pk)
            if(quiz):
                return HttpResponseRedirect('/quiz/attempt/' + pk + '/')

        return render(request, 'app/quiz/Quiz-Find.html', {'alert': "Wrong Quiz Code. Try again!"})

