# Generated by Django 3.1.3 on 2020-12-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeID', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=200)),
                ('response', models.CharField(max_length=200)),
            ],
        ),
    ]
