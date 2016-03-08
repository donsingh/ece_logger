-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 08, 2016 at 09:26 AM
-- Server version: 5.5.47-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `node_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `single_phase`
--

CREATE TABLE IF NOT EXISTS `single_phase` (
  `indx` int(11) NOT NULL AUTO_INCREMENT,
  `node` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `vrms` double(15,4) NOT NULL,
  `irms` double(15,4) NOT NULL,
  `freq` double(15,4) NOT NULL,
  `pwrf` double(15,4) NOT NULL,
  `actp` double(15,4) NOT NULL,
  `reap` double(15,4) NOT NULL,
  `appp` double(15,4) NOT NULL,
  PRIMARY KEY (`indx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `three_phase`
--

CREATE TABLE IF NOT EXISTS `three_phase` (
  `indx` int(11) NOT NULL AUTO_INCREMENT,
  `node` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `vrms1` double(15,4) NOT NULL,
  `irms1` double(15,4) NOT NULL,
  `actp1` double(15,4) NOT NULL,
  `vrms2` double(15,4) NOT NULL,
  `irms2` double(15,4) NOT NULL,
  `actp2` double(15,4) NOT NULL,
  `actpt` double(15,4) NOT NULL,
  PRIMARY KEY (`indx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
