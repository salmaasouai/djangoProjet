# Generated by Django 4.2 on 2024-10-15 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Conference', '0011_alter_conference_start_date'),
        ('Participant', '0002_alter_reservation_options_alter_participant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservationss', to='Conference.conference'),
        ),
    ]