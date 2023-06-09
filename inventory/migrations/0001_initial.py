# Generated by Django 3.1.8 on 2023-04-06 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug_name', models.SlugField(max_length=3, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('industry', models.CharField(max_length=20, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug_name', models.SlugField(max_length=4, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Lot_description',
            fields=[
                ('lot_id', models.CharField(default='default_lot', max_length=20, primary_key=True, serialize=False)),
                ('due_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movement_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remission', models.CharField(max_length=40, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customers')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.IntegerField(null=True)),
                ('ean', models.BigIntegerField(null=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50, null=True)),
                ('perishable', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customers')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Warehouses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.cities')),
            ],
            options={
                'verbose_name_plural': 'Warehouses',
            },
        ),
        migrations.CreateModel(
            name='Warehouse_admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouses')),
            ],
            options={
                'verbose_name_plural': 'Warehouses_Admins',
            },
        ),
        migrations.CreateModel(
            name='Products_on_warehouses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('lot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.lot_description')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available', to='inventory.products')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouses')),
            ],
        ),
        migrations.CreateModel(
            name='Movements_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField()),
                ('description', models.CharField(max_length=200, null=True)),
                ('lot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.lot_description')),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_details', to='inventory.movements')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.products')),
            ],
        ),
        migrations.AddField(
            model_name='movements',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouses'),
        ),
        migrations.AddField(
            model_name='lot_description',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.products'),
        ),
    ]
