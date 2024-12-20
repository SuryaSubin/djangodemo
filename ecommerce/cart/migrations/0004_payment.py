# Generated by Django 5.1.2 on 2024-10-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_order_details_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=30)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=30)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
