# Generated by Django 5.2 on 2025-05-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_candidate_cover_letter_alter_candidate_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='skills',
            field=models.CharField(blank=True, help_text='Comma-separated list of skills', max_length=255, null=True, verbose_name='Skills'),
        ),
    ]
