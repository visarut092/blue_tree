# Generated by Django 4.1 on 2023-06-04 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformationDetail',
            fields=[
                ('info_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('info_detail_country', models.CharField(blank=True, max_length=100, null=True)),
                ('info_detail_live_phuket', models.BooleanField(default=False)),
                ('info_detail_people', models.IntegerField(default=0)),
                ('info_detail_status', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'information_detail',
            },
        ),
        migrations.CreateModel(
            name='TypeGroup',
            fields=[
                ('type_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_group_people', models.IntegerField(default=0)),
                ('type_group_detail', models.CharField(max_length=20)),
                ('type_group_stauts', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'type_group',
            },
        ),
        migrations.CreateModel(
            name='UserBooking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_agent_com', models.CharField(blank=True, max_length=55, null=True)),
                ('booking_customer_first_name', models.CharField(blank=True, max_length=55, null=True)),
                ('booking_customer_last_name', models.CharField(blank=True, max_length=55, null=True)),
                ('booking_email', models.EmailField(blank=True, max_length=55, null=True)),
                ('booking_age', models.IntegerField(default=0)),
                ('booking_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('booking_tel', models.IntegerField(default=0)),
                ('booking_voucher_code', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('booking_booking_id', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_booking',
            },
        ),
        migrations.CreateModel(
            name='InformationDetailList',
            fields=[
                ('info_list_id', models.AutoField(primary_key=True, serialize=False)),
                ('info_list_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('info_list_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('info_list_age', models.IntegerField(default=0)),
                ('info_list_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('info_list_status', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('info_list_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='info_list_info_id', to='blue_tree_api.informationdetail')),
            ],
            options={
                'db_table': 'information_detail_list',
            },
        ),
        migrations.AddField(
            model_name='informationdetail',
            name='info_detail_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='info_detail_booking_id', to='blue_tree_api.userbooking'),
        ),
        migrations.AddField(
            model_name='informationdetail',
            name='info_detail_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='info_detail_type_id', to='blue_tree_api.typegroup'),
        ),
    ]
