# Generated by Django 2.1.3 on 2019-01-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_auto_20190112_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generationgroup',
            name='generation_text',
            field=models.CharField(max_length=50, unique=True, verbose_name='generation_text'),
        ),
    ]