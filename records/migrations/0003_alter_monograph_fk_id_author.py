# Generated by Django 4.1.2 on 2022-11-06 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_alter_monograph_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monograph',
            name='fk_id_author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='records.author'),
        ),
    ]
