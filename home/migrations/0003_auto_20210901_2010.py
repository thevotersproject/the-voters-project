# Generated by Django 3.2.6 on 2021-09-01 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210829_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admintable',
            name='admin',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='AdminTable',
        ),
    ]
