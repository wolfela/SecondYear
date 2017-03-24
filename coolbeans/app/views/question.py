from django.views.generic import TemplateView
from django.template import RequestContext

from coolbeans.app.forms import MCForm, WMForm, WSForm, GFForm
from coolbeans.app.models.question import MultipleChoiceModel, WordScrambleQuestionModel, WordMatchingModel, GapFillQuestionModel, CrosswordQuestionModel, BaseQuestionModel
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
import json

def CreateView(type):
    return eval(type)

class MCCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/MC-Creation.html"

    def get_template(request):
        return "app/question/MC-Creation.html"

    def submitMC(request):
        return MCCreateView.submit(request, 'MC', MCForm)

    def submit(request, type, formtype):
        if 'save_form' in request.POST:
            return MCCreateView.save(request, type, formtype)
        elif 'cancel_form' in request.POST:
            return cancel(request, type, formtype)


    def save(request, type, formtype):
        pathCreation = 'app/question/' + type + '-Creation.html'
        pathType = '/' + type
        """
        Method for saving the question, right now its a preview as well, to be fixed
        :return:
        """
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
    template_name = "app/question/MC-Display.html"

    def show_question(request, pk, score):
        question = get_object_or_404(MultipleChoiceModel, pk=pk)
        return render(request, 'app/question/MC-Display.html', {'question': question, 'score': score})

    def check_answer(request, pk, score):
        question = get_object_or_404(MultipleChoiceModel, pk=pk)
        answer = request.POST.get('answers')
        if question.check_answer(answer):
            score = int(score) + 1
        return HttpResponseRedirect('/quiz/attempt/' + question.quiz + '/next/' + question.position + '/' + str(score))

class MCPreviewView(TemplateView):
    template_name = "app/question/MC-Preview.html"


class WMCreateView(TemplateView):
    """
    A view for creating Word Match Questions
    """
    template_name = "app/question/WM-Creation.html"


    def submitWM(request):
        return WMCreateView.submit(request, 'WM', WMForm)

    def submit(request, type, formtype):
        if 'save_form' in request.POST:
            return WMCreateView.save(request, type, formtype)
        elif 'cancel_form' in request.POST:
            return cancel(request, type, formtype)


    def save(request, type, formtype):
        pathCreation = 'app/question/' + type + '-Creation.html'
        pathType = '/' + type
        """
        Method for saving the question, right now its a preview as well, to be fixed
        :return:
        """
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
    template_name = "app/question/WM-Display.html"

    def show_question(request, pk, score):
        question = get_object_or_404(WordMatchingModel, pk=pk)
        return render(request, 'app/question/WM-Display.html', {'question': question, 'score': score})

    def check_answer(request, pk, score):
        question = get_object_or_404(WordMatchingModel, pk=pk)
        answerA = request.POST.get('listA')
        aA = answerA.split(",")
        answerB = request.POST.get('listB')
        aB = answerB.split(",")
        if question.check_answer(aA, aB):
            score = int(score) + 1
        return HttpResponseRedirect('/quiz/attempt/' + question.quiz + '/next/' + question.position + '/' + str(score))

class WMPreviewView(TemplateView):
    template_name = "app/question/WM-Preview.html"



class WSCreateView(TemplateView):
    """
    A view for creating Word Scramble Questions
    """
    template_name = "app/question/WS-Creation.html"


    def submitWS(request):
        return WSCreateView.submit(request, 'WS', WSForm)

    def save(request, type, formtype):
        pathCreation = 'app/question/' + type + '-Creation.html'
        pathType = '/' + type
        """
        Method for saving the question, right now its a preview as well, to be fixed
        :return:
        """
        if request.method == 'POST':
            form = formtype(request.POST)
            if form.is_valid():
                saved = form.save()
                return HttpResponseRedirect('/quiz/edit/' + form.data['quiz'] + '/ws/' + str(saved.pk))
            else:
                form = formtype()

        return render(request, pathType, {'form': form}, context_instance=RequestContext(request))

    def submit(request, type, formtype):
        if 'save_form' in request.POST:
            return WSCreateView.save(request, type, formtype)
        elif 'cancel_form' in request.POST:
            return cancel(request, type, formtype)


