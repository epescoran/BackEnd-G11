
-- Join
SELECT * from direcciones INNER JOIN alumnos on direcciones.alumno_id= alumnos.id;


insert into alumnos(nombre , apellido) values('Juan','Zuñiga');


INSERT INTO direcciones (direccion, numero, referencia, alumno_id) VALUES ('Calle los Tulipanes',429 , 'Al costado de la bodega', NULL);

SELECT * from direcciones INNER JOIN alumnos on direcciones.alumno_id= alumnos.id;


SELECT * from direcciones LEFT JOIN alumnos on direcciones.alumno_id= alumnos.id;


SELECT * from direcciones RIGHT JOIN alumnos on direcciones.alumno_id= alumnos.id;


SELECT * from direcciones FULL JOIN alumnos on direcciones.alumno_id= alumnos.id;

--Crear una tabla llamada Cursos
--Nombre TEXT
--Descripcion VARCHAR(100)
--habilitado BOOLEAN

CREATE TABLE alumnos_cursos(
id SERIAL PRIMARY KEY,
alumno_id INT NOT NULL,
curso_id INT NOT NULL,
UNIQUE (alumno_id, curso_id),
CONSTRAINT fk_alumnos FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
CONSTRAINT fk_cursos FOREIGN KEY (curso_id) REFERENCES cursos(id)
);


INSERT INTO cursos (nombre, descripcion, habilitado) VALUES
                    ('Matematica', 'Matematica con algebra', true),
                    ('CTA', 'Cienta Tecnologia y Ambiente', true),
                    ('Comunicacion', 'Letras', true),
                    ('Arte', 'Artes plasticas', false),
                    ('Ingles', 'English for kids', true);


INSERT INTO alumnos_cursos (alumno_id, curso_id) VALUES
                               (1,     1),
                               (2,     1),
                               (1,     3),
                               (3,     4),
                               (3,     2),
                               (3,     3);

-- Haciendo un join desde la tabla alumnos, pasando por la tabla alumnos_cursos y terminando en la tabla cursos
SELECT * FROM
alumnos INNER JOIN alumnos_cursos
ON alumnos.id = alumnos_cursos.alumno_id
INNER JOIN cursos
ON alumnos_cursos.curso_id = cursos.id;