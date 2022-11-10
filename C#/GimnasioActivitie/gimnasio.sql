create database bdGym;
use bdGym;

-- Crear tabla cliente 
create table tCliente(
    codigo_cliente varchar(6) primary key not null,
    nombres varchar(30) not null
);

INSERT INTO tCliente VALUES ('000001','Carlos Priale');
INSERT INTO tCliente VALUES ('000002','Ana Gallardo');
INSERT INTO tCliente VALUES ('000003','Juan Guzman');

-- Crear tabla Referencia 
crear table tReferencia (
    c_referente varchar(6) not null,
    c_referenciado varchar(6) not null,
    fecha_ref date,
    numero_referencia integer,
    primary key (c_referente, c_referenciado)
);

INSERT INTO tReferencia(c_referente,c_referenciado,fecha_ref) VALUES ('000001','000002','01-01-2000');
INSERT INTO tReferencia(c_referente,c_referenciado,fecha_ref) VALUES ('000001','000003','01-02-2000');

alter table tReferencia
add CONSTRAINT fk_c_referente 
foreign key (c_referente) 
REFERENCES tCliente(codigo_cliente);

alter table tReferencia
add CONSTRAINT fk_c_c_referenciado 
foreign key (c_referenciado) 
REFERENCES tCliente(codigo_cliente);

-- Crear tabla pago_porHacer
create table tPago_Por_Hacer(
    codigo_pago varchar(6) primary key not null,
    cod_cliente varchar(6) not null,
    subtotal float,
    fecha_pago date,
    CONSTRAINT fk_c_cliente foreign key (cod_cliente) references tCliente(codigo_cliente)
); 

-- Crear tabla Pago_realizado
create table tPago_Realizado(
    cod_pago varchar(6) primary key not null,
    fecha_pago_realizado date,
    subt float,
    monto float
);

-- Claves foraneas para tPagoRealizdo
alter table tPago_Realizado
add CONSTRAINT fk_c_subtotal 
foreign key (subt) 
REFERENCES tPago_Por_Hacer(subtotal);

ALTER TABLE tPago_Realizado
ADD CONSTRAINT fk_c_pago 
FOREIGN KEY (cod_pago) 
REFERENCES tPago_Por_Hacer(codigo_pago);

select numero_referencia
from tReferencia
ORDER BY tReferencia.fecha_ref DESC
OFFSET 1 ROWS
FETCH FIRST 2 ROWS ONLY;



    
'''create or replace trigger tgActualizarPago
after insert on tReferencia FOR EACH ROW 
DECLARE 
BEGIN
        UPDATE tReferencia
        SET numero_referencia = @numero_referencia + 1
        WHERE c_referente = :new.c_referente
            and 
            c_referenciado = :new.c_referenciado;
    END;
/

CREATE TRIGGER tSumuno AFTER INSERT ON tReferencia
FOR EACH ROW SET @numero_referencia = @numero_referencia + 1;
WHERE codigo_pago = :new.codigo_pago'''