# Generated by Django 2.2.4 on 2020-09-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200919_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uid',
            field=models.CharField(blank=True, db_index=True, max_length=20, null=True),
        ),
    ]