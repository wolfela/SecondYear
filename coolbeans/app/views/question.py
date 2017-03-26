from django.views.generic import TemplateView
from django.template import RequestContext
from coolbeans.app.forms import MCForm, WMForm, WSForm, GFForm
from coolbeans.app.models.question import MultipleChoiceModel, WordScrambleQuestionModel, WordMatchingModel, GapFillQuestionModel, CrosswordQuestionModel, BaseQuestionModel
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
import json

class MCCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/MC-Creation.html"


    def submitMC(request):
        """
        Method for deciding what kind of submit it is and give formtype and question type
        :param type: type of question
        :param formtype: form type for this particular question
        :return: redirect to cancel or save
        """
        if 'save_form' in request.POST:
            return MCCreateView.save(request, 'MC', MCForm)
        elif 'cancel_form' in request.POST:
            return cancel(request, 'MC', MCForm)


    def save(request, type, formtype):
        """
        Method for saving Multiple Choice forms
        :param type: type of a question
        :param formtype: form type for this particular question
        :return: http response redirect back to quiz create
        """
        pathType = '/' + type

        if request.method == 'POST':
            form = formtype(request.POST)
            if form.is_valid():
                answers = request.POST.getlist('answers[]')
                form.cleaned_data['answers'] = ','.join(answers)
                formcopy = formtype(request.POST.copy())
                answers.append(request.POST.get('correct'))
                formcopy.data['answers'] = ','.join(answers)
                saved = formcopy.save()
                return HttpResponseRedirect('/quiz/edit/' + form.data['quiz'] + '/mc/' + str(saved.pk))
            else:
                form = formtype()

        return render(request, pathType, {'form': form}, context_instance=RequestContext(request))

class MCQuestionView(TemplateView):
    """
    A view for attempting Multiple Choice Questions
    """
    template_name = "app/question/MC-Display.html"

    def show_question(request, pk, score):
        """
        Get the question with given pk from the database and return the question form
        :param pk: primary key
        :param score: quiz attempt score
        :return: http response redirect to question display with the current score
        """
        question = get_object_or_404(MultipleChoiceModel, pk=pk)
        return render(request, 'app/question/MC-Display.html', {'question': question, 'score': score})

    def check_answer(request, pk, score):
        """
        Method for Multiple Choice answer checking in quiz attempts
        :param pk: primary key
        :param score: current score
        :return: http response redirect to the next question with the updated score
        """
        question = get_object_or_404(MultipleChoiceModel, pk=pk)
        answer = request.POST.get('answers')
        if question.check_answer(answer):
            score = int(score) + 1
        return HttpResponseRedirect('/quiz/attempt/' + question.quiz + '/next/' + question.position + '/' + str(score))

class MCPreviewView(TemplateView):
    """
    A view for previewing Multiple Choice Questions
    """
    template_name = "app/question/MC-Preview.html"


class WMCreateView(TemplateView):
    """
    A view for creating Word Match Questions
    """
    template_name = "app/question/WM-Creation.html"

    def submitWM(request):
        """
        decide what kind of submit it is and give formtype and question type
        :param type: type of question
        :param formtype: form type for this particular question
        :return: redirect to cancel or save
        """
        if 'save_form' in request.POST:
            return WMCreateView.save(request, 'WM', WMForm)
        elif 'cancel_form' in request.POST:
            return cancel(request, 'WM', WMForm)


    def save(request, type, formtype):
        """
        Method for saving Word Match forms
        :param type: type of a question
        :param formtype: form type for this particular question
        :return: http response redirect back to quiz create
        """
        pathType = '/' + type

        if request.method == 'POST':
            form = formtype(request.POST)
            if form.is_valid():
                listA = request.POST.getlist('listA[]')
                form.cleaned_data['listA'] = ','.join(listA)
                formcopy = formtype(request.POST.copy())
                formcopy.data['listA'] = ','.join(listA)
                listB = request.POST.getlist('listB[]')
                form.cleaned_data['listB'] = ','.join(listB)
                formcopy.data['listB'] = ','.join(listB)
                saved = formcopy.save()
                return HttpResponseRedirect('/quiz/edit/' + form.data['quiz'] + '/wm/' + str(saved.pk))
            else:
                form = formtype()
        return render(request, pathType, {'form': form}, context_instance=RequestContext(request))



