# Generated by Django 4.1.4 on 2022-12-12 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0002_rename_post_comment_forum_comment_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
    ]
