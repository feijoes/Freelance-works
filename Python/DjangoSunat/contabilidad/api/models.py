from django.db import models

# Create your models here.

class TipoComprobante(models.Model):
    OPCIONES_COMPROBANTE = [
        ('01', 'Factura'),
        ('02', 'Boleta'),
        ('05', 'Nota de crédito'),
    ]
    
    TIPO_MONEDA = [
        ('soles', 'Soles'),
        ('dolares', 'Dolares'),       
    ]

    GLOSA_GENERAL = [
        ('combustible', 'Combustible'),
        ('sctr', 'SCTR'),
        ('examen_medico', 'EXAMEN MEDICO'),
    ]

    IGV = [
        ('18', '18%'),
        ('10', '10%'),
        ('0', '0%'),
    ]


    tipo_comprobante = models.CharField(max_length=20, choices=OPCIONES_COMPROBANTE, default='Factura')
    tipo_moneda = models.CharField(max_length=20, choices=TIPO_MONEDA, default='Soles')
    serieFactura=models.CharField(max_length=50)
    numeroFactura =models.CharField(max_length=50)
    glosa_general = models.CharField(max_length=20, choices=GLOSA_GENERAL)
    fecha_emision = models.DateField()
    ruc_emisor = models.CharField(max_length=11, default='')
    ruc_receptor = models.CharField(max_length=11)
    glosa_especifica = models.CharField(max_length=255, default='Glosa por defecto')
    igv = models.CharField(max_length=20, choices=IGV, default='18%')
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    monto_igv = models.DecimalField(max_digits=10, decimal_places=2)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.tipo_comprobante} - {self.tipo_moneda} - {self.serieFactura} - {self.numeroFactura} - {self.ruc_emisor} - ({self.fecha_emision}) - {self.monto_total}"


class RucVerificado(models.Model):
    ESTADO_CONTRIBUYENTE = [
        ('00', 'ACTIVO'),
        ('01', 'BAJA PROVISIONAL'),
        ('02', 'BAJA PROV. POR OFICIO'),
        ('03', 'SUSPENSION TEMPORAL'),
        ('10', 'BAJA DEFINITIVA'),
        ('11', 'BAJA DE OFICIO'),
        ('22', 'INHABILITADO-VENT.UNICA'),
    ]

    CONDICION_DOMICILIO_CONTRIBUYENTE = [
        ('00', 'HABIDO'),
        ('09', 'PENDIENTE'),
        ('11', 'POR VERIFICAR'),
        ('12', 'NO HABIDO'),
        ('20', 'NO HALLADO'),
    ]
    ESTADO_COPROBANTE = [
        ("0","NO EXISTE"),
        ("1","ACEPTADO"),
        ("2","ANULADO"),
        ("3","AUTORIZADO"),
        ("4","NO AUTORIZADO"),
    ]
    success  = models.BooleanField()
    estadoCp =  models.CharField(max_length=20, choices=ESTADO_COPROBANTE, default='NO EXISTE')
    estadoRuc = models.CharField(max_length=20, choices=ESTADO_CONTRIBUYENTE, default='ACTIVO')
    condDomiRuc = models.CharField(max_length=20, choices=CONDICION_DOMICILIO_CONTRIBUYENTE, default='HABIDO')
    
    
class VerificarRuc(models.Model):
    
    CODIGO_TIPO_COMPROBANTE = [
        ("01","FACTURA"),
        ("03","BOLETA DE VENTA"),
        ("04","LIQUIDACION DE COMPRA"),
        ("07","NOTA DE CREDITO"),
        ("08","NOTA DE DEBIDO"),
        ("R1","RECIBO POR HONORARIOS"),
        ("R7","NOTA DE CREDITO DE RECIBOS"),
    ]
    numRuc = models.CharField(max_length=11, default='',primary_key=True)
    codComp = models.CharField(max_length=2, choices=CODIGO_TIPO_COMPROBANTE, default="01")
    numeroSerie = models.CharField(max_length=4, default='')
    numero = models.IntegerField()
    fechaEmision = models.DateField()
    monto = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    
    