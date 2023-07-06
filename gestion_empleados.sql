-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-06-2023 a las 06:07:50
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_empleados`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `idcategoria` int(11) NOT NULL,
  `categoria_empl` varchar(15) NOT NULL,
  `sueldo_basico` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`idcategoria`, `categoria_empl`, `sueldo_basico`) VALUES
(1, 'Ayudante', 100000),
(2, 'Medio Oficial', 120000),
(3, 'Oficial', 150000),
(4, 'Mantenimiento', 170000),
(5, 'Supervisor', 200000),
(6, 'Jefe', 220000),
(7, 'Gerente', 280000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_empleados`
--

CREATE TABLE `datos_empleados` (
  `idempleado` int(11) NOT NULL,
  `nombre` varchar(15) NOT NULL,
  `apellido` varchar(15) NOT NULL,
  `dni` int(11) DEFAULT NULL,
  `fecha_nacimiento` date NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `fecha_salida` date DEFAULT NULL,
  `categoriaid` int(11) NOT NULL,
  `estado_civil` enum('Soltero','Casado','Separado') NOT NULL,
  `hijos` varchar(5) NOT NULL,
  `direccion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `datos_empleados`
--

INSERT INTO `datos_empleados` (`idempleado`, `nombre`, `apellido`, `dni`, `fecha_nacimiento`, `fecha_ingreso`, `fecha_salida`, `categoriaid`, `estado_civil`, `hijos`, `direccion`) VALUES
(1, 'Juan', 'García', 33258789, '1984-05-22', '2011-06-01', NULL, 1, 'Casado', '0', 'San Martin 1235 - Bahía Blanca'),
(2, 'María', 'López', 28546987, '1985-08-10', '2012-02-15', NULL, 3, 'Soltero', '2', 'Belgrano 987 - Bahía Blanca'),
(3, 'Carlos', 'Rodríguez', 39987456, '1982-03-18', '2010-09-20', NULL, 3, 'Separado', '1', 'San Martín 369 - Bahía Blanca'),
(4, 'Laura', 'Fernández', 26587456, '1986-11-30', '2013-07-10', NULL, 4, 'Casado', '3', 'Belgrano 753 - Bahía Blanca'),
(5, 'Pedro', 'Gómez', 28569745, '1987-09-25', '2015-05-05', NULL, 5, 'Soltero', '0', 'San Martín 852 - Bahía Blanca'),
(6, 'Ana', 'Pérez', 37845698, '1983-07-12', '2009-12-05', NULL, 6, 'Casado', '2', 'Belgrano 456 - Bahía Blanca'),
(7, 'Luis', 'Sánchez', 42569874, '1980-06-05', '2008-04-18', NULL, 7, 'Separado', '4', 'San Martín 147 - Bahía Blanca'),
(8, 'Marcela', 'Torres', 31548796, '1989-04-17', '2017-09-30', NULL, 1, 'Soltero', '1', 'Belgrano 369 - Bahía Blanca'),
(9, 'Jorge', 'González', 25789456, '1981-01-25', '2014-11-20', NULL, 2, 'Casado', '0', 'San Martín 963 - Bahía Blanca'),
(10, 'Silvia', 'Morales', 39874125, '1984-12-08', '2019-03-12', NULL, 4, 'Soltero', '3', 'Belgrano 654 - Bahía Blanca'),
(11, 'Roberto', 'Luna', 31254789, '1985-10-30', '2016-08-15', NULL, 6, 'Casado', '2', 'San Martín 753 - Bahía Blanca'),
(12, 'Lucía', 'Cabrera', 28974563, '1982-09-17', '2011-10-05', NULL, 7, 'Soltero', '0', 'Belgrano 258 - Bahía Blanca'),
(13, 'Diego', 'Romero', 39856214, '1983-06-02', '2018-06-25', NULL, 3, 'Separado', '4', 'San Martín 456 - Bahía Blanca'),
(14, 'Mariana', 'Navarro', 25987436, '1987-03-15', '2014-02-10', NULL, 5, 'Soltero', '1', 'Belgrano 987 - Bahía Blanca'),
(15, 'Gustavo', 'Mendoza', 24581369, '1980-02-14', '2009-11-18', NULL, 2, 'Casado', '2', 'San Martín 369 - Punta Alta'),
(16, 'Marina', 'Ríos', 38796521, '1986-07-29', '2013-05-05', NULL, 7, 'Casado', '0', 'Belgrano 753 - Punta Alta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horas_extras`
--

CREATE TABLE `horas_extras` (
  `idhorahextra` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `empleadoid` int(11) NOT NULL,
  `compensatoria` tinyint(4) NOT NULL,
  `extras` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `horas_extras`
--

INSERT INTO `horas_extras` (`idhorahextra`, `fecha`, `empleadoid`, `compensatoria`, `extras`) VALUES
(1, '2023-06-16', 15, 1, 0),
(2, '2023-06-18', 15, 2, 0),
(3, '2023-06-18', 15, 0, 2),
(4, '2023-06-20', 15, 0, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `licencias`
--

CREATE TABLE `licencias` (
  `idlicencia` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `empleadoid` int(11) NOT NULL,
  `tipolicenciaid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `licencias`
--

INSERT INTO `licencias` (`idlicencia`, `fecha_inicio`, `fecha_fin`, `empleadoid`, `tipolicenciaid`) VALUES
(1, '2023-06-02', '2023-06-07', 15, 2),
(2, '2023-06-08', '2023-06-13', 15, 3),
(3, '2023-06-02', '2023-06-07', 14, 2),
(4, '2023-06-08', '2023-06-13', 14, 3),
(5, '2023-06-14', '2023-06-15', 15, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_licencia`
--

CREATE TABLE `tipo_licencia` (
  `idtipolicencia` int(11) NOT NULL,
  `tipolicencia` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `tipo_licencia`
--

INSERT INTO `tipo_licencia` (`idtipolicencia`, `tipolicencia`) VALUES
(1, 'Sin Motivo'),
(2, 'Enfermedad inclulpable'),
(3, 'ART'),
(4, 'Paternidad/Maternidad'),
(5, 'Vacaciones'),
(6, 'Compensatorias');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`idcategoria`);

--
-- Indices de la tabla `datos_empleados`
--
ALTER TABLE `datos_empleados`
  ADD PRIMARY KEY (`idempleado`),
  ADD KEY `categoriaid` (`categoriaid`);

--
-- Indices de la tabla `horas_extras`
--
ALTER TABLE `horas_extras`
  ADD PRIMARY KEY (`idhorahextra`),
  ADD KEY `empleadoid` (`empleadoid`);

--
-- Indices de la tabla `licencias`
--
ALTER TABLE `licencias`
  ADD PRIMARY KEY (`idlicencia`),
  ADD KEY `empleadoid` (`empleadoid`),
  ADD KEY `tipolicenciaid` (`tipolicenciaid`);

--
-- Indices de la tabla `tipo_licencia`
--
ALTER TABLE `tipo_licencia`
  ADD PRIMARY KEY (`idtipolicencia`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `idcategoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `datos_empleados`
--
ALTER TABLE `datos_empleados`
  MODIFY `idempleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `horas_extras`
--
ALTER TABLE `horas_extras`
  MODIFY `idhorahextra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `licencias`
--
ALTER TABLE `licencias`
  MODIFY `idlicencia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tipo_licencia`
--
ALTER TABLE `tipo_licencia`
  MODIFY `idtipolicencia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `datos_empleados`
--
ALTER TABLE `datos_empleados`
  ADD CONSTRAINT `datos_empleados_ibfk_1` FOREIGN KEY (`categoriaid`) REFERENCES `categoria` (`idcategoria`);

--
-- Filtros para la tabla `horas_extras`
--
ALTER TABLE `horas_extras`
  ADD CONSTRAINT `horas_extras_ibfk_1` FOREIGN KEY (`empleadoid`) REFERENCES `datos_empleados` (`idempleado`);

--
-- Filtros para la tabla `licencias`
--
ALTER TABLE `licencias`
  ADD CONSTRAINT `licencias_ibfk_1` FOREIGN KEY (`empleadoid`) REFERENCES `datos_empleados` (`idempleado`),
  ADD CONSTRAINT `licencias_ibfk_2` FOREIGN KEY (`tipolicenciaid`) REFERENCES `tipo_licencia` (`idtipolicencia`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
