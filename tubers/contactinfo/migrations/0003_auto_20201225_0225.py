# Generated by Django 3.1.4 on 2020-12-24 20:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactinfo', '0002_auto_20201225_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='description',
            new_name='description_1',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='description_2',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]