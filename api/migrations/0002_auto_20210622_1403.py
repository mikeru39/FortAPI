# Generated by Django 3.2.4 on 2021-06-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='Tags',
            new_name='tags',
        ),
        migrations.AddField(
            model_name='table',
            name='disabled',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
