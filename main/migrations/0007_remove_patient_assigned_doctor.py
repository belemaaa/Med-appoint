# Generated by Django 4.2 on 2023-04-28 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_appointment_access_id_appointment_appointment_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='assigned_doctor',
        ),
    ]