# Generated by Django 5.1.6 on 2025-02-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('summary', models.TextField()),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.TextField()),
            ],
        ),
    ]
