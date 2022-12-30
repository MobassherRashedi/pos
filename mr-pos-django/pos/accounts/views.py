from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

def redirect_after_login(request):
    nxt = request.GET.get("next", None)
    if nxt is None:
        return redirect(settings.LOGIN_REDIRECT_URL)
    elif not url_has_allowed_host_and_scheme(
            url=nxt,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return redirect(nxt)


class LoginView(LoginView):
    template_name = "accounts/sign-in/index.html"
    
    def get_success_url(self):
        return reverse_lazy('dashboard.home')


    