from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from .models import UserSession
from django.contrib.sessions.models import Session

from django.contrib.auth.models import User

from .forms import UserRegisterForm

from django.contrib.auth.decorators import login_required


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

@login_required()
def display_users(request):
    template_name = "users/display_users.html"

    # querying Document table from db
    queryset1 = User.objects.all().order_by("-username")

    context = {"user_list": queryset1}
    return render(request, template_name, context)



@login_required()
def deactivate_user(request, pk):
    # querying Document table from db to get single row and deleting it
    instance1 = get_object_or_404(User, id=pk)
    instance2 = User.objects.filter(id=pk).update(is_active=False)

    messages.success(request, "successfully User deactivate")
    return redirect("display_users")

@login_required()
def activate_user(request, pk):
    # querying Document table from db to get single row and deleting it
    instance1 = get_object_or_404(User, id=pk)
    instance2 = User.objects.filter(id=pk).update(is_active=True)

    messages.success(request, "successfully User activate")
    return redirect("display_users")
