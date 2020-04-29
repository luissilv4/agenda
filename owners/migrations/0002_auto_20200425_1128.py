# Generated by Django 2.2 on 2020-04-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='contact',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='owner',
            name='alt_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
