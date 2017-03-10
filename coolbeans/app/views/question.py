from django.views.generic import TemplateView
from django.template import RequestContext

from coolbeans.app.forms import MCQForm
from coolbeans.app.forms import DNDForm
from coolbeans.app.models.question import MultipleChoiceModel
from django.shortcuts import render, get_object_or_404, redirect


class MCQCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/MCQ-Creation.html"

    def previewMCQ(request):
        return preview(request, 'MCQ', MCQForm)

    def saveMCQ(request):
        return save(request, 'MCQ', MCQForm)


class MCQQuestionView(TemplateView):
    template_name = "app/question/MCQ-Display.html"

    def show_question(request, pk):
        question = get_object_or_404(MultipleChoiceModel, pk=pk)
        return render(request, 'app/question/MCQ-Display.html', {'question': question})


class DNDCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/DND-Creation.html"


    def previewDND(request):
        return preview(request, 'DND', DNDForm)


    def saveDND(request):
        return save(request, 'DND', DNDForm)


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
    pathShowSaved = type + 'question'
    """
    Method for saving the question, right now its a preview as well, to be fixed
    :return:
    """
    if request.method == 'POST':
        form = formtype(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect(pathShowSaved, pk=question.pk)
        else:
            form = DNDForm()

    return render(request, pathType, {'form': form}, context_instance=RequestContext(request))