class WMQuestionView(TemplateView):
    """
    A view for attempting Word Match Questions
    """
    template_name = "app/question/WM-Display.html"

    def show_question(request, pk, score):
        """
        Get the question with given pk from the database and return the question form
        :param pk: primary key
        :param score: quiz attempt score
        :return: http response redirect to question display with the current score
        """
        question = get_object_or_404(WordMatchingModel, pk=pk)
        return render(request, 'app/question/WM-Display.html', {'question': question, 'score': score})

    def check_answer(request, pk, score):
        """
        Method for Word Match answer checking in quiz attempts
        :param pk: primary key
        :param score: current score
        :return: http response redirect to the next question with the updated score
        """
        question = get_object_or_404(WordMatchingModel, pk=pk)
        answerA = request.POST.get('listA')
        aA = answerA.split(",")
        answerB = request.POST.get('listB')
        aB = answerB.split(",")
        if question.check_answer(aA, aB):
            score = int(score) + 1
        return HttpResponseRedirect('/quiz/attempt/' + question.quiz + '/next/' + question.position + '/' + str(score))

class WMPreviewView(TemplateView):
    """
    A view for previewing Word Match Questions
    """
    template_name = "app/question/WM-Preview.html"



class WSCreateView(TemplateView):
    """
    A view for creating Word Scramble Questions
    """
    template_name = "app/question/WS-Creation.html"

    def submitWS(request):
        """
        decide what kind of submit it is and give formtype and question type
        :param type: type of question
        :param formtype: form type for this particular question
        :return: redirect to cancel or save
        """
        if 'save_form' in request.POST:
            return WSCreateView.save(request, 'WS', WSForm)
        elif 'cancel_form' in request.POST:
            return cancel(request, 'WS', WSForm)

    def save(request, type, formtype):
        """
        Method for saving Word Scramble forms
        :param type: type of a question
        :param formtype: form type for this particular question
        :return: http response redirect back to quiz create
        """
        pathType = '/' + type

        if request.method == 'POST':
            form = formtype(request.POST)
            if form.is_valid():
                saved = form.save()
                return HttpResponseRedirect('/quiz/edit/' + form.data['quiz'] + '/ws/' + str(saved.pk))
            else:
                form = formtype()

        return render(request, pathType, {'form': form}, context_instance=RequestContext(request))




class WSQuestionView(TemplateView):
    """
    A view for attempting Word Scramble Questions
    """
    template_name = "app/question/WS-Display.html"

    def show_question(request, pk, score):
        """
        Get the question with given pk from the database and return the question form
        :param pk: primary key
        :param score: quiz attempt score
        :return: http response redirect to question display with the current score
        """
        question = get_object_or_404(WordScrambleQuestionModel, pk=pk)
        return render(request, 'app/question/WS-Display.html', {'question': question, 'score': score})

    def check_answer(request, pk, score):
        """
        Method for Word Scramble answer checking in quiz attempts
        :param pk: primary key
        :param score: current score
        :return: http response redirect to the next question with the updated score
        """
        question = get_object_or_404(WordScrambleQuestionModel, pk=pk)
        answer = request.POST.get('answer').split(",")
        if question.check_answer(answer):
            score = int(score) + 1
        return HttpResponseRedirect('/quiz/attempt/' + question.quiz + '/next/' + question.position + '/' + str(score))


class WSPreviewView(TemplateView):
    """
    A view for previewing Word Scramble Questions
    """
    template_name = "app/question/WS-Preview.html"


class GFCreateView(TemplateView):
    """
    A view for creating Gap Fill Questions
    """
    template_name = "app/question/GF-Creation.html"

    def submitGF(request):
        """
        decide what kind of submit it is and give formtype and question type
        :param type: type of question
        :param formtype: form type for this particular question
        :return: redirect to cancel or save
        """
        if 'save_form' in request.POST:
            return GFCreateView.save(request, 'gf', GFForm)
        elif 'cancel_form' in request.POST:
            return cancel(request, 'gf', GFForm)

    def save(request, type, formtype):
        """
        Method for saving Gap Fill forms
        :param type: type of a question
        :param formtype: form type for this particular question
        :return: http response redirect back to quiz create
        """
        pathCreation = 'app/question/' + type + '-Creation.html'
        pathType = '/' + type
        if request.method == 'POST':
            form = formtype(request.POST)
            if form.is_valid():
                saved = form.save()
                return HttpResponseRedirect('/quiz/edit/' + form.data['quiz'] + '/gf/' + str(saved.pk))



