# Generated by Django 2.0.2 on 2018-02-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20180131_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
