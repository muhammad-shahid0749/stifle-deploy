# Generated by Django 3.2.10 on 2022-02-18 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTypeIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficial',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('benefical_owner_name', models.CharField(max_length=50)),
                ('relationship_with_customer', models.CharField(max_length=50)),
                ('beneficial_address', models.CharField(max_length=200)),
                ('beneficial_id', models.CharField(max_length=200)),
                ('beneficial_document_no', models.CharField(max_length=200)),
                ('beneficial_id_expiray', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('beneficial_nationality', models.CharField(max_length=100)),
                ('beneficial_residence', models.CharField(max_length=100)),
                ('is_us_persone', models.CharField(max_length=50)),
                ('beneficial_fund_source', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CountryNationality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_type', models.CharField(max_length=500)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerTypeOrganization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_type', models.CharField(max_length=500)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryChannel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('channel', models.CharField(max_length=500)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityAccountPurpose',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('purpose', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EntityBaselRisk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(default='', max_length=500, null=True)),
                ('basel_aml_index_scores', models.IntegerField(blank=True, null=True)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityBusinessNature',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('industry_type', models.CharField(max_length=500)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_type', models.CharField(max_length=500)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntitySourceFund',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source_fund', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GeographicLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=500)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HighRiskCountries',
            fields=[
                ('serial_no', models.IntegerField(primary_key=True, serialize=False)),
                ('country_code', models.CharField(default='', max_length=50, null=True)),
                ('country_name', models.CharField(default='', max_length=500, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('map_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IdentityDocument',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document_type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('account_date', models.DateTimeField(auto_now_add=True)),
                ('cif_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('id_type', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('customer_id', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('document_expiry_date', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gender', models.CharField(default='', max_length=50, null=True)),
                ('account_title', models.CharField(default='', max_length=100, null=True)),
                ('account_number', models.CharField(default='', max_length=50, null=True)),
                ('branch_name', models.CharField(default='', max_length=50, null=True)),
                ('branch_code', models.CharField(default='', max_length=50, null=True)),
                ('iban_number', models.CharField(default='', max_length=50, null=True)),
                ('customer_name', models.CharField(default='', max_length=50, null=True)),
                ('father_name', models.CharField(default='', max_length=50, null=True)),
                ('birth_date', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('birth_place', models.CharField(default='', max_length=100, null=True)),
                ('nationality', models.CharField(default='', max_length=50, null=True)),
                ('residence_status', models.CharField(default='', max_length=100, null=True)),
                ('residence_country', models.CharField(default='', max_length=100, null=True)),
                ('current_address', models.CharField(default='', max_length=200, null=True)),
                ('permanent_addres', models.CharField(default='', max_length=200, null=True)),
                ('district', models.CharField(default='', max_length=100, null=True)),
                ('province', models.CharField(default='', max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100, null=True)),
                ('zipcode', models.CharField(default='', max_length=100, null=True)),
                ('email', models.CharField(default='', max_length=100, null=True)),
                ('mobile_number', models.CharField(default='', max_length=100, null=True)),
                ('fax_number', models.CharField(default='', max_length=100, null=True)),
                ('residential_number', models.CharField(default='', max_length=100, null=True)),
                ('office_number', models.CharField(default='', max_length=100, null=True)),
                ('customer_type', models.CharField(default='', max_length=300, null=True)),
                ('product_type', models.CharField(max_length=300)),
                ('delivery_channel', models.CharField(default='', max_length=300, null=True)),
                ('account_purpose', models.CharField(default='', max_length=300, null=True)),
                ('mode_of_transactions', models.CharField(default='', max_length=300, null=True)),
                ('fund_source', models.CharField(default='', max_length=50, null=True)),
                ('number_debit_transaction', models.CharField(default='', max_length=100, null=True)),
                ('amount_debit_transaction', models.CharField(default='', max_length=100, null=True)),
                ('number_credit_transaction', models.CharField(default='', max_length=100, null=True)),
                ('amount_credit_transaction', models.CharField(default='', max_length=100, null=True)),
                ('risk_category', models.CharField(default='', max_length=50, null=True)),
                ('risk_score', models.IntegerField(default=0, null=True)),
                ('diligence_type', models.CharField(default='', max_length=50, null=True)),
                ('pep_status', models.CharField(default='', max_length=30, null=True)),
                ('beneficial_ownership', models.CharField(default='', max_length=50, null=True)),
                ('user_image', models.ImageField(blank=True, default='', null=True, upload_to='identification/customer-profile-pics/')),
                ('screening_performed', models.BooleanField(default=False)),
                ('beneficial_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.beneficial')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualAccountPurpose',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('purpose', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('org_type', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PEP',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('high_rank_official', models.CharField(default='', max_length=50, null=True)),
                ('high_rank_official_type', models.CharField(default='', max_length=200, null=True)),
                ('legislative_assembly', models.CharField(default='', max_length=100, null=True)),
                ('legislative_assembly_type', models.CharField(default='', max_length=200, null=True)),
                ('judicial_official', models.CharField(default='', max_length=100, null=True)),
                ('judicial_official_type', models.CharField(default='', max_length=200, null=True)),
                ('public_function', models.CharField(default='', max_length=50, null=True)),
                ('public_function_type', models.CharField(default='', max_length=200, null=True)),
                ('diplomat', models.CharField(default='', max_length=50, null=True)),
                ('diplomat_type', models.CharField(default='', max_length=200, null=True)),
                ('military_official', models.CharField(default='', max_length=50, null=True)),
                ('military_official_type', models.CharField(default='', max_length=200, null=True)),
                ('senior_position_status', models.CharField(default='', max_length=50, null=True)),
                ('senior_position_status_type', models.CharField(default='', max_length=200, null=True)),
                ('high_risk_ranking_official', models.CharField(default='', max_length=50, null=True)),
                ('high_risk_ranking_official_type', models.CharField(default='', max_length=200, null=True)),
                ('member_of_ruling_families', models.CharField(default='', max_length=50, null=True)),
                ('member_of_ruling_familiesl_position', models.CharField(default='', max_length=200, null=True)),
                ('immediate_family_member', models.CharField(default='', max_length=50, null=True)),
                ('immediate_family_member_section_no', models.CharField(default='', max_length=50, null=True)),
                ('immediate_family_member_name', models.CharField(default='', max_length=50, null=True)),
                ('immediate_family_member_relation', models.CharField(default='', max_length=50, null=True)),
                ('pep_wealth_source', models.CharField(default='', max_length=50, null=True)),
                ('pep_share_holdig', models.CharField(default='', max_length=50, null=True)),
                ('pep_country', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_type', models.CharField(max_length=500)),
                ('risk_category', models.CharField(blank=True, max_length=20, null=True)),
                ('risk_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceFundIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source_fund', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionsModeEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trans_mode', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionsModeIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trans_mode', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ScreenStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_type', models.CharField(max_length=30)),
                ('screen_date', models.CharField(max_length=40)),
                ('individual', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.individual')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('account_date', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('industry_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('business_nature', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('organization_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('corporation_name', models.CharField(default='', max_length=50, null=True)),
                ('corporation_date', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('corporation_type', models.CharField(default='', max_length=100, null=True)),
                ('account_title', models.CharField(default='', max_length=100, null=True)),
                ('account_number', models.CharField(default='', max_length=50, null=True)),
                ('branch_name', models.CharField(default='', max_length=50, null=True)),
                ('branch_code', models.CharField(default='', max_length=50, null=True)),
                ('address', models.CharField(default='', max_length=200, null=True)),
                ('district', models.CharField(default='', max_length=100, null=True)),
                ('province', models.CharField(default='', max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100, null=True)),
                ('country', models.CharField(default='', max_length=100, null=True)),
                ('zipcode', models.CharField(default='', max_length=100, null=True)),
                ('customer_type', models.CharField(default='', max_length=300, null=True)),
                ('product_type', models.CharField(default='', max_length=300, null=True)),
                ('delivery_channel', models.CharField(default='', max_length=300, null=True)),
                ('risk_category', models.CharField(default='', max_length=50, null=True)),
                ('risk_score', models.IntegerField(default=0, null=True)),
                ('diligence_type', models.CharField(default='', max_length=50, null=True)),
                ('pep_status', models.CharField(default='', max_length=300, null=True)),
                ('account_purpose', models.CharField(default='', max_length=300, null=True)),
                ('mode_of_transactions', models.CharField(default='', max_length=300, null=True)),
                ('fund_source', models.CharField(default='', max_length=50, null=True)),
                ('screening_performed', models.BooleanField(default=False)),
                ('pep_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.pep')),
            ],
        ),
        migrations.AddField(
            model_name='individual',
            name='pep_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.pep'),
        ),
        migrations.CreateModel(
            name='EntityScreenStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_type', models.CharField(max_length=30)),
                ('screen_date', models.CharField(max_length=40)),
                ('organization', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='identification.organization')),
            ],
        ),
        migrations.CreateModel(
            name='EntityOwnershipDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=500)),
                ('owner_id', models.CharField(max_length=100)),
                ('owner_share', models.CharField(max_length=50, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identification.organization')),
            ],
        ),
    ]
