# Generated by Django 2.0.3 on 2018-11-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20181126_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document_tags',
            name='pdf_documents',
            field=models.ManyToManyField(blank=True, null=True, related_name='document_tags', to='tags.Pdf_documents', verbose_name='pdf_documents'),
        ),
    ]