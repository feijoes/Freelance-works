from django.db import models

# Create your models here.
class NRuc_info(models.Model):
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
    ruc= models.CharField(max_length=11,primary_key=True)
    nombre = models.CharField(max_length=255)
    tipoDocumento = models.CharField(max_length=255)
    numeroDocumento = models.CharField(max_length=255)
    estado = models.CharField(max_length=255,choices=ESTADO_CONTRIBUYENTE,default="ACTIVO")
    condicion = models.CharField(max_length=255,choices=CONDICION_DOMICILIO_CONTRIBUYENTE)
    direccion = models.CharField(max_length=255)
    ubigeo = models.CharField(max_length=255)
    viaTipo = models.CharField(max_length=255)
    viaNombre =models.CharField(max_length=255)
    zonaCodigo = models.CharField(max_length=255)
    zonaTipo = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    lote = models.CharField(max_length=255)
    dpto = models.CharField(max_length=255)
    manzana = models.CharField(blank=True,max_length=255)
    kilometro = models.CharField(blank=True,max_length=255)
    distrito = models.CharField(blank=True,max_length=255)
    provincia = models.CharField(blank=True,max_length=255)
    departamento = models.CharField(blank=True,max_length=255)
    
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
    razonSocial = models.CharField(max_length=255)
    estadoCp =  models.CharField(max_length=20, choices=ESTADO_COPROBANTE, default='NO EXISTE',null=True,blank=True)
    estadoRuc = models.CharField(max_length=20, choices=ESTADO_CONTRIBUYENTE, default='ACTIVO',null=True,blank=True)
    condDomiRuc = models.CharField(max_length=20, choices=CONDICION_DOMICILIO_CONTRIBUYENTE, default='HABIDO',null=True,blank=True)
    ruc_info =  models.ForeignKey(NRuc_info,on_delete=models.CASCADE)
    

    
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
   

    
    
    
    
   