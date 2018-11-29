from rest_framework import serializers

from project.base.apps.tags.models import HighlightedText


class HighlightedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighlightedText
        fields = ['selected_text', 'document_tags', 'pdf_documents']
