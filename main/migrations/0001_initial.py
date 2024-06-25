# Generated by Django 5.0.5 on 2024-05-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('image_data1', models.ImageField(upload_to='home')),
                ('image_data2', models.ImageField(upload_to='home')),
                ('image_data3', models.ImageField(upload_to='home')),
                ('image_data4', models.ImageField(upload_to='home')),
                ('image_data5', models.ImageField(upload_to='home')),
            ],
        ),
    ]