# Generated by Django 3.2.10 on 2022-02-18 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('identification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Central_Bank_Email_Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('individual', models.CharField(default='', max_length=30)),
                ('customer_type', models.CharField(default='', max_length=30)),
                ('alert_id', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='FuzzyScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Self_Analysis_Cases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alert_id', models.CharField(max_length=25)),
                ('case_status', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('individual', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.individual')),
            ],
        ),
        migrations.CreateModel(
            name='MLRO_Cases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alert_id', models.CharField(max_length=25)),
                ('case_status', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('customer_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.individual')),
            ],
        ),
        migrations.CreateModel(
            name='L2_Cases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alert_id', models.CharField(max_length=25)),
                ('case_status', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('individual', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.individual')),
            ],
        ),
        migrations.CreateModel(
            name='L1_Cases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alert_id', models.CharField(max_length=25)),
                ('case_status', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('individual', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.individual')),
            ],
        ),
        migrations.CreateModel(
            name='IndividulDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(blank=True, max_length=25, null=True)),
                ('data_Id', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('name_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('alias', models.CharField(blank=True, max_length=1000, null=True)),
                ('alias_quality', models.CharField(blank=True, max_length=50, null=True)),
                ('id_number', models.CharField(blank=True, max_length=100, null=True)),
                ('id_number_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('passportNum', models.CharField(blank=True, max_length=100, null=True)),
                ('passport_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('father_name', models.CharField(blank=True, max_length=500, null=True)),
                ('father_name_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.CharField(blank=True, max_length=500, null=True)),
                ('dob_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('pob', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('address_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('province', models.CharField(blank=True, max_length=1000, null=True)),
                ('province_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=1000, null=True)),
                ('district_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('nationality_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('country_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=300, null=True)),
                ('city_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('discrepant_check', models.CharField(blank=True, max_length=20, null=True)),
                ('list', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=15, null=True)),
                ('score', models.CharField(blank=True, max_length=10, null=True)),
                ('strength', models.CharField(blank=True, max_length=10, null=True)),
                ('match_type', models.CharField(max_length=20)),
                ('proposed_action', models.CharField(blank=True, max_length=500, null=True)),
                ('risk', models.CharField(blank=True, max_length=20, null=True)),
                ('discounting_rationale', models.CharField(max_length=200)),
                ('discounting_factor', models.IntegerField()),
                ('type_discounting_factor', models.CharField(blank=True, max_length=200, null=True)),
                ('action_performed_type', models.CharField(blank=True, max_length=100, null=True)),
                ('discount_status', models.CharField(blank=True, max_length=50, null=True)),
                ('over_all_discount_status', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('sent_to_L1', models.BooleanField(default=False)),
                ('sent_to_L2', models.BooleanField(default=False)),
                ('sent_to_MLRO', models.BooleanField(default=False)),
                ('self_analysis', models.BooleanField(default=False)),
                ('individual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.individual')),
            ],
        ),
        migrations.CreateModel(
            name='EntityDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_registeration', models.CharField(blank=True, max_length=200, null=True)),
                ('data_Id', models.CharField(blank=True, max_length=100, null=True)),
                ('case_id', models.CharField(blank=True, max_length=25, null=True)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('name_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('alias', models.CharField(blank=True, max_length=1000, null=True)),
                ('alias_quality', models.CharField(blank=True, max_length=100, null=True)),
                ('id_number', models.CharField(blank=True, max_length=200, null=True)),
                ('id_number_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('address_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('province', models.CharField(blank=True, max_length=1000, null=True)),
                ('province_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=1000, null=True)),
                ('district_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('nationality_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('country_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('city_match_score', models.CharField(blank=True, max_length=20, null=True)),
                ('list', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('score', models.CharField(blank=True, max_length=10, null=True)),
                ('strength', models.CharField(blank=True, max_length=10, null=True)),
                ('match_type', models.CharField(max_length=20)),
                ('proposed_action', models.CharField(blank=True, max_length=500, null=True)),
                ('risk', models.CharField(blank=True, max_length=20, null=True)),
                ('discounting_rationale', models.CharField(max_length=200)),
                ('discounting_factor', models.IntegerField()),
                ('type_discounting_factor', models.CharField(blank=True, max_length=200, null=True)),
                ('action_performed_type', models.CharField(blank=True, max_length=100, null=True)),
                ('discount_status', models.CharField(blank=True, max_length=50, null=True)),
                ('over_all_discount_status', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('sent_to_L1', models.BooleanField(default=False)),
                ('sent_to_MLRO', models.BooleanField(default=False)),
                ('self_analysis', models.BooleanField(default=False)),
                ('entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.organization')),
            ],
        ),
        migrations.CreateModel(
            name='EntityAlerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.CharField(blank=True, max_length=100, null=True)),
                ('case_id', models.CharField(blank=True, max_length=25, null=True)),
                ('dataID', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('alias', models.CharField(blank=True, max_length=200, null=True)),
                ('alias_quality', models.CharField(blank=True, max_length=200, null=True)),
                ('id_number', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('strength', models.CharField(blank=True, max_length=200, null=True)),
                ('score', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('province', models.CharField(blank=True, max_length=200, null=True)),
                ('distict', models.CharField(blank=True, max_length=200, null=True)),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=400, null=True)),
                ('list', models.CharField(blank=True, max_length=200, null=True)),
                ('entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(blank=True, max_length=25, null=True)),
                ('dataID', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('father_name', models.CharField(blank=True, max_length=200, null=True)),
                ('alias', models.CharField(blank=True, max_length=200, null=True)),
                ('alias_quality', models.CharField(blank=True, max_length=200, null=True)),
                ('id_number', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('strength', models.CharField(blank=True, max_length=200, null=True)),
                ('score', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.CharField(blank=True, max_length=200, null=True)),
                ('pob', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('province', models.CharField(blank=True, max_length=200, null=True)),
                ('distict', models.CharField(blank=True, max_length=200, null=True)),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('list', models.CharField(blank=True, max_length=200, null=True)),
                ('individual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.individual')),
            ],
        ),
    ]
