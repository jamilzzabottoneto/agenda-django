# Generated by Django 5.2 on 2025-04-02 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contac_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contac',
            new_name='Contact',
        ),
    ]
