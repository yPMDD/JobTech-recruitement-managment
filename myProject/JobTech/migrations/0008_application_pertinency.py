# Generated by Django 5.2 on 2025-05-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobTech', '0007_job_skills_alter_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='pertinency',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True, verbose_name='Pertinency Score'),
        ),
    ]
