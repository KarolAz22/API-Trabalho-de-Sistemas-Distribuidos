# Generated by Django 4.1.2 on 2022-11-06 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_alter_monograph_fk_id_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monograph',
            name='fk_id_author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='records.author'),
        ),
    ]
