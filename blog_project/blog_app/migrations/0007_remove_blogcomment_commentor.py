# Generated by Django 4.2.7 on 2023-12-05 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_blogcomment_commentor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='commentor',
        ),
    ]
