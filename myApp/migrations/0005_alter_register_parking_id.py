# Generated by Django 4.2.6 on 2024-01-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_rename_slots_register_parking_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='parking_id',
            field=models.CharField(max_length=200),
        ),
    ]
