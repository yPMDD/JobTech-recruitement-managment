# Generated by Django 5.2 on 2025-05-28 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobTech', '0010_alter_interview_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JobTech.job'),
        ),
    ]
