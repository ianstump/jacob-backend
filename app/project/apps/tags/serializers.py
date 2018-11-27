from rest_framework import serializers

from project.base.apps.tags.models import Document_tags, Highlighted_text


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_tags
        fields = ['id', 'name', 'pdf_documents']


class HighlightedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlighted_text
        fields = ['selected_text']
