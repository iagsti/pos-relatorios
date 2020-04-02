# Generated by Django 3.0.4 on 2020-04-01 20:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0004_relatorios_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorios',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid'),
        ),
    ]
