# Generated by Django 2.1.5 on 2019-11-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20191104_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=5, null=True),
        ),
    ]