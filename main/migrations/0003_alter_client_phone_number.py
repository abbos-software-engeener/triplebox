# Generated by Django 5.0.5 on 2024-05-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_house_image_data1_alter_house_image_data2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
