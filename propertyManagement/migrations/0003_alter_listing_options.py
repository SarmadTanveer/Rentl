# Generated by Django 4.0.3 on 2022-04-07 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propertyManagement', '0002_listing_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'permissions': (('can_edit', 'can_delete'),)},
        ),
    ]