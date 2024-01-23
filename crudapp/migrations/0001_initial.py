# Generated by Django 5.0 on 2023-12-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=250)),
            ],
        ),
    ]
