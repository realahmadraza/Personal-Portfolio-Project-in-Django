# Generated by Django 5.1 on 2024-08-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='project_images/'),
        ),
    ]
