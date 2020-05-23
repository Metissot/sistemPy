-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-05-2020 a las 18:17:14
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `muni`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `oficios`
--

CREATE TABLE `oficios` (
  `ID_OFICIO` int(11) NOT NULL,
  `FECHA_ING_OF` date NOT NULL,
  `JUZ_N_OF` int(11) NOT NULL,
  `N_ACTA_OF` varchar(11) NOT NULL,
  `N_CAUSA_OF` varchar(11) NOT NULL,
  `FECHA_RES_OF` date NOT NULL,
  `N_RESOL_OF` varchar(11) NOT NULL,
  `DNI_PER_OF` int(40) NOT NULL,
  `FECHA_INHA_OF` date NOT NULL,
  `FECHA_FIN_IN_OF` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `oficios`
--

INSERT INTO `oficios` (`ID_OFICIO`, `FECHA_ING_OF`, `JUZ_N_OF`, `N_ACTA_OF`, `N_CAUSA_OF`, `FECHA_RES_OF`, `N_RESOL_OF`, `DNI_PER_OF`, `FECHA_INHA_OF`, `FECHA_FIN_IN_OF`) VALUES
(1331, '2020-03-16', 1, 'D127696', '2262', '2020-03-11', '13822020', 25511185, '2020-03-16', '2020-06-16'),
(1332, '2020-03-05', 2, '132', '3212', '2020-03-05', '32132', 14258369, '2020-03-05', '2020-03-05'),
(1333, '2020-03-05', 2, '21231', '1321', '2020-03-05', '3213212020', 14258369, '2020-03-05', '2020-03-05'),
(1334, '2020-06-04', 2, '213213', '321321', '2020-06-04', '32132', 25147369, '2020-06-04', '2020-06-04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `DNI_PER` int(40) NOT NULL,
  `APE_PER` varchar(50) NOT NULL,
  `NOM_PER` varchar(50) NOT NULL,
  `N_LICPER` int(40) NOT NULL,
  `DOMI_PER` varchar(60) DEFAULT NULL,
  `CON_PER` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`DNI_PER`, `APE_PER`, `NOM_PER`, `N_LICPER`, `DOMI_PER`, `CON_PER`) VALUES
(252123, 'LOPEZ', 'JULIO', 0, NULL, ''),
(14258369, 'DELGADO', 'MARCOS DIONISIO', 14258369, NULL, ''),
(25147369, 'TOLEDO', 'PABLO RODRIGO', 25147369, NULL, ''),
(25511185, 'SACAYAN', 'DIEGO ALBERTO', 25511185, NULL, ''),
(36258147, 'LEGUIZAMON', 'HERMES ', 36258147, NULL, ''),
(39013931, 'TISSOT', 'MAURICIO', 0, NULL, ''),
(145654321, 'LALO', 'LANDA', 145432132, NULL, '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `oficios`
--
ALTER TABLE `oficios`
  ADD PRIMARY KEY (`ID_OFICIO`),
  ADD KEY `FK_DNI_PER` (`DNI_PER_OF`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`DNI_PER`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `oficios`
--
ALTER TABLE `oficios`
  MODIFY `ID_OFICIO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1335;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `oficios`
--
ALTER TABLE `oficios`
  ADD CONSTRAINT `PER-OFICIO` FOREIGN KEY (`DNI_PER_OF`) REFERENCES `personas` (`DNI_PER`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
