# Generated by Django 2.2.5 on 2019-09-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0011_auto_20190926_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(choices=[(1, 'A/c double'), (2, 'A/c single'), (3, 'Non A/C Double'), (4, 'Non A/C single')], default=None, max_length=200),
        ),
    ]
