# Generated by Django 5.0.1 on 2024-05-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstN', models.CharField(max_length=20)),
                ('lastN', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('userN', models.CharField(max_length=5)),
                ('password', models.CharField(max_length=14)),
            ],
        ),
    ]
