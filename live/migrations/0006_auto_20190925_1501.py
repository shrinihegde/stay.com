# Generated by Django 2.2.5 on 2019-09-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0005_auto_20190925_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotelimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotelstars',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3),
        ),
    ]
