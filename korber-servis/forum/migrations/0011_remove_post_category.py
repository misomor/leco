# Generated by Django 5.0.2 on 2024-03-07 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_alter_document_pdffile_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
