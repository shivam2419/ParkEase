# Generated by Django 4.2.6 on 2024-01-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_signup_rename_date_register_slot_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
