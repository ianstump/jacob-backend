import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import pdftotext


class DocumentTags(models.Model):
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
        to='tags.PdfDocuments',
        blank=True
    )

    def __str__(self):
        return str(self.name)


class PdfDocuments(models.Model):
    pdf = models.FileField(upload_to='', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="text", null=True)
    html_created = models.BooleanField(verbose_name='html_created', default=False)
    text_created = models.BooleanField(verbose_name='html_created', default=False)

    def __str__(self):
        return str(self.pdf)


@receiver(post_save, sender=PdfDocuments)
def convert_pdf_html(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.html_created:
        convertingPDFtoHTML(instance.pdf)
        instance.html_created = True
        instance.save()
    if not instance.text_created:
        convertingPDFtoText(instance)
        instance.save()


def convertingPDFtoText(instance):
    myfile = instance.pdf
    with open(f'/pdfs/{myfile}', "rb") as f:
        pdf = pdftotext.PDF(f)
        complete_pdf = ("\n\n".join(pdf))
        # uncommented for formatting
        complete_pdf_no_ext_spaces = ' '.join(complete_pdf.split())
        instance.text = complete_pdf
        instance.text_created = True
        instance.save()


def convertingPDFtoHTML(myfile):
    os.system(f'pdf2htmlEX --zoom 1.3 /pdfs/{myfile} --dest-dir /htmls/')


class HighlightedText(models.Model):
    selected_text = models.CharField(
        verbose_name='selected_text',
        max_length=1000,
    )
    document_tags = models.ForeignKey(
        verbose_name='document_tags',
        related_name='highlighted_text',
        to='tags.DocumentTags',
        on_delete=models.CASCADE,

    )
    pdf_documents = models.ForeignKey(
        verbose_name='pdf_documents',
        related_name='highlighted_text',
        to='tags.PdfDocuments',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.selected_text)
