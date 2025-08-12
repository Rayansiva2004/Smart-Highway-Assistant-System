from django.shortcuts import render,get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import Document

def documentWallet(request):
    if request.method == "POST":
        title = request.POST.get("title")
        file = request.FILES.get("document")  # Retrieve the uploaded file
        user_id = request.session.get('user_id',None)

        if title and file:
            # Save the uploaded file to a directory
            

            # Save to the database
            document = Document(title=title, document=file, user_id=user_id)
            document.save()

    # Retrieve all documents from the database
    documents = Document.objects.filter(user_id = request.session.get('user_id',None))

    return render(request, 'DocumentWallet/documentwallet.html', {"documents": documents})


def open_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    return render(request, 'DocumentWallet/document_view.html', {'doc': doc})