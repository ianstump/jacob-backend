from django.http import HttpResponse
from rest_framework.views import APIView
# from django.core.files.storage import FileSystemStorage
from project.base.apps.tags.models import Pdf_documents


class FileView(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # file_name = f'/media-files/{filename}'
        instance = Pdf_documents(report=myfile)
        instance.save()
        # print("filename", file_name)s
        return HttpResponse("Working upload")
