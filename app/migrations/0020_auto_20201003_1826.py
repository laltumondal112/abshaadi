# Generated by Django 2.2.4 on 2020-10-03 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20200926_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_details', models.CharField(db_index=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=True)),
            ],
            options={
                'verbose_name_plural': 'Jobs Filters',
            },
        ),
        migrations.CreateModel(
            name='MyFilters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_name', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=True)),
                ('l_attr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Looking_For_Attr')),
                ('l_caste', models.ManyToManyField(to='app.Caste')),
                ('l_cities', models.ManyToManyField(to='app.Countries_Cities')),
                ('l_countries', models.ManyToManyField(to='app.Countries')),
                ('l_jobs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Jobs')),
            ],
            options={
                'verbose_name_plural': 'Filters Table',
            },
        ),
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(db_index=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=True)),
            ],
            options={
                'verbose_name_plural': 'Qualifications Filters',
            },
        ),
        migrations.RemoveField(
            model_name='looking_for_countries',
            name='country',
        ),
        migrations.RemoveField(
            model_name='looking_for_countries',
            name='user',
        ),
        migrations.RemoveField(
            model_name='looking_for_jobs',
            name='user',
        ),
        migrations.RemoveField(
            model_name='looking_for_religions',
            name='caste_creed',
        ),
        migrations.RemoveField(
            model_name='looking_for_religions',
            name='religion',
        ),
        migrations.RemoveField(
            model_name='looking_for_religions',
            name='user',
        ),
        migrations.RemoveField(
            model_name='looking_for_states',
            name='c_states',
        ),
        migrations.RemoveField(
            model_name='looking_for_states',
            name='user',
        ),
        migrations.DeleteModel(
            name='Looking_For_Cities',
        ),
        migrations.DeleteModel(
            name='Looking_For_Countries',
        ),
        migrations.DeleteModel(
            name='Looking_For_Jobs',
        ),
        migrations.DeleteModel(
            name='Looking_For_Religions',
        ),
        migrations.DeleteModel(
            name='Looking_For_States',
        ),
        migrations.AddField(
            model_name='myfilters',
            name='l_qualifications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Qualifications'),
        ),
        migrations.AddField(
            model_name='myfilters',
            name='l_religions',
            field=models.ManyToManyField(to='app.Religion'),
        ),
        migrations.AddField(
            model_name='myfilters',
            name='l_states',
            field=models.ManyToManyField(to='app.Countries_States'),
        ),
        migrations.AddField(
            model_name='myfilters',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
