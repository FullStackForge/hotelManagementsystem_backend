# Generated by Django 5.1.3 on 2024-12-17 16:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_alter_roomtype_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
