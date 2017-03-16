from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    The Index view.
    """

    template_name = "app/index.html"

