# Generated by Django 3.2.12 on 2022-10-25 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ravelry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('linde_hobby', models.BooleanField(default=False)),
                ('hobbii', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='yarn',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='yarn',
            name='hobbii',
        ),
        migrations.RemoveField(
            model_name='yarn',
            name='linde_hobby',
        ),
        migrations.AddField(
            model_name='yarn',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ravelry.company'),
            preserve_default=False,
        ),
    ]
