# Generated by Django 3.0.5 on 2020-06-29 20:43

from django.db import migrations, models
import lets_ride.models.ride_request


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('travel_date_time', models.DateTimeField(blank=True, null=True)),
                ('flexible_timings', models.BooleanField(default=False)),
                ('flexible_from_date_time', models.DateTimeField(blank=True, null=True)),
                ('flexible_to_date_time', models.DateTimeField(blank=True, null=True)),
                ('asset_quantity', models.IntegerField()),
                ('asset_type', models.CharField(choices=[('BAG', 'BAG'), ('LAPTOP', 'LAPTOP'), ('DOCUMENTS', 'DOCUMENTS'), ('OTHERS', 'OTHERS')], max_length=50)),
                ('asset_type_others', models.CharField(blank=True, max_length=100, null=True)),
                ('asset_sensitivity', models.CharField(choices=[('LOW', 'LOW'), ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM')], max_length=50)),
                ('user_id', models.IntegerField()),
                ('accepted_by', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('travel_date_time', models.DateTimeField(blank=True, null=True)),
                ('flexible_timings', models.BooleanField(default=False)),
                ('flexible_from_date_time', models.DateTimeField(blank=True, null=True)),
                ('flexible_to_date_time', models.DateTimeField(blank=True, null=True)),
                ('seats', models.IntegerField(validators=[lets_ride.models.ride_request.validate_seats])),
                ('laguage_quantity', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('accepted_by_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShareRide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('travel_date_time', models.DateTimeField(blank=True, null=True)),
                ('flexible_timings', models.BooleanField(default=False)),
                ('flexible_from_date_time', models.DateTimeField(blank=True, null=True)),
                ('flexible_to_date_time', models.DateTimeField(blank=True, null=True)),
                ('seats', models.IntegerField()),
                ('asset_quantity', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TravelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('travel_date_time', models.DateTimeField(blank=True, null=True)),
                ('flexible_timings', models.BooleanField(default=False)),
                ('flexible_from_date_time', models.DateTimeField(blank=True, null=True)),
                ('flexible_to_date_time', models.DateTimeField(blank=True, null=True)),
                ('travel_medium', models.CharField(choices=[('BUS', 'BUS'), ('TRAIN', 'TRAIN'), ('FLIGHT', 'FLIGHT')], max_length=50)),
                ('asset_quantity', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
