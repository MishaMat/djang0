# Generated by Django 4.0.1 on 2022-01-23 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms6', '0002_flagmodel_newsmodel_commentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='news',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='forms6.newsmodel'),
        ),
    ]
