# Generated by Django 4.1.7 on 2023-03-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_project_project_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.URLField(blank=True, null=True),
        ),
    ]