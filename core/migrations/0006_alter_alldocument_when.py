# Generated by Django 4.0.1 on 2022-01-21 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alldocument_documentnames_delete_alldocuments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldocument',
            name='when',
            field=models.TextField(blank=True, null=True),
        ),
    ]