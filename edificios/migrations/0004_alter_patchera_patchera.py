# Generated by Django 4.0.3 on 2022-04-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificios', '0003_alter_apartamento_apartamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patchera',
            name='patchera',
            field=models.CharField(max_length=5),
        ),
    ]
