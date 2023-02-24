# Generated by Django 4.1.7 on 2023-02-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_tipocomprobante_igv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipocomprobante',
            name='igv',
            field=models.CharField(choices=[('18', '18%'), ('10', '10%'), ('0', '0%')], default='18%', max_length=20),
        ),
    ]