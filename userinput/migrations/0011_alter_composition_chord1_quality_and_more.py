# Generated by Django 4.0.4 on 2022-06-09 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinput', '0010_alter_track_chord1_style_alter_track_chord2_style_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='chord1_quality',
            field=models.CharField(blank=True, choices=[('', ''), ('major', 'major'), ('minor', 'minor'), ('minor7', 'minor7'), ('major7', 'major7'), ('dominant7', 'dominant7')], default='major', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='composition',
            name='chord2_quality',
            field=models.CharField(blank=True, choices=[('', ''), ('major', 'major'), ('minor', 'minor'), ('minor7', 'minor7'), ('major7', 'major7'), ('dominant7', 'dominant7')], default='major', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='composition',
            name='chord3_quality',
            field=models.CharField(blank=True, choices=[('', ''), ('major', 'major'), ('minor', 'minor'), ('minor7', 'minor7'), ('major7', 'major7'), ('dominant7', 'dominant7')], default='major', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='composition',
            name='chord4_quality',
            field=models.CharField(blank=True, choices=[('', ''), ('major', 'major'), ('minor', 'minor'), ('minor7', 'minor7'), ('major7', 'major7'), ('dominant7', 'dominant7')], default='major', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='composition',
            name='chord5_quality',
            field=models.CharField(blank=True, choices=[('', ''), ('major', 'major'), ('minor', 'minor'), ('minor7', 'minor7'), ('major7', 'major7'), ('dominant7', 'dominant7')], default='major', max_length=10, null=True),
        ),
    ]
