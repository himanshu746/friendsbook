# Generated by Django 2.0.2 on 2018-03-17 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.IntegerField()),
                ('user2', models.IntegerField()),
                ('since', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('friendship', models.IntegerField()),
            ],
        ),
    ]
