# Generated by Django 2.2 on 2020-05-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('nif', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('alt_phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
