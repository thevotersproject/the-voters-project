# Generated by Django 3.2.6 on 2021-09-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_adminprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminprofile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='adminprofile',
            name='lastname',
        ),
        migrations.AddField(
            model_name='adminprofile',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
