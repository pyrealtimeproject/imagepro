# Generated by Django 2.2.1 on 2019-05-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_auto_20190522_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
