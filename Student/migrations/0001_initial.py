# Generated by Django 2.2.5 on 2019-09-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=20)),
                ('session', models.CharField(max_length=50)),
            ],
        ),
    ]