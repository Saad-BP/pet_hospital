# Generated by Django 2.2.7 on 2019-11-19 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hospital.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('grooming', 'Grooming'), ('dentistry', 'Dentistry'), ('boarding', 'Boarding'), ('other', 'Other')], max_length=50)),
                ('appointment_date', models.DateField()),
                ('details', models.TextField()),
                ('phone', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('attended', models.BooleanField()),
                ('payment_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('short_description', models.CharField(max_length=2000)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to=hospital.models.blog_photos_path, verbose_name='image*')),
                ('date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=hospital.models.team_photos_path)),
                ('designation', models.CharField(choices=[('doctor', 'Doctor'), ('staff', 'Stuff'), ('assistant', 'Assistant')], max_length=50)),
                ('details', models.TextField()),
                ('phone', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.TextField()),
                ('treatment', models.TextField()),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(null=True, upload_to=hospital.models.photos_path, verbose_name='Photo*')),
                ('employee_type', models.CharField(choices=[('doctor', 'Doctor'), ('director', 'Director'), ('receptionist', 'Receptionist'), ('inventory_manager', 'Inventory Manager'), ('accountant', 'Accountant'), ('typist', 'Typist')], max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='assigned_doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='pets.Pet'),
        ),
    ]
