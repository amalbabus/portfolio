# Generated by Django 2.2.13 on 2020-07-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200718_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='email',
            field=models.EmailField(default='none', max_length=254),
        ),
    ]
