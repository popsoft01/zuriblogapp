# Generated by Django 3.2 on 2021-09-28 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_commentmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentModel',
        ),
    ]
