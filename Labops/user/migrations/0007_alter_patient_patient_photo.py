# Generated by Django 4.1.13 on 2024-01-31 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_patient_age_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_photo',
            field=models.ImageField(default='NONE', upload_to='user/images/patient'),
        ),
    ]
