# Generated by Django 4.2.5 on 2023-10-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='suggestions',
            name='year_released',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
