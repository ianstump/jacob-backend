from django.db import models


class Document_tags(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=200,
    )
    datapoint = models.CharField(
        verbose_name='datapoint',
        max_length=200,
    )
    field_type = models.CharField(
        verbose_name='field_type',
        max_length=200,
    )
    domain_value = models.CharField(
        verbose_name='domain_value',
        max_length=200,
    )
    description_gbr = models.TextField(
        verbose_name='description_gbr',

    )
    description_FR = models.TextField(
        verbose_name='description_fr',

    )
    pdf_documents = models.ManyToManyField(
        verbose_name='pdf_documents',
        related_name='document_tags',
        to='tags.Pdf_documents',
    )


class Pdf_documents(models.Model):
    report = models.FileField(upload_to='reports')


class Highlighted_text(models.Model):
    selected_text = models.CharField(
        verbose_name='file_name',
        max_length=1000,
    )
    document_tags = models.ForeignKey(
        verbose_name='document_tags',
        related_name='highlighted_text',
        to='tags.Document_tags',
        on_delete=models.CASCADE,

    )
    pdf_documents = models.ForeignKey(
        verbose_name='pdf_documents',
        related_name='highlighted_text',
        to='tags.Pdf_documents',
        on_delete=models.CASCADE
    )
