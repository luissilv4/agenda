# Generated by Django 2.2 on 2020-05-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='office',
            field=models.ManyToManyField(to='services.Office'),
        ),
    ]
