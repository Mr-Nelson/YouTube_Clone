# Generated by Django 3.1.8 on 2021-07-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0004_comment_subcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subComment',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
