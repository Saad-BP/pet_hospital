# Generated by Django 2.2.7 on 2019-11-20 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hospital.models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to=hospital.models.photos_path)),
                ('is_available', models.BooleanField(default=True)),
                ('url', models.CharField(max_length=5000)),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='order',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='attended',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='payment_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
    ]