# Generated by Django 4.1.7 on 2023-03-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_experience_experienceitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
