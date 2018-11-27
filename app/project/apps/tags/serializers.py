from rest_framework import serializers

from project.base.apps.tags.models import Document_tags


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_tags
        fields = ['name', 'pdf_documents']
