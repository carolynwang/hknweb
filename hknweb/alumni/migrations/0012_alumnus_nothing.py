# Generated by Django 2.1.3 on 2018-11-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0011_auto_20181110_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnus',
            name='nothing',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
