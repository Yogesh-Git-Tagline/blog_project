# Generated by Django 4.2.7 on 2023-12-05 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_blog_author_blogcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='blogcomment',
            old_name='for_blog',
            new_name='blog',
        ),
    ]
