# Generated by Django 4.2 on 2023-08-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_remove_person_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cPassword',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='', max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='person',
            name='userName',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