class GFQuestionView(TemplateView):
    """
    A view for attempting Gap Fill Questions
    """
    template_name = "app/question/GF-Display.html"

    def show_question(request, pk, score):
        """
        Get the question with given pk from the database and return the question form
        :param pk: primary key
        :param score: quiz attempt score
        :return: http response redirect to question display with the current score
        """
        question = get_object_or_404(GapFillQuestionModel, pk=pk)
        gapfilled = question.question.split(" ")
        gaps = question.gaps
        for index, word in enumerate(gapfilled):
            if word in question.gaps:
                gapfilled[index] = '$$ $$'

        return render(request, 'app/question/GF-Display.html', {'question': question, 'score': score, 'gapfilled': gapfilled, 'gaps': gaps})

    def check_answer(request, pk, score):
        """
        Method for Gap Fill answer checking in quiz attempts
        :param pk: primary key
        :param score: current score
        :return: http response redirect to the next question with the updated score
        """
        question = get_object_or_404(GapFillQuestionModel, pk=pk)
        answer = request.POST.getlist('answers')
        if question.check_answer(answer):
            score = int(score) + 1
        return HttpResponseRedirect('/quiz/attempt/' + question.quiz + '/next/' + question.position + '/' + str(score))


class GFPreviewView(TemplateView):
    """
    A view for previewing Gap Fill Questions
    """
    template_name = "app/question/GF-Preview.html"



class CWCreateView(TemplateView):
    """
    A view for creating Crossword Questions
    """
    template_name = "app/question/CW-Creation.html"

    def submit(request):
        """
        Method for submitting and saving crossword questions through json data
        :return: url back to quiz create
        """
        json_data = json.loads(request.body.decode('utf-8'))
        base = BaseQuestionModel.objects.create()
        quiz =""
        pos=""

        for element in json_data['q']:
            quiz = element['quiz']
            pos = element['pos']

        for element in json_data['data']:
            CrosswordQuestionModel.objects.create(question=base, direction=element['direction'], length=element['length'],
                                                 x=element['x'],y=element['y'],clue=element['clue'],
                                                 answer=element['word'], quiz=quiz, position=pos)

        message = '/quiz/edit/' + quiz + '/cw/' + str(base.pk)
        return HttpResponse(message)


class CWQuestionView(TemplateView):
    """
    A view for attempting Crossword Questions
    """
    template_name = "app/question/CW-Display.html"

    def show_question(request, pk, score):
        """
        Get the question with given pk from the database and return the json data
        :param pk: primary key
        :param score: current score
        :return: json crossword data
        """
        question = get_object_or_404(BaseQuestionModel, pk=pk)
        all = question.crosswordquestionmodel_set.all()
        dictionaries = [obj.as_dict() for obj in all]

        return JsonResponse({'data': dictionaries})

    def check_answer(request, pk, score):
        """
        Method for checking the answers in a crossword
        :param pk: primary key
        :param score: current score
        :return: updated score
        """
        question = get_object_or_404(BaseQuestionModel, pk=pk)
        json_data = json.loads(request.body.decode('utf-8'))
        if question.check_answer(json_data):
            score = int(score) + 1

        return HttpResponse(str(score))

class CWPreviewView(TemplateView):
    """
    A view for previewing Crossword Questions
    """
    template_name = "app/question/CW-Preview.html"

def cancel(request, type, formtype):
    """
    Global cancel method for going back from question editor to quiz editor
    :param request:
    :param type: type of question
    :param formtype: formtype
    :return: http response redirect back to quiz editor
    """
    form = formtype(request.POST)
    return HttpResponseRedirect('/quiz/edit/' + form.data['quiz'])