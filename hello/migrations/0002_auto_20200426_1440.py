# Generated by Django 3.0.5 on 2020-04-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greeting',
            name='when',
        ),
        migrations.AddField(
            model_name='greeting',
            name='name',
            field=models.CharField(default='emtpy', max_length=80),
            preserve_default=False,
        ),
    ]
