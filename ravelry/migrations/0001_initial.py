# Generated by Django 3.2.12 on 2022-10-25 18:40

from django.db import migrations, models
import ravelry.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yarn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('texture', models.CharField(max_length=200)),
                ('grams', models.IntegerField(default=0, null=True)),
                ('yardage', models.IntegerField(default=0, null=True)),
                ('min_gauge', models.IntegerField(default=0, null=True)),
                ('max_gauge', models.IntegerField(default=0, null=True)),
                ('gauge_divisor', models.IntegerField(default=0, null=True)),
                ('ravelry_id', models.IntegerField(default=0)),
                ('linde_hobby', models.BooleanField(default=False)),
                ('hobbii', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fiber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kind', models.IntegerField(choices=[(ravelry.enums.FiberTypes['ANIMAL_FIBER'], 0), (ravelry.enums.FiberTypes['ANIMAL_DERIVED'], 1), (ravelry.enums.FiberTypes['SYNTHETIC'], 2), (ravelry.enums.FiberTypes['PLANT_FIBERS'], 3)])),
                ('yarns', models.ManyToManyField(to='ravelry.Yarn')),
            ],
        ),
    ]