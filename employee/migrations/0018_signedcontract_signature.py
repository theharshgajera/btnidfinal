# Generated by Django 5.0.2 on 2024-06-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_employeedetail_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='signedcontract',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='signatures/'),
        ),
    ]
