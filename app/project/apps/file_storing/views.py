# !/usr/bin/env python
import time

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework.views import APIView
import os
import pdftotext
from project.base.apps.tags.models import Pdf_documents


class FileView(APIView):
    permission_classes = []

    """the view is made for the upload"""

    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        print("name of file", myfile)
        fs = FileSystemStorage()
        self.convertingPDFtoText(myfile)
        return HttpResponse("Working upload")

    """ the next function converts the pdf directly to text and saves it into the Pdf_documents model
     with a relation to report """

    def convertingPDFtoText(self, myfile):
        while not os.path.exists(f'/pdfs/{myfile}'):
            time.sleep(1)
        if os.path.isfile(f'/pdfs/{myfile}'):
            with open(f'/pdfs/{myfile}', "rb") as f:
                pdf = pdftotext.PDF(f)
                complete_pdf = ("\n\n".join(pdf))
                instance = Pdf_documents(report=myfile, text_document=complete_pdf)
                instance.save()
