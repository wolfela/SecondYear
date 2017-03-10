from django.views.generic import TemplateView
from django.template import RequestContext

from coolbeans.app.forms import MCQForm
from django.shortcuts import render



class MCQCreateView(TemplateView):
    """
    A view for creating Multiple Choice Questions
    """
    template_name = "app/question/MCQ-Creation-update.html"


    def preview(request):
        """
        Method for previewing the question
        :return:
        """
        if request.method == 'POST':
            form = MCQForm(request.POST)
            if form.is_valid():
                return render(request, 'app/question/MCQ-Display.html', {'form': form})
        else:
            form = MCQForm()

        return render(request, 'app/question/MCQ-Display.html', {'form': form})

    def save(request):
        """
        Method for saving the quuestion, right now its a preview as well, to be fixed
        :return:
        """
        if request.method == 'POST':
            form = MCQForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                return render(request, 'app/question/MCQ-Display.html', {'form': form})
        else:
            form = MCQForm()

        return render(request, '/mcq2', {'form': form},context_instance=RequestContext(request))

