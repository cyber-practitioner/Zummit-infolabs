# Generated by Django 3.2.6 on 2021-08-30 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_consumer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumer',
            old_name='name',
            new_name='names',
        ),
    ]