# Generated by Django 3.2.6 on 2021-08-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cumulus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='password_hash',
            new_name='password',
        ),
    ]