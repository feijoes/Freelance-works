CREATE TABLE Programa (
    idprograma INT PRIMARY KEY,
    description VARCHAR(255)
);
CREATE TABLE Proyecto (
    IDproyecto INT PRIMARY KEY,
    nombre VARCHAR(255),
    acronico VARCHAR(10),
    presupuesto DECIMAL(10,2),
    IDprograma INT FOREIGN KEY REFERENCES Programa(IDprograma),
    fecha_inicio DATE,
    fecha_fin DATE,
    descrip_objeto VARCHAR(MAX)
);
CREATE TABLE Rol (
    IDrol INT PRIMARY KEY,
    description VARCHAR(255)
);
CREATE TABLE Oficina (
    IDoficina INT PRIMARY KEY,
    description VARCHAR(255),
	direccion VARCHAR(255),
	telefono VARCHAR(20)
);
CREATE TABLE Gradoacademico (
    IDgradoacademico INT PRIMARY KEY,
    description VARCHAR(255),
	anotitulacion INT,
	telefono VARCHAR(20)
);
CREATE TABLE Profesor (
    IDprofesor INT PRIMARY KEY,
    nombre VARCHAR(255),
	apellidos VARCHAR(255),
	IDoficina INT FOREIGN KEY REFERENCES Oficina(IDoficina),
	IDgradoacademico INT FOREIGN KEY REFERENCES Gradoacademico(IDgradoacademico),
	telefono VARCHAR(20)
);
CREATE TABLE Participación  (
    IDparticipacion INT PRIMARY KEY,
    fecha_inicio DATE,
    fecha_fin DATE,
    IDrol INT FOREIGN KEY REFERENCES Rol(IDrol),
	IDprofesor INT FOREIGN KEY REFERENCES Profesor(IDprofesor),
	IDproyecto INT FOREIGN KEY REFERENCES Proyecto(IDproyecto)
);
CREATE TABLE Descriptor(
	IDdescriptor INT PRIMARY KEY,
	descripcion VARCHAR(255)
);
CREATE TABLE Linea_invest(
	IDlinea_invest INT PRIMARY KEY,
	nombre VARCHAR(255)
);
CREATE TABLE Linea_descrip(
	IDlinea_descrip INT PRIMARY KEY,
	IDlinea_invest INT FOREIGN KEY REFERENCES Linea_invest(IDlinea_invest),
	IDdescrip INT FOREIGN KEY REFERENCES Descriptor(IDdescriptor)
);
CREATE TABLE Publicacion  (
    IDpublicacion INT PRIMARY KEY,
	nro_dec INT,
	titulo VARCHAR(30),
	ID_lineal INT FOREIGN KEY REFERENCES Linea_invest(IDlinea_invest),
	IDproyecto INT FOREIGN KEY REFERENCES Proyecto(IDproyecto)
);

CREATE TABLE Registroslineas(
	IDregistroslineas INT PRIMARY KEY
	IDlineal_invest	INT FOREIGN KEY REFERENCES Linea_invest(IDlinea_invest),

	IDpublicacion INT FOREIGN KEY REFERENCES Publicacion(IDpublicacion)
);


CREATE TABLE Tipocongreso (
	IDtipocongreso INT PRIMARY KEY,
	descripcion VARCHAR(255)
);
CREATE TABLE Pais(
	IDpais INT PRIMARY KEY,
	descripcion VARCHAR(255)
);
CREATE TABLE Lugar(
	IDlugar INT PRIMARY KEY,
	descripcion VARCHAR(255),
	direccion VARCHAR(255),
	IDpais INT FOREIGN KEY REFERENCES Pais(IDpais)

);
CREATE TABLE Editorial(
	IDeditorial INT PRIMARY KEY,
	descripcion VARCHAR(255),
	direccion VARCHAR(255),

);
CREATE TABLE Public_revista(
	IDpubli_revista INT PRIMARY KEY,
	nom_revista VARCHAR(100),
	titulo VARCHAR(30),
	IDeditoral INT FOREIGN KEY REFERENCES Editorial(IDeditorial),
	volumen INT,
	numero INT,
	pagina_inicio INT,
	paginal_final INT
);
CREATE TABLE Publi_congreso (
	IDpubli_congreso INT PRIMARY KEY,
	nom_cong VARCHAR(100),
	IDtipo_congreso INT FOREIGN KEY REFERENCES Tipocongreso(IDtipocongreso),
	fecha_inicio DATE,
	fecha_fin DATE,
	IDlugar INT FOREIGN KEY REFERENCES Lugar(IDlugar),
	IDeditoral INT FOREIGN KEY REFERENCES Editorial(IDeditorial),
	IDpublicacion INT FOREIGN KEY REFERENCES Publicacion(IDpublicacion)
);


CREATE TABLE Auditoria  (
    IDauditoria INT PRIMARY KEY,
    IDprofesor INT FOREIGN KEY REFERENCES Profesor(IDprofesor),
	IDpublicacion INT  FOREIGN KEY REFERENCES Publicacion(IDpublicacion),
	IDproyecto INT  FOREIGN KEY REFERENCES Proyecto(IDproyecto)
);