# Generated by Django 3.1.7 on 2021-03-28 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20210328_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratesnumber',
            old_name='car',
            new_name='car_id',
        ),
    ]
