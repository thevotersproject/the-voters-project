# Generated by Django 3.2.6 on 2021-09-02 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userFirstname', models.CharField(max_length=100)),
                ('userLastname', models.CharField(max_length=100)),
                ('userImg', models.ImageField(upload_to='pics')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidateFirstname', models.CharField(max_length=100)),
                ('candidateLastname', models.CharField(max_length=100)),
                ('candidateDetails', models.CharField(max_length=100)),
                ('candidateImg', models.ImageField(upload_to='pics')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]