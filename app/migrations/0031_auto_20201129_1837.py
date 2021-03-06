# Generated by Django 3.1.3 on 2020-11-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_profile_partner_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number_verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
