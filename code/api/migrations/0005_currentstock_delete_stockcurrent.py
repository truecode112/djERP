# Generated by Django 4.0.4 on 2022-04-22 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_attachment_attachedfile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('currentStock', models.PositiveIntegerField()),
                ('lastUpdateDate', models.DateTimeField(auto_now=True)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CurrentStockPart', to='api.part')),
            ],
        ),
        migrations.DeleteModel(
            name='StockCurrent',
        ),
    ]