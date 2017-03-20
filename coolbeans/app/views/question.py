import json
from django.views.generic import TemplateView
from django.template import RequestContext

from coolbeans.app.forms import MCForm, WMForm, WSForm, GFForm
from coolbeans.app.models.question import MultipleChoiceModel, WordScrambleQuestionModel, WordMatchingQuestionModel, GapFillQuestionModel, CrosswordQuestionModel, BaseQuestionModel
from coolbeans.app.models.quiz import QuizModel
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers


# FOR PRINTING SAVED OBJECTS:
# data = serializers.serialize("json", CrosswordQuestionModel.objects.all(), indent=4)
# print(data)


class MCCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/MC-Creation.html"

    def submitMC(request):
        return MCCreateView.submit(request, 'MC', MCForm)

    def submit(request, type, formtype):
        if 'save_form' in request.POST:
            return MCCreateView.save(request, type, formtype)
        elif 'preview_form' in request.POST:
            return MCCreateView.preview(request, type, formtype)
        elif 'cancel_form' in request.POST:
            return cancel(request, type, formtype)

    def preview(request, type, formtype):
        pathDisplay = 'app/question/' + type + '-Preview.html'
        """
        Method for previewing the question
        :return:
        """
        if request.method == 'POST':
            form = formtype(request.POST)
            if form.is_valid():
                answers = request.POST.getlist('answers[]')
                correct = request.POST.get('correct')
                form.cleaned_data['answers'] = ','.join(answers)
                formcopy = formtype(request.POST.copy())
                answers.append(correct)
                formcopy.data['answers'] = ','.join(answers)
                return render(request, pathDisplay, {'form': formcopy})
        else:
            form = formtype()

        return render(request, pathDisplay, {'form': form})


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
                correct = request.POST.get('correct')
                form.cleaned_data['answers'] = ','.join(answers)
                formcopy = formtype(request.POST.copy())
                answers.append(correct)
                formcopy.data['answers'] = ','.join(answers)
                formcopy.save()
                return redirect(type.lower())
            else:
                form = formtype()

        return render(request, pathType, {'form': form}, context_instance=RequestContext(request))

class MCQuestionView(TemplateView):
    template_name = "app/question/MC-Display.html"

    def show_question(request, pk):
        question = get_object_or_404(MultipleChoiceModel, pk=pk)
        return render(request, 'app/question/MC-Display.html', {'question': question})


class WMCreateView(TemplateView):
    """
    A view for creating Word Match Questions
    """
    template_name = "app/question/WM-Creation.html"


    def submitWM(request):
        return submit(request, 'WM', WMForm)


class WMQuestionView(TemplateView):
    template_name = "app/question/WM-Display.html"

    def show_question(request, pk):
        question = get_object_or_404(WordMatchingQuestionModel, pk=pk)
        return render(request, 'app/question/WM-Display.html', {'question': question})


class WSCreateView(TemplateView):
    """
    A view for creating Word Scramble Questions
    """
    template_name = "app/question/WS-Creation.html"


    def submitWS(request):
        return submit(request, 'WS', WSForm)



class WSQuestionView(TemplateView):
    template_name = "app/question/WS-Display.html"

    def show_question(request, pk):
        question = get_object_or_404(WordScrambleQuestionModel, pk=pk)
        return render(request, 'app/question/WS-Display.html', {'question': question})


class GFCreateView(TemplateView):
    """
    A view for creating Word Scramble Questions
    """
    template_name = "app/question/GF-Creation.html"

    def submitGF(request):
        return submit(request, 'GF', GFForm)


class GFQuestionView(TemplateView):
    template_name = "app/question/GF-Display.html"

    def show_question(request, pk):
        question = get_object_or_404(GapFillQuestionModel, pk=pk)
        return render(request, 'app/question/GF-Display.html', {'question': question})




class CWPreviewView(TemplateView):
    template_name = "app/question/CW-Preview.html"


class CWCreateView(TemplateView):
    """
    A view for creating Word Scramble Questions
    """
    template_name = "app/question/CW-Creation.html"

    def submit(request):
        json_data = json.loads(request.body.decode('utf-8'))
        q = QuizModel.objects.create()
        base = BaseQuestionModel.objects.create(quiz=q)
        for element in json_data['data']:
            CrosswordQuestionModel.objects.create(question=base, direction=element['direction'], length=element['length'],
                                                 x=element['x'],y=element['y'],clue=element['clue'],
                                                 answer=element['word'])

        print(base.id)
        message = "yes"
        return HttpResponse(message)


class CWQuestionView(TemplateView):
    template_name = "app/question/CW-Display.html"

    def show_question(request, pk):

        question = get_object_or_404(BaseQuestionModel, pk=pk)
        all = question.crosswordquestionmodel_set.all()
        dictionaries = [obj.as_dict() for obj in all]

        return JsonResponse({'data': dictionaries})

def submit(request, type, formtype):
    if 'save_form' in request.POST:
        return save(request, type, formtype)
    elif 'preview_form' in request.POST:
        return preview(request, type, formtype)
    elif 'cancel_form' in request.POST:
        return cancel(request, type, formtype)

def cancel(request, type, formtype):
    return redirect(type.lower())

def preview(request, type, formtype):
    pathDisplay = 'app/question/' + type + '-Preview.html'
    """
    Method for previewing the question
    :return:
    """
    if request.method == 'POST':
        form = formtype(request.POST)
        if form.is_valid():
            return render(request, pathDisplay, {'form': form})
    else:
        form = formtype()

    return render(request, pathDisplay, {'form': form})


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
            form.save()
            return redirect(type.lower())
        else:
            form = formtype()

    return render(request, pathType, {'form': form}, context_instance=RequestContext(request))

