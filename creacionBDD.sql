use gestion_empleados;

DROP TABLE IF EXISTS categoria, datos_empleados, tipo_licencia, licencias, horas_extras;

create table categoria (idcategoria int auto_increment primary key not null,
categoria_empl varchar(15) not null);

alter table categoria add sueldo_basico int;

create table datos_empleados (idempleado int auto_increment primary key not null,
nombre varchar(15) not null,
apellido varchar(15) not null,
dni int,
fecha_nacimiento date not null,
fecha_ingreso date not null,
fecha_salida date,
categoriaid int not null,
estado_civil ENUM('Soltero', 'Casado', 'Separado') not null,
hijos varchar(5) not null,
direccion varchar(50) not null,
foreign key (categoriaid) references categoria (idcategoria));

create table tipo_licencia (idtipolicencia int auto_increment primary key not null,
tipolicencia varchar(25) not null);

create table licencias (idlicencia int auto_increment primary key not null,
fecha_inicio date not null,
fecha_fin date,
empleadoid int not null,
tipolicenciaid int not null,
foreign key (empleadoid) references datos_empleados (idempleado),
foreign key (tipolicenciaid) references tipo_licencia (idtipolicencia));

create table horas_extras (idhorahextra int auto_increment primary key not null,
fecha date not null,
empleadoid int not null,
compensatoria tinyint not null,
extras tinyint not null,
foreign key (empleadoid) references datos_empleados (idempleado));

insert into categoria (categoria_empl, sueldo_basico) values
('Ayudante', 100000), ('Medio Oficial', 120000), ('Oficial', 150000), ('Mantenimiento', 170000), 
('Supervisor', 200000), ('Jefe', 220000), ('Gerente', 280000); 


insert into tipo_licencia (tipolicencia) values
('Sin Motivo'), ('Enfermedad inclulpable'), ('ART'), ('Paternidad/Maternidad'), ('Vacaciones'), ('Compensatorias');

INSERT INTO datos_empleados (nombre, apellido, dni, direccion, fecha_nacimiento, fecha_ingreso, estado_civil, hijos, categoriaid)
VALUES
    ('Juan', 'García', 33258789, 'San Martin 1235 - Bahía Blanca', '1984-05-22', '2011-06-01', 'Casado', 0, 1),
    ('María', 'López', 28546987, 'Belgrano 987 - Bahía Blanca', '1985-08-10', '2012-02-15', 'Soltero', 2, 3),
    ('Carlos', 'Rodríguez', 39987456, 'San Martín 369 - Bahía Blanca', '1982-03-18', '2010-09-20', 'Separado', 1, 3),
    ('Laura', 'Fernández', 26587456, 'Belgrano 753 - Bahía Blanca', '1986-11-30', '2013-07-10', 'Casado', 3, 4),
    ('Pedro', 'Gómez', 28569745, 'San Martín 852 - Bahía Blanca', '1987-09-25', '2015-05-05', 'Soltero', 0, 5),
    ('Ana', 'Pérez', 37845698, 'Belgrano 456 - Bahía Blanca', '1983-07-12', '2009-12-05', 'Casado', 2, 6),
    ('Luis', 'Sánchez', 42569874, 'San Martín 147 - Bahía Blanca', '1980-06-05', '2008-04-18', 'Separado', 4, 7),
    ('Marcela', 'Torres', 31548796, 'Belgrano 369 - Bahía Blanca', '1989-04-17', '2017-09-30', 'Soltero', 1, 1),
    ('Jorge', 'González', 25789456, 'San Martín 963 - Bahía Blanca', '1981-01-25', '2014-11-20', 'Casado', 0, 2),
    ('Silvia', 'Morales', 39874125, 'Belgrano 654 - Bahía Blanca', '1984-12-08', '2019-03-12', 'Soltero', 3, 4),
    ('Roberto', 'Luna', 31254789, 'San Martín 753 - Bahía Blanca', '1985-10-30', '2016-08-15', 'Casado', 2, 6),
    ('Lucía', 'Cabrera', 28974563, 'Belgrano 258 - Bahía Blanca', '1982-09-17', '2011-10-05', 'Soltero', 0, 7),
    ('Diego', 'Romero', 39856214, 'San Martín 456 - Bahía Blanca', '1983-06-02', '2018-06-25', 'Separado', 4, 3),
    ('Mariana', 'Navarro', 25987436, 'Belgrano 987 - Bahía Blanca', '1987-03-15', '2014-02-10', 'Soltero', 1, 5),
    ('Gustavo', 'Mendoza', 24581369, 'San Martín 369 - Punta Alta', '1980-02-14', '2009-11-18', 'Casado', 2, 2),
    ('Marina', 'Ríos', 38796521, 'Belgrano 753 - Punta Alta', '1986-07-29', '2013-05-05', 'Casado', 0, 7);

insert into licencias (fecha_inicio, fecha_fin, empleadoid, tipolicenciaid) values
('2023-06-02', '2023-06-7', 15, 2),
('2023-06-08', '2023-06-13', 15, 3),
('2023-06-02', '2023-06-7', 14, 2),
('2023-06-08', '2023-06-13', 14, 3),
('2023-06-14', '2023-06-15', 15, 1);

insert into horas_extras (fecha, empleadoid, compensatoria, extras) values
('2023-06-16', 15, 1, 0),
('2023-06-18', 15, 2, 0),
('2023-06-18', 15, 0, 2),
('2023-06-20', 15, 0, 2);

ALTER TABLE categoria MODIFY sueldo_basico float;
ALTER TABLE licencias MODIFY fecha_fin date NOT NULL;