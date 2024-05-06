# Generated by Django 4.2.9 on 2024-05-02 13:36

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
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='ExternalNoiseLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='FuelEconomy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GripOnWetSurfaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LoadIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LoadIndexForDual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Seasonality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SpeedIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Width',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='tires/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=255)),
                ('promotion', models.DecimalField(decimal_places=2, max_digits=255)),
                ('quantity', models.IntegerField()),
                ('state', models.BooleanField(default=False)),
                ('discount', models.BooleanField(default=False)),
                ('runflat', models.BooleanField(default=False)),
                ('offroad', models.BooleanField(default=False)),
                ('set', models.BooleanField()),
                ('in_stock', models.BooleanField()),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.cartype')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.category')),
                ('diameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.diameter')),
                ('external_noise_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.externalnoiselevel')),
                ('fuel_economy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.fueleconomy')),
                ('grip_on_wet_surfaces', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.griponwetsurfaces')),
                ('load_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.loadindex')),
                ('load_index_for_dual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.loadindexfordual')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tires.manufacturer')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.model')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.profile')),
                ('seasonality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.seasonality')),
                ('speed_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.speedindex')),
                ('width', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.width')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('rating', models.PositiveIntegerField(choices=[(1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')])),
                ('tires', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tires.tires')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('tires', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires.tires')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'tires')},
            },
        ),
    ]
