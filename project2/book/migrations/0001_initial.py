# Generated by Django 4.0.5 on 2022-06-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('available_count', models.IntegerField()),
                ('rent_per_day', models.IntegerField()),
            ],
        ),
    ]
