from django.views.generic import TemplateView
from django.template import RequestContext

from coolbeans.app.forms import MCForm, WMForm, WSForm, GFForm
from coolbeans.app.models.question import MultipleChoiceModel, WordScrambleQuestionModel, WordMatchingQuestionModel, GapFillQuestionModel
from django.shortcuts import render, get_object_or_404, redirect


class MCCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/MC-Creation.html"

    def submitMC(request):
        return submit(request, 'MC', MCForm)


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
            question = form.save()
            return redirect(type.lower())
        else:
            form = formtype()

    return render(request, pathType, {'form': form}, context_instance=RequestContext(request))


