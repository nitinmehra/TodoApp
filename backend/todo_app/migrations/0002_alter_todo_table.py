# Generated by Django 3.2.7 on 2021-09-10 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='todo',
            table='todo_task',
        ),
    ]
