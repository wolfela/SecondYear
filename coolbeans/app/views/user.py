from django.views import View
from django.views.generic import TemplateView


class LoginView(TemplateView):
    """
    The login view.
    """
    template_name = "app/user/login.html"

    def post(self):
        """
        Logs the user in.
        :return:
        """
        pass


class LogoutView(View):
    """
    The logout view.
    """

    def get(self):
        """
        Logs the current user out.

        :return:
        """
        pass


class RegisterView(TemplateView):
    """
    The registration view.
    """
    template_name = "app/user/register.html"

    def post(self):
        """
        Registers an user.
        :return:
        """
        pass


class ProfileView(TemplateView):
    """
    A View for a single user.
    """
    template_name = "app/user/profile.html"

    def get(self, request, **kwargs):
        """
        Gets a profile.

        :param request:
        :return:
        """
        pass


class SelfProfileView(ProfileView):
    """
    A view for the current user.
    """

    def get(self, request, **kwargs):
        """
        Gets the profile of the current user.
        :param request:
        :return:
        """
        pass


class EditProfileView(TemplateView):
    """
    A view for editing the current user.
    """
    template_name = "app/user/profile_edit.html"

    def get(self, request, **kwargs):
        """
        Displays the edit profile form.
        :param request:
        :return:
        """
        pass

    def post(self, request):
        """
        Edits the user.
        :param request:
        :return:
        """
