# Generated by Django 4.2 on 2024-12-09 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='data',
            new_name='date',
        ),
    ]
