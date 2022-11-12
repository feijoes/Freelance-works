create database bdgym;
use bdgym;

-- Crear tabla cliente 
create table clientes(
    Nombre varchar(36) primary key not null,
    nPersonas int not null,
    contrasena varchar(36) not null
);