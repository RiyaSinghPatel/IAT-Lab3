# Generated by Django 5.0.6 on 2024-05-30 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='borroed_books',
            new_name='borrowed_books',
        ),
    ]
