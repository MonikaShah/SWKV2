# Generated by Django 3.1.1 on 2020-12-17 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swk', '0003_auto_20201216_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('zone_name', models.CharField(blank=True, max_length=100, null=True)),
                ('zone_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'zones',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='zone',
        ),
        migrations.AlterField(
            model_name='tracksheet',
            name='zone_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swk.zones'),
        ),
    ]