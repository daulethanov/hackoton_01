# Generated by Django 3.2.15 on 2022-09-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_checkdocument_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkdocument',
            name='status',
            field=models.CharField(choices=[(1, 'Присужден'), (2, 'Не присужден')], default=2, max_length=10),
        ),
    ]
