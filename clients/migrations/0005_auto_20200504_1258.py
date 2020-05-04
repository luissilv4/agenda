# Generated by Django 2.2 on 2020-05-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20200501_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='RGPD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sms_reminders', models.BooleanField(default=False)),
                ('email_reminders', models.BooleanField(default=False)),
                ('new_appointment_notification', models.BooleanField(default=False)),
                ('marketing', models.BooleanField(default=False)),
                ('satisfaction_forms', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='rgpd',
        ),
    ]
