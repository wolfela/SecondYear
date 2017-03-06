from django.views import View
from django.views.generic import TemplateView
from coolbeans.app.models.question import TestModel, TestModelll, BaseQuestionModel, MultipleChoiceModel
from coolbeans.app.models.base import TimeStampedModel
from coolbeans.app.models.user import UserModel
from coolbeans.app.models.quiz import QuizModel
from django.http import JsonResponse
from django.utils import timezone


class MCQView(TemplateView):
    """
    A view for listing the quizzes this user can access.
    """
    template_name = "app/question/MCQ-Display.html"


class MCQCreateView(TemplateView):
    """
    A view for listing the quizzes this user can access.
    """
    template_name = "app/question/MCQ-Creation-update.html"

""" def store(request):
        if request.is_ajax():
            if request.method == 'GET':
                q = MCQQuestionModel.objects.get(correct=request.GET.get('a1'))
                q.answers = request.GET.get('a2')
                q.save()
                return HttpResponse("%s" % q.correct) """
"""  def savethis(request):
        if request.POST['a1'] and request.POST['a2']:
            name = request.GET['a1']
            desc = request.GET['a2']
            test = TestModel(name=name, description=desc)
            test.save
            return HttpResponse('Ok')
        else:
            return HttpResponse('Fail')
        """
def validate(request):
   a1 = request.GET.get('a1')
   list = request.GET.get('list')
   t = request.GET.get('title')
   q = QuizModel.objects.create()
   m = BaseQuestionModel(quiz=q)
   #m = TestModelll.objects.create(quiz=q,name=1)
   m = MultipleChoiceModel.objects.create(quiz=q, title=t,answers=list,correct=a1)
   #test.save()
   data = {
        'is_taken': 'okay'
    }
   return JsonResponse(data)

# def validatee(request):
#        a1 = request.GET.get('a1')
#
#
#        test = TestModel.objects.filter(name__iexact=a1).exists()
#        data = {
#            'is_taken': test
#        }
#        return JsonResponse(data)

       #TestModel.objects.filter(name__iexact=a1).exists()
   # data={
   #      'returnVal':'nice'
   #  }
   # return JsonResponse(data)