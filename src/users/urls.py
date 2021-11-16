from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import activate_user, deactivate_user, display_users 
from users.views import register 


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    url(r'^users/$', display_users, name='display_users'),
    url(r'^deactivate/(?P<pk>\d+)/$', deactivate_user, name='deactivate_user'),
    url(r'^activate/(?P<pk>\d+)/$', activate_user, name='activate_user'),


]