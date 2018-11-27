from rest_framework import serializers

from project.base.apps.tags.models import DocumentTags, HighlightedText


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTags
        fields = ['id', 'name', 'pdf_documents']


class HighlightedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighlightedText
        fields = ['selected_text']
