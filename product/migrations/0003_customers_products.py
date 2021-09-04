# Generated by Django 3.2.6 on 2021-08-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_order_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('mode_of_payment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('product_weight', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('customer_id_who_purchased', models.CharField(max_length=100)),
            ],
        ),
    ]