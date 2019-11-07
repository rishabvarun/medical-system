# Generated by Django 2.1.5 on 2019-11-03 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_prescription_finger'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescription',
            options={'ordering': ['checked', '-date']},
        ),
        migrations.AddField(
            model_name='prescription',
            name='disease',
            field=models.CharField(choices=[('Asthama', 'Asthama'), ('Cancer', 'Cancer'), ('Cholera', 'Cholera'), ('Common cold', 'Common cold'), ('Diarrhoea', 'Diarrhoea'), ('Dengue', 'Dengue'), ('Malaria', 'Malaria'), ('Typhoid', 'Typhoid')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Doctor'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medicine',
            field=models.CharField(choices=[('Synthroid', 'Synthroid'), ('Crestor', 'Crestor'), ('Ventolin HFA', 'Ventolin HFA'), ('Nexium', 'Nexium'), ('Lyrica', 'Lyrica'), ('Vyvanse', 'Vyvanse'), ('Lantus Solostar', 'Lantus Solostar'), ('Advair Diskus', 'Advair Diskus')], max_length=15, null=True),
        ),
    ]