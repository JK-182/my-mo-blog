# Generated by Django 3.0.7 on 2020-12-04 14:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymoblog', '0004_auto_20201130_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='information',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
