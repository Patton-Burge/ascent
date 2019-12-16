# Generated by Django 3.0 on 2019-12-11 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mileage_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriveToWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('distance', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='distancetowork',
            name='miles',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Commute',
        ),
    ]