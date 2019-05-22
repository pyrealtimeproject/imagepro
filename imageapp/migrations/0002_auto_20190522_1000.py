# Generated by Django 2.2.1 on 2019-05-22 10:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='Address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='DateofJoining',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Department',
            field=models.IntegerField(blank=True, choices=[(1, 'UI'), (2, 'AWS'), (3, 'Newtworking'), (4, 'Human Resource'), (5, 'Software Developer')], null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='Name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+919999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]