# Generated by Django 4.2 on 2023-04-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_events_discipline_events_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(default='a', max_length=150),
        ),
    ]
