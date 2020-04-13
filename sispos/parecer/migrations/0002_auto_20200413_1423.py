# Generated by Django 3.0.4 on 2020-04-13 14:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('parecer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rds1',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='rds1',
            name='atividades',
            field=models.TextField(max_length=2048, verbose_name='atividades'),
        ),
        migrations.AlterField(
            model_name='rds1',
            name='definicao',
            field=models.TextField(max_length=2048, verbose_name='definicao'),
        ),
        migrations.AlterField(
            model_name='rds1',
            name='desempenho',
            field=models.TextField(max_length=2048, verbose_name='desempenho'),
        ),
        migrations.AlterField(
            model_name='rds1',
            name='plano',
            field=models.TextField(max_length=2048, verbose_name='planos'),
        ),
        migrations.AlterField(
            model_name='rds1',
            name='resultados',
            field=models.TextField(max_length=2048, verbose_name='resultados'),
        ),
        migrations.AlterField(
            model_name='rds1',
            name='revisao',
            field=models.TextField(max_length=2048, verbose_name='revisao'),
        ),
    ]