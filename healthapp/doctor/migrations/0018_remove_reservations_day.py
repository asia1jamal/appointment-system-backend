# Generated by Django 4.1.3 on 2023-01-14 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_alter_reservations_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='Day',
        ),
    ]
