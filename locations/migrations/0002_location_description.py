# Generated by Django 2.2.7 on 2019-11-19 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(default='Check out the AR content!', max_length=500),
        ),
    ]