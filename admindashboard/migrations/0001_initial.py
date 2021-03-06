# Generated by Django 3.2.10 on 2022-02-18 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='extendedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('bank_code', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('employee_code', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('designation', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('employee_status', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('contact_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('user_role', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('action_required', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('hod_name', models.CharField(default='', max_length=50)),
                ('hod_designation', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('hod_cell_phone', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('hod_email', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
