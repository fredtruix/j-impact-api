# Generated by Django 4.0.4 on 2023-05-22 17:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_group_name_alter_group_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]
