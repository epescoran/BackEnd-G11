--Crear base de datos
create database pruebas;


--listar bases de datos en el servidor
--Comandos para PSQL
--En comandos PSQL es opcional el ;
\l 

--Conectarse a una Base de datos
\c Database 

--Crear tipo de datos
CREATE TYPE tipo_sexo as ENUM('MASCULINO','FEMENINO','PANSEXUAL','OTRES');

--Crear Tabla
CREATE TABLE alumnos(
Id SERIAL NOT NULL PRIMARY KEY,
Nombre TEXT NOT NULL,
Apellido VARCHAR(100),
Sexo tipo_sexo DEFAULT 'OTRES',
Fecha_Creacion TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
Matriculado BOOLEAN DEFAULT FALSE
);
--mostrar tablas de la DB
\dt

--mostrar detalle de la tabla indicada
 \d alumnos

 --Mostrara todas la tablas y sus indices
 \d

--ver los enumerables de un tipo de datos
 SELECT enum_range(NULL::tipo_sexo)
;

--Insertar Registros

pruebas=# INSERT INTO alumnos(Id, Nombre, Apellido, Sexo, Fecha_Creacion, matriculado) VALUES
pruebas-# (DEFAULT , 'Edison','Pescoran','MASCULINO',DEFAULT,TRUE);

--Insertar columnas que no tengan valores por defecto
pruebas=# INSERT INTO alumnos(Nombre, Apellido) VALUES
pruebas-# ('Victor','Mayta');

--Ingresar varios registros
pruebas=# INSERT INTO alumnos(Nombre, Apellido) VALUES
pruebas-# ('Juana','Martinez'),
pruebas-# ('Luis','Lopez'),
pruebas-# ('Carlos','Quispe');

--Select
SELECT * FROM alumnos WHERE sexo='MASCULINO' OR matriculado=false;

SELECT * FROM alumnos WHERE nombre like '%o%';