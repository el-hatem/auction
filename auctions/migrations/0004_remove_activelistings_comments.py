# Generated by Django 3.1.8 on 2021-05-03 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210503_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activelistings',
            name='comments',
        ),
    ]