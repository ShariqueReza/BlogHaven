# Generated by Django 5.1.3 on 2024-11-17 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parents',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to='app.comments'),
        ),
    ]
