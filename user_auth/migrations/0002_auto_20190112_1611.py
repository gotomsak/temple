# Generated by Django 2.1.3 on 2019-01-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generationgroup',
            name='generation_text',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='landgroup',
            name='land_text',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='regiongroup',
            name='region_text',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]