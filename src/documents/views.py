from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from document_viewer.settings import CDN_DOMAIN

from .models import Document, DocumentUpload
from .forms import AddDocument

from django.http import JsonResponse
import itertools

# comentarios
#   parte 1
#       trabajando 1
#       trabajando 2
#       trabajando 3
#       trabajando 4--- te amo amor

#   parte 2
# comentario1
# comentario2
# comentario3
# TE AMO CAELITO


@login_required()
def add_documents(request):
    form = AddDocument(request.POST or None, request.FILES or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated and not request.user.groups.filter(
            name="G_SUSCRIPTORES_AIP"
        ):

            # saving the details in the db
            obj = Document.objects.create(
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                uploaded_by=request.user,
            )

            # uploading the first document with same id
            query = Document.objects.latest("id")
            obj = DocumentUpload.objects.create(
                document_id=query.id,
                name=form.cleaned_data.get("title"),
                document_url=form.cleaned_data.get("document"),
            )

            # looping through all other documents and uploading with same id
            for i in range(2, 11):
                extra = "document" + str(i)
                if str(form.cleaned_data.get(extra)) != "None":
                    obj = DocumentUpload.objects.create(
                        document_id=query.id,
                        name=form.cleaned_data.get("title"),
                        document_url=form.cleaned_data.get(extra),
                    )
            return redirect("documents:view")

    if form.errors:
        errors = form.errors
    template_name = "documents/add_documents.html"
    context = {"form": form, "errors": errors}
    if request.user.is_authenticated and request.user.groups.filter(
        name="G_SUSCRIPTORES_AIP"
    ):
        return redirect("/")
    return render(request, template_name, context)


from django.views.decorators.clickjacking import xframe_options_exempt


@login_required()
@xframe_options_exempt
def display_documents(request):
    template_name = "documents/display_documents.html"

    # querying Document table from db
    queryset1 = Document.objects.all().order_by("-pk")

    # querying DocumentUpload table from db
    queryset2 = DocumentUpload.objects.all()

    # domain of CDN where the documents will be uploaded
    cdn = CDN_DOMAIN

    context = {"object_list": queryset1, "document_list": queryset2, "cdn": cdn}
    return render(request, template_name, context)


@login_required()
def user_documents(request):
    template_name = "documents/user_documents.html"

    # querying Document table from db
    queryset1 = Document.objects.filter(uploaded_by=request.user).order_by("-pk")

    # querying DocumentUpload table from db
    queryset2 = DocumentUpload.objects.all()

    # domain of CDN where the documents will be uploaded
    cdn = CDN_DOMAIN

    context = {"object_list": queryset1, "document_list": queryset2, "cdn": cdn}
    return render(request, template_name, context)


@login_required()
def delete_document(request, pk):
    # querying Document table from db to get single row and deleting it
    instance1 = get_object_or_404(Document, pk=pk).delete()
    instance2 = DocumentUpload.objects.filter(document_id=pk).delete()

    messages.success(request, "successfully deleted the document")
    return redirect("documents:user_doc")


@login_required()
def get_document(request, pk):
    # querying Document table from db to get single row and deleting it
    instance1 = get_object_or_404(DocumentUpload, id=pk)
    instance2 = DocumentUpload.objects.get(id=pk)
    instance2 = serializar_DocumentUpload(instance2)

    messages.success(request, "successfully get document")
    return JsonResponse(
        data={"document": instance2}, safe=False, json_dumps_params={"indent": 1}
    )
    # return redirect("documents:user_doc")


def serializar_DocumentUpload(document):
    return {
        "document_id": document.document_id,
        "name": document.name,
        "document_url": "media/" + str(document.document_url),
    }