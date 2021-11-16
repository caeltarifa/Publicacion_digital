from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from .models import UserSession
from django.contrib.sessions.models import Session

from .forms import UserRegisterForm


def register(request):
    form = UserRegisterForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        messages.success(
            request, "Cuenta creada exitosamente! Ahora continua iniciando sesion."
        )
        return HttpResponseRedirect("/users/login/")

    if form.errors:
        errors = form.errors

    template_name = "users/register.html"
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    # remove other sessions
    Session.objects.filter(usersession__user=user).delete()

    # save current session
    request.session.save()

    # create a link from the user to the current session (for later removal)
    UserSession.objects.get_or_create(
        user=user, session=Session.objects.get(pk=request.session.session_key)
    )