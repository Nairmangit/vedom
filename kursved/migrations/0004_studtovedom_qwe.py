# Generated by Django 2.1.4 on 2019-12-19 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kursved', '0003_auto_20191218_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='studtovedom',
            name='qwe',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kursved.stud'), max_length=40),
        ),
    ]