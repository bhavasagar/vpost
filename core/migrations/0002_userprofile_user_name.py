# Generated by Django 2.2.10 on 2021-03-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_name',
            field=models.CharField(default=False, max_length=30),
        ),
    ]
