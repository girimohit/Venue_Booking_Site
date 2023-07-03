# Generated by Django 4.2.2 on 2023-07-01 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formatapp', '0006_remove_your_activity_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditorium',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
