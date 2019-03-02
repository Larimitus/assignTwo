# Generated by Django 2.0.5 on 2019-02-28 21:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('p_description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('pickup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('setup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cleanup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 28, 21, 38, 53, 520728, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='service',
            name='cust_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='product',
            name='cust_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='crm.Customer'),
        ),
    ]
