# Generated by Django 2.2.5 on 2019-09-25 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0006_auto_20190925_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomtype', models.IntegerField(choices=[(1, 'A/c double'), (2, 'A/c single'), (3, 'Non A/C Double'), (4, 'Non A/C single')], default=1)),
                ('roompricing', models.IntegerField(default=0)),
                ('Numguests', models.IntegerField(choices=[(1, '2'), (2, '3')], default=1)),
                ('Amenities', models.CharField(max_length=100)),
                ('hotelname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='live.Hotel')),
            ],
        ),
    ]
