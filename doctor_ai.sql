-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 15, 2023 at 10:55 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `doctor_ai`
--

-- --------------------------------------------------------

--
-- Table structure for table `results`
--

CREATE TABLE `results` (
  `id` int(33) NOT NULL,
  `query` varchar(99) NOT NULL,
  `result` longblob NOT NULL,
  `user_id` int(33) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `results`
--

INSERT INTO `results` (`id`, `query`, `result`, `user_id`) VALUES
(33, 'asd', 0x646e61746f726e612f73657175656e63655f6d6f6469666965642e6661737461, 22),
(33, 'asd', 0x646e61746f726e612f73657175656e63655f6d6f6469666965642e6661737461, 22),
(33, 'asd', 0x646e61746f726e612f73657175656e63655f6d6f6469666965642e6661737461, 2),
(2968524, 'dna_to_rna', 0x646e61746f726e612f73657175656e63655f6d6f6469666965642e6661737461, 2),
(9542264, 'dnaprotein', 0x646e6170726f7465696e2f73657175656e63655f70726f7465696e2e6661737461, 2),
(5082945, 'dna_to_rna', 0x646e61746f726e612f73657175656e63655f6d6f6469666965642e6661737461, 3);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `role_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `role_name`) VALUES
(1, 'admin'),
(2, 'doctor'),
(3, 'user');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pass_hash` varchar(255) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `name`, `surname`, `email`, `pass_hash`, `role_id`) VALUES
(1, 'cardenet', 'Luis', 'Cardenete', 'carde602@gmail.com', '1234', 1),
(2, 'arnau', 'Arnau', 'Albert', 'arnau@gmail.com', '1234', 1),
(3, 'alex', 'Alex', 'Varela', 'alex@gmail.com', '1234', 1),
(4, 'victor', 'Victor', 'Piñana', 'victor@gmail.com', '1234', 1),
(5, 'jdoe', 'John', 'Doe', 'jdoe@example.com', '12', 2),
(6, 'aaren', 'Aaren', 'Montaña', 'Aaren@example.com', '12', 2),
(7, 'Agnetha', 'Agnetha', 'Santo', 'Agnetha@example.com', '12', 2),
(8, 'Algot', 'Algot', 'Noble', 'Algot@example.com', '12', 3),
(9, 'Alrik', 'Alrik', 'Ann', 'Alrik@example.com', '12', 2),
(10, 'Anneke', 'Anneke', 'Little', 'Anneke@example.com', '12', 3),
(11, 'Argus', 'Argus', 'Vigilante', 'Argus@example.com', '12', 3),
(12, 'Asbjorn', 'Asbjorn', 'Oso', 'Asbjorn@example.com', '12', 3),
(13, 'pep', 'aaaa', 'aaa', 'aaa@asdsda', '1234', 1),
(14, 'asdfxcvxzcv', 'nasdasasdfafddame', 'surname', 'email', 'pass', 1),
(15, 'asdasdasdasdasdasdas', 'asdasdasdasdasdasdas', 'surname', 'email', 'pass', 1),
(16, 'ola', 'ola', 'ola', 'ola', 'ola', 1),
(17, 'asd', 'asd', 'asd', 'asd', 'asd', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `fk_users_role` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_role` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
