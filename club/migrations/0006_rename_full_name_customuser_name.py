# Generated by Django 4.1.2 on 2023-10-01 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='full_name',
            new_name='name',
        ),
    ]
