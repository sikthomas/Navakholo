# Generated by Django 5.0.7 on 2024-07-31 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NavakholoBursary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinformation',
            old_name='user',
            new_name='userid',
        ),
    ]
