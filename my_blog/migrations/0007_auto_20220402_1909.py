# Generated by Django 3.2.9 on 2022-04-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click above link to read bolg post...', max_length=255),
        ),
    ]
