--CURSO DESARROLLADOR FULLSTACK CodiGo Grupo G-11
--EDISON A. PESCORAN LOPEZ


--Creacion de la Tabla Direccion_Alumno
CREATE TABLE Direccion_Alumno(
    Direccion VARCHAR(200), 
    Num INT, 
    Referencia VARCHAR(150), 
    Alumno_Id INT);

--Ingreso de la Informacion

INSERT INTO Direccion_Alumno(Direccion, Num, Referencia, Alumno_Id) VALUES
('Calle los Girasoles', 750, 'Al costado de la polleria', 1),
('Calle Los aviadores', 1050, NULL,2),
('Av El Sol', 125, 'Del ovalo a media cuadra', 1),
('Av Los Gallos', 777, NULL, 3),
('Av Tupac Yupanqui', 123, NULL, 7),
('Av Siempre viva', 7840, 'Al frente de la ferreteria', 8),
('Calle Los martires', 6520, NULL, 5),
('Pasaje de las flores', 526, NULL, 4),
('Alameda Chabuca', 740, 'Dos cuadras de la piscina', 6),
('Callejon Bravo', 14, 'A dos casas de la reja', 3)

-- 1. Buscar todas las direcciones que sean calles

SELECT Direccion FROM Direccion_Alumno WHERE direccion LIKE '%Calle%';

-- 2. Listar todas las direcciones sin referencia

 SELECT Direccion FROM Direccion_Alumno WHERE Referencia IS NULL;

-- 3. Listar todas las direcciones que sean menores que 1000

SELECT Direccion FROM Direccion_Alumno WHERE Num < 1000;

-- 4. Listar todas las direcciones que sean o Av o Pasaje

SELECT Direccion FROM Direccion_Alumno WHERE direccion LIKE '%Av%' or direccion LIKE '%Pasaje%';

-- 5. Listar todas las direcciones de los alumnos 1 o que vivan en calles o que no tengan referencias

 SELECT Direccion FROM Direccion_Alumno WHERE Alumno_Id=1 AND (direccion LIKE '%Calle%' OR Referencia IS NULL);

-- 6. Listar todas las direcciones que sean calle y que su referencia no sea nula y que su alumno sea el 1

 SELECT Direccion FROM Direccion_Alumno WHERE Alumno_Id=1 AND (direccion LIKE '%Calle%' OR Referencia IS NOT NULL);