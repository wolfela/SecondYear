from django.views.generic import TemplateView
from django.template import RequestContext

from coolbeans.app.forms import MCQForm
from coolbeans.app.forms import DNDForm
from django.shortcuts import render


class MCQCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/MCQ-Creation-update.html"

    def previewMCQ(request):
        preview(request, 'MCQ', MCQForm)

    def saveMCQ(request):
        save(request, 'MCQ', MCQForm)


class DNDCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/DND-Creation.html"


    def previewDND(request):
        preview(request, 'DND', DNDForm)


    def saveDND(request):
        save(request, 'DND', DNDForm)


def preview(request, type, formtype):
    pathDisplay = 'app/question/' + type + '-Display.html'
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
    pathCreation = 'app/question' + type + '-Creation.html'
    pathType = '/' + type
    """
    Method for saving the question, right now its a preview as well, to be fixed
    :return:
    """
    if request.method == 'POST':
        form = formtype(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return render(request, pathCreation, {'form': form})
        else:
            form = DNDForm()

        return render(request, pathType, {'form': form},context_instance=RequestContext(request))


