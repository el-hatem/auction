# Generated by Django 3.1.8 on 2021-05-03 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_comments_listing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'Users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_list',
        ),
    ]
