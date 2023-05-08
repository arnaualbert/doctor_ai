-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 08, 2023 at 05:49 PM
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
  `id` int(11) NOT NULL,
  `query` varchar(99) NOT NULL,
  `result` longblob DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `start` varchar(99) DEFAULT NULL,
  `date` varchar(99) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `results`
--

INSERT INTO `results` (`id`, `query`, `result`, `user_id`, `start`, `date`) VALUES
(532459, 'local_alignment', 0x616c69676e6d656e745f726573756c74353332343539616c69676e6d656e745f726573756c742e747874, 2, '2023-05-06 20:18:31.018143+02:00', '2023-05-06 20:18:53.713311+02:00'),
(8928092, 'random_sequence', 0x646e613839323830393272616e646f6d2e6661737461, 2, '2023-05-06 20:18:35.608684+02:00', '2023-05-06 20:18:35.625053+02:00'),
(3937054, 'random_sequence', 0x646e613339333730353472616e646f6d2e6661737461, 2, '2023-05-08 15:44:29.837041+02:00', '2023-05-08 15:44:29.850286+02:00'),
(2724808, 'gb_to_fasta', 0x3237323438303867625f746f5f66617374612e6661737461, 2, '2023-05-08 17:38:49.849520+02:00', '2023-05-08 17:38:49.874151+02:00'),
(5693525, 'gb_to_fasta', 0x3536393335323567625f746f5f66617374612e6661737461, 2, '2023-05-08 17:39:30.210228+02:00', '2023-05-08 17:39:30.217754+02:00'),
(3493382, 'reverse_complementary', 0x33343933333832726576657273655f636f6d706c656d656e746172792e6661737461, 2, '2023-05-08 17:42:20.234444+02:00', '2023-05-08 17:42:20.242862+02:00');

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
(1, 'cardenet', 'Luis', 'Cardenete', 'carde602@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(2, 'arnau', 'Arnau', 'Albert', 'arnau@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(3, 'alex', 'Alex', 'Varela', 'alex@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(4, 'victor', 'Victor', 'Piñana', 'victor@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(5, 'jdoe', 'John', 'Doe', 'jdoe@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2),
(6, 'aaren', 'Aaren', 'Montaña', 'Aaren@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2),
(7, 'Agnetha', 'Agnetha', 'Santo', 'Agnetha@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2),
(8, 'Algot', 'Algot', 'Noble', 'Algot@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 3),
(9, 'Alrik', 'Alrik', 'Ann', 'Alrik@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2),
(10, 'Anneke', 'Anneke', 'Little', 'Anneke@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 3),
(11, 'Argus', 'Argus', 'Vigilante', 'Argus@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 3),
(12, 'Asbjorn', 'Asbjorn', 'Oso', 'Asbjorn@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 3),
(13, 'pep', 'aaaa', 'aaa', 'aaa@asdsda', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(14, 'asdfxcvxzcv', 'nasdasasdfafddame', 'surname', 'email', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(15, 'asdasdasdasdasdasdas', 'asdasdasdasdasdasdas', 'surname', 'email', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(16, 'ola', 'ola', 'ola', 'ola', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(17, 'asd', 'asd', 'asd', 'asd', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(18, 'fsadf', 'Arnau', 'sadfdf', 'sdf@asd.com', 'asdfsdafsdf', 1),
(19, 'zxc', 'asd', 'qew', 'asd@asd.com', '2aa696f49b3e47765a7df8f15fa45a40d9ae7d21b21b6630431bc8594e5ae5d6', 3);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

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