class WSQuestionView(TemplateView):
    template_name = "app/question/WS-Display.html"

    def show_question(request, pk, score):
        question = get_object_or_404(WordScrambleQuestionModel, pk=pk)
        return render(request, 'app/question/WS-Display.html', {'question': question, 'score': score})

    def check_answer(request, pk, score):
        question = get_object_or_404(WordScrambleQuestionModel, pk=pk)
        answer = request.POST.get('answer').split(",")
        if question.check_answer(answer):
            score = int(score) + 1
        return HttpResponseRedirect('/quiz/attempt/' + question.quiz + '/next/' + question.position + '/' + str(score))


class WSPreviewView(TemplateView):
    template_name = "app/question/WS-Preview.html"


class GFCreateView(TemplateView):
    """
    A view for creating Word Scramble Questions
    """
    template_name = "app/question/GF-Creation.html"

    def submitGF(request):
        if 'save_form' in request.POST:
            return GFCreateView.save(request, 'gf', GFForm)
        elif 'cancel_form' in request.POST:
            return cancel(request, 'gf', GFForm)

    def save(request, type, formtype):
        pathCreation = 'app/question/' + type + '-Creation.html'
        pathType = '/' + type
        if request.method == 'POST':
            form = formtype(request.POST)
            if form.is_valid():
                saved = form.save()
                return HttpResponseRedirect('/quiz/edit/' + form.data['quiz'] + '/gf/' + str(saved.pk))



class GFQuestionView(TemplateView):
    template_name = "app/question/GF-Display.html"

    def show_question(request, pk, score):
        question = get_object_or_404(GapFillQuestionModel, pk=pk)
        gapfilled = question.question.split(" ")
        for index, word in enumerate(gapfilled):
            if word in question.gaps:
                gapfilled[index] = '$$ $$'

        return render(request, 'app/question/GF-Display.html', {'question': question, 'score': score, 'gapfilled': gapfilled})

    def check_answer(request, pk, score):
        question = get_object_or_404(GapFillQuestionModel, pk=pk)
        answer = request.POST.getlist('answers')
        if question.check_answer(answer):
            score = int(score) + 1
        return HttpResponseRedirect('/quiz/attempt/' + question.quiz + '/next/' + question.position + '/' + str(score))


class GFPreviewView(TemplateView):
    template_name = "app/question/GF-Preview.html"


class CWPreviewView(TemplateView):
    template_name = "app/question/CW-Preview.html"


class CWCreateView(TemplateView):
    """
    A view for creating Word Scramble Questions
    """
    template_name = "app/question/CW-Creation.html"

    def submit(request):
        json_data = json.loads(request.body.decode('utf-8'))
        print(json_data)
        base = BaseQuestionModel.objects.create()

        quiz =""
        pos=""

        for element in json_data['q']:
            quiz = element['quiz']
            pos = element['pos']

        print(pos)

        for element in json_data['data']:
            CrosswordQuestionModel.objects.create(question=base, direction=element['direction'], length=element['length'],
                                                 x=element['x'],y=element['y'],clue=element['clue'],
                                                 answer=element['word'], quiz=quiz, position=pos)

        print(base.id)
        message = '/quiz/edit/' + quiz + '/cw/' + str(base.pk)
        return HttpResponse(message)


class CWQuestionView(TemplateView):
    template_name = "app/question/CW-Display.html"

    def show_question(request, pk, score):

        question = get_object_or_404(BaseQuestionModel, pk=pk)
        all = question.crosswordquestionmodel_set.all()
        dictionaries = [obj.as_dict() for obj in all]

        return JsonResponse({'data': dictionaries})

    def check_answer(request, pk, score):
        question = get_object_or_404(BaseQuestionModel, pk=pk)
        json_data = json.loads(request.body.decode('utf-8'))
        print(json_data)
        if question.check_answer(json_data):
            score = int(score) + 1

        message = 'lala'
        return HttpResponse(str(score))


def cancel(request, type, formtype):
    form = formtype(request.POST)
    return HttpResponseRedirect('/quiz/edit/' + form.data['quiz'])