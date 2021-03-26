-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Мар 12 2021 г., 02:33
-- Версия сервера: 10.3.13-MariaDB
-- Версия PHP: 7.1.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `carsharing`
--

-- --------------------------------------------------------

--
-- Структура таблицы `carsharing`
--

CREATE TABLE `carsharing` (
  `ID_Client` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Surname` varchar(20) NOT NULL,
  `PhoneNumber` varchar(15) NOT NULL,
  `BirthDate` date NOT NULL,
  `DriverLicenseNumber` varchar(10) NOT NULL,
  `DrivingExperience` int(11) NOT NULL,
  `Status` varchar(50) NOT NULL,
  `Tariff` varchar(15) NOT NULL,
  `DistanceToCar` double DEFAULT NULL,
  `OrderDate` date DEFAULT NULL,
  `TripStartTime` date DEFAULT NULL,
  `TripEndTime` date DEFAULT NULL,
  `CarNumber` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `carsharing`
--
ALTER TABLE `carsharing`
  ADD PRIMARY KEY (`ID_Client`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `carsharing`
--
ALTER TABLE `carsharing`
  MODIFY `ID_Client` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
