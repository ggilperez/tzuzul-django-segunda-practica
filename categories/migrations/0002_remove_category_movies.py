# Generated by Django 3.2.9 on 2021-12-05 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='movies',
        ),
    ]