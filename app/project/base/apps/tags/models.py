import os
import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.name)


class Pdf_documents(models.Model):
    report = models.FileField(upload_to='', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    text_document = models.TextField(
        verbose_name="text_document",
        null=True)

    def __str__(self):
        return str(self.report)


@receiver(post_save, sender=Pdf_documents)
def convert_pdf_html(sender, **kwargs):
    instance = kwargs.get('instance')
    convertingPDFtoHTML(instance.report)


def convertingPDFtoHTML(myfile):
    while not os.path.exists(f'/pdfs/{myfile}'):
        time.sleep(1)
    if os.path.isfile(f'/pdfs/{myfile}'):
        os.system(f'pdf2htmlEX --zoom 1.3 /pdfs/{myfile} --dest-dir /htmls/')


class Highlighted_text(models.Model):
    selected_text = models.CharField(
        verbose_name='selected_text',
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
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.selected_text)
