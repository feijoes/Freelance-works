# Generated by Django 4.1.4 on 2023-02-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RucVerificado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("success", models.BooleanField()),
                (
                    "estadoCp",
                    models.CharField(
                        choices=[
                            ("0", "NO EXISTE"),
                            ("1", "ACEPTADO"),
                            ("2", "ANULADO"),
                            ("3", "AUTORIZADO"),
                            ("4", "NO AUTORIZADO"),
                        ],
                        default="NO EXISTE",
                        max_length=20,
                    ),
                ),
                (
                    "estadoRuc",
                    models.CharField(
                        choices=[
                            ("00", "ACTIVO"),
                            ("01", "BAJA PROVISIONAL"),
                            ("02", "BAJA PROV. POR OFICIO"),
                            ("03", "SUSPENSION TEMPORAL"),
                            ("10", "BAJA DEFINITIVA"),
                            ("11", "BAJA DE OFICIO"),
                            ("22", "INHABILITADO-VENT.UNICA"),
                        ],
                        default="ACTIVO",
                        max_length=20,
                    ),
                ),
                (
                    "condDomiRuc",
                    models.CharField(
                        choices=[
                            ("00", "HABIDO"),
                            ("09", "PENDIENTE"),
                            ("11", "POR VERIFICAR"),
                            ("12", "NO HABIDO"),
                            ("20", "NO HALLADO"),
                        ],
                        default="HABIDO",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VerificarRuc",
            fields=[
                (
                    "numRuc",
                    models.CharField(
                        default="", max_length=11, primary_key=True, serialize=False
                    ),
                ),
                (
                    "codComp",
                    models.CharField(
                        choices=[
                            ("01", "FACTURA"),
                            ("03", "BOLETA DE VENTA"),
                            ("04", "LIQUIDACION DE COMPRA"),
                            ("07", "NOTA DE CREDITO"),
                            ("08", "NOTA DE DEBIDO"),
                            ("R1", "RECIBO POR HONORARIOS"),
                            ("R7", "NOTA DE CREDITO DE RECIBOS"),
                        ],
                        default="01",
                        max_length=2,
                    ),
                ),
                ("numeroSerie", models.CharField(default="", max_length=4)),
                ("numero", models.IntegerField()),
                ("fechaEmision", models.DateField()),
                (
                    "monto",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ConsultarRuc",
        ),
    ]
