# Generated by Django 5.0.2 on 2024-06-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_employeedetail_blood_group_employeedetail_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='empcode',
            field=models.TextField(null=True),
        ),
    ]
