from django.conf.urls import url

from .views import display_documents, add_documents, user_documents, delete_document, get_document

from documents.views import delete_document_upload

urlpatterns = [
    url(r'^$', display_documents, name='view'),
    url(r'^view_documents/$', user_documents, name='user_doc'),
    url(r'^add/$', add_documents, name='add'),
    url(r'^delete/(?P<pk>\d+)/$', delete_document, name='delete'),
    url(r'^deleteuploaded/(?P<pk>\d+)/$', delete_document_upload, name='delete_upload'),
    url(r'^get-document/(?P<pk>\d+)/$', get_document, name='get_document'),
]