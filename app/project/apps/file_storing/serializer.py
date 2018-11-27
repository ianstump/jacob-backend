from rest_framework import serializers

from project.base.apps.tags.models import Pdf_documents


class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = Pdf_documents
        fields = ('report', 'timestamp', 'text_document')
