# Generated by Django 4.2.7 on 2023-12-05 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='altura',
            field=models.IntegerField(default=0.0),
        ),
    ]
