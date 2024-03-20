# Generated by Django 2.2.5 on 2019-09-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_version_1', '0004_bus_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_id', models.IntegerField()),
                ('seat_row', models.IntegerField()),
                ('seat_col', models.IntegerField()),
            ],
            options={
                'db_table': 'seat',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_id', models.IntegerField()),
                ('amt', models.FloatField()),
                ('bus_id', models.IntegerField()),
                ('seat_row', models.IntegerField()),
                ('seat_col', models.IntegerField()),
            ],
            options={
                'db_table': 'trans',
            },
        ),
        migrations.AddField(
            model_name='bus',
            name='available_seats',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='bus',
            name='time',
            field=models.TimeField(),
        ),
    ]