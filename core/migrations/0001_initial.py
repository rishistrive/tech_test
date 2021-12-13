# Generated by Django 4.0 on 2021-12-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('building_csv', models.FileField(upload_to='building_data/csv')),
                ('resource_csv', models.FileField(upload_to='meter_data/csv')),
                ('resource_usage_csv', models.FileField(upload_to='half_hourly_data/csv')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
