# Generated by Django 4.1.3 on 2023-01-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_alter_doctors_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='DateOfBirth',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
