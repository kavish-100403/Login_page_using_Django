# Generated by Django 4.2.3 on 2023-08-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
