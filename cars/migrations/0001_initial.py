# Generated by Django 3.1.7 on 2021-03-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default=None, max_length=100, unique=True)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
    ]
