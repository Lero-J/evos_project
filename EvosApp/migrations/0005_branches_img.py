# Generated by Django 4.2.14 on 2024-09-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvosApp', '0004_meal_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='branches/'),
        ),
    ]