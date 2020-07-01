# Generated by Django 3.0.1 on 2020-06-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200630_2032'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Done',
        ),
        migrations.RemoveField(
            model_name='listtodo',
            name='date',
        ),
        migrations.AddField(
            model_name='listtodo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]