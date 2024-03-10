# Generated by Django 4.1.7 on 2023-04-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spdapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
    ]
