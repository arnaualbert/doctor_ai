-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 19, 2023 at 03:23 PM
-- Server version: 8.0.32-0ubuntu0.22.04.2
-- PHP Version: 8.1.2-1ubuntu2.11

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
  `id` int NOT NULL,
  `query` varchar(99) COLLATE utf8mb4_general_ci NOT NULL,
  `result` longblob NOT NULL,
  `user_id` int NOT NULL,
  `date` varchar(99) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `results`
--

INSERT INTO `results` (`id`, `query`, `result`, `user_id`, `date`) VALUES
(65697, 'random_sequence', 0x646e61363536393772616e646f6d2e6661737461, 2, '2023-04-15 16:39:22.832290'),
(2448647, 'random_sequence', 0x646e613234343836343772616e646f6d2e6661737461, 2, '2023-04-15 16:40:06.274423'),
(5798422, 'dnaprotein', 0x646e6170726f7465696e2f646e613234343836343772616e646f6d5f70726f7465696e2e6661737461, 2, '2023-04-15 16:42:13.298916'),
(1540105, 'dna_to_rna', 0x646e61746f726e612f646e61363536393772616e646f6d202832295f6d6f6469666965642e6661737461, 2, '2023-04-15 16:42:34.283574'),
(7498121, 'dnaprotein', 0x646e6170726f7465696e2f646e613234343836343772616e646f6d373439383132315f70726f7465696e2e6661737461, 2, '2023-04-15 16:47:03.436021'),
(5344444, 'dnaprotein', 0x646e6170726f7465696e2f646e613234343836343772616e646f6d5f70726f7465696e2e6661737461, 2, '2023-04-15 16:50:38.783486'),
(5258968, 'dnaprotein', 0x646e6170726f7465696e2f646e613234343836343772616e646f6d5f6161616170726f7465696e2e6661737461, 2, '2023-04-15 16:52:07.980075'),
(3610479, 'dnaprotein', 0x646e6170726f7465696e2f2f686f6d652f61726e6175616c626572742f4465736b746f702f646f63746f725f61692f646e6170726f7465696e2f646e61363536393772616e646f6d20283129333631303437395f70726f7465696e2e6661737461, 2, '2023-04-15 16:53:09.633606'),
(2973312, 'dnaprotein', 0x646e6170726f7465696e2f2f686f6d652f61726e6175616c626572742f4465736b746f702f646f63746f725f61692f646e6170726f7465696e2f646e61363536393772616e646f6d20283129323937333331325f70726f7465696e2e6661737461, 2, '2023-04-15 16:53:52.616387'),
(1322977, 'dna_to_rna', 0x646e61746f726e612f646e613234343836343772616e646f6d5f6d6f6469666965642e6661737461, 2, '2023-04-15 17:00:40.956078'),
(3226676, 'dna_to_rna', 0x646e61746f726e612f33323236363736646e613234343836343772616e646f6d5f6d6f6469666965642e6661737461, 2, '2023-04-15 17:02:13.024536'),
(4006175, 'extract_cds', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 17:04:25.711720'),
(3656970, 'dnaprotein', 0x646e6170726f7465696e2f33363536393730646e613234343836343772616e646f6d5f70726f7465696e2e6661737461, 2, '2023-04-15 17:07:29.185035'),
(8061633, 'dnaprotein', 0x646e6170726f7465696e2f38303631363333646e61363536393772616e646f6d202832295f70726f7465696e2e6661737461, 2, '2023-04-15 17:07:43.704344'),
(3742481, 'local_alignment', 0x616c69676e6d656e745f726573756c7433373432343831616c69676e6d656e745f726573756c742e747874, 2, '2023-04-15 17:35:53.715801'),
(79674, 'random_sequence', 0x646e61373936373472616e646f6d2e6661737461, 2, '2023-04-15 17:36:06.320093'),
(5982552, 'local_alignment', 0x616c69676e6d656e745f726573756c7435393832353532616c69676e6d656e745f726573756c742e747874, 2, '2023-04-15 17:36:14.133839'),
(5820740, 'random_sequence', 0x646e613538323037343072616e646f6d2e6661737461, 2, '2023-04-15 17:43:25.256630'),
(4042193, 'random_sequence', 0x646e613430343231393372616e646f6d2e6661737461, 2, '2023-04-15 17:43:26.416299'),
(7187069, 'local_alignment', 0x616c69676e6d656e745f726573756c7437313837303639616c69676e6d656e745f726573756c742e747874, 2, '2023-04-15 17:45:39.934385'),
(9707387, 'random_sequence', 0x646e613937303733383772616e646f6d2e6661737461, 2, '2023-04-15 17:50:40.179155'),
(9065175, 'random_sequence', 0x646e613930363531373572616e646f6d2e6661737461, 2, '2023-04-15 17:50:43.888763'),
(759222, 'random_sequence', 0x646e6137353932323272616e646f6d2e6661737461, 2, '2023-04-15 17:53:01.331347'),
(7439626, 'random_sequence', 0x646e613734333936323672616e646f6d2e6661737461, 2, '2023-04-15 17:53:06.441193'),
(9705500, 'extract_cds', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 18:11:22.532324'),
(1072090, 'extract_cds', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 18:11:32.201679'),
(521774, 'cds_extract', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 18:14:31.744412'),
(1012593, 'cds_extract', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 18:15:59.715869'),
(7705789, 'cds_extract', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 18:16:42.824250'),
(9027903, 'cds_extract', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 18:17:47.621244'),
(3887124, 'cds_extract', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 18:19:28.746062'),
(1951552, 'cds_extract', 0x726573756c7461646f2e6661737461, 2, '2023-04-15 18:23:09.219031'),
(7513569, 'cds_extract', 0x37353133353639726573756c7461646f2e747874, 2, '2023-04-15 18:23:58.476337'),
(6727187, 'random_sequence', 0x646e613637323731383772616e646f6d2e6661737461, 3, '2023-04-15 18:25:57.535083'),
(8427633, 'dna_to_rna', 0x646e61746f726e612f38343237363333646e613637323731383772616e646f6d5f6d6f6469666965642e6661737461, 3, '2023-04-15 18:26:06.170167'),
(4092643, 'gb_to_fasta', 0x67623266617374612f3430393236343373657175656e63652e6661737461, 2, '2023-04-15 19:17:38.872942'),
(7360907, 'gb2fasta', 0x73657175656e63652e6661737461, 2, '2023-04-15 19:19:42.668908'),
(7557227, 'gb_to_fasta', 0x3735353732323767625f746f5f66617374612e6661737461, 2, '2023-04-15 19:30:03.540297'),
(1136308, 'gb_to_fasta', 0x3131333633303867625f746f5f66617374612e6661737461, 2, '2023-04-15 19:31:37.137350'),
(3175934, 'random_sequence', 0x646e613331373539333472616e646f6d2e6661737461, 2, '2023-04-16 09:18:11.572784'),
(4318344, 'cds_extract', 0x34333138333434726573756c7461646f2e747874, 3, '2023-04-16 09:31:38.290495'),
(3114931, 'random_sequence', 0x646e613331313439333172616e646f6d2e6661737461, 3, '2023-04-16 09:35:15.348705'),
(3488700, 'random_sequence', 0x646e613334383837303072616e646f6d2e6661737461, 3, '2023-04-16 09:35:37.153812'),
(1354882, 'local_alignment', 0x616c69676e6d656e745f726573756c7431333534383832616c69676e6d656e745f726573756c742e747874, 3, '2023-04-16 09:35:51.221212'),
(4993858, 'random_sequence', 0x646e613439393338353872616e646f6d2e6661737461, 3, '2023-04-16 09:36:27.233696'),
(9606057, 'random_sequence', 0x646e613936303630353772616e646f6d2e6661737461, 3, '2023-04-16 09:36:32.545266'),
(172659, 'local_alignment', 0x616c69676e6d656e745f726573756c74313732363539616c69676e6d656e745f726573756c742e747874, 3, '2023-04-16 09:37:17.109833'),
(5034319, 'random_sequence', 0x646e613530333433313972616e646f6d2e6661737461, 3, '2023-04-16 09:37:30.244449'),
(3606173, 'local_alignment', 0x616c69676e6d656e745f726573756c7433363036313733616c69676e6d656e745f726573756c742e747874, 3, '2023-04-16 09:37:40.658208'),
(523012, 'gb_to_fasta', 0x35323330313267625f746f5f66617374612e6661737461, 3, '2023-04-16 09:37:59.173573'),
(3861306, 'random_sequence', 0x646e613338363133303672616e646f6d2e6661737461, 2, '2023-04-17 17:24:02.458912'),
(5577811, 'random_sequence', 0x646e613535373738313172616e646f6d2e6661737461, 2, '2023-04-17 17:24:19.804412'),
(7145225, 'random_sequence', 0x646e613731343532323572616e646f6d2e6661737461, 2, '2023-04-17 17:24:23.868345'),
(9344305, 'random_sequence', 0x646e613933343433303572616e646f6d2e6661737461, 2, '2023-04-17 17:24:40.561087'),
(3240382, 'random_sequence', 0x646e613332343033383272616e646f6d2e6661737461, 2, '2023-04-17 17:25:51.995952'),
(7610976, 'random_sequence', 0x646e613736313039373672616e646f6d2e6661737461, 2, '2023-04-17 17:26:58.115291'),
(4444784, 'random_sequence', 0x646e613434343437383472616e646f6d2e6661737461, 2, '2023-04-17 17:28:35.693486'),
(6290687, 'random_sequence', 0x646e613632393036383772616e646f6d2e6661737461, 3, '2023-04-18 13:53:24.252289'),
(6838812, 'random_sequence', 0x646e613638333838313272616e646f6d2e6661737461, 3, '2023-04-18 13:53:49.855344'),
(5665007, 'random_sequence', 0x646e613536363530303772616e646f6d2e6661737461, 3, '2023-04-18 13:54:20.312222'),
(160582, 'random_sequence', 0x646e6131363035383272616e646f6d2e6661737461, 3, '2023-04-18 13:55:11.919575'),
(2289438, 'random_sequence', 0x646e613232383934333872616e646f6d2e6661737461, 3, '2023-04-18 13:56:03.262004'),
(9075613, 'random_sequence', 0x646e613930373536313372616e646f6d2e6661737461, 2, '2023-04-18 14:02:35.068947'),
(8442927, 'local_alignment', 0x616c69676e6d656e745f726573756c7438343432393237616c69676e6d656e745f726573756c742e747874, 3, '2023-04-18 15:07:50.454212'),
(6339269, 'random_sequence', 0x646e613633333932363972616e646f6d2e6661737461, 2, '2023-04-18 15:40:54.633147'),
(1180589, 'random_sequence', 0x646e613131383035383972616e646f6d2e6661737461, 2, '2023-04-18 15:41:04.174810'),
(3969156, 'random_sequence', 0x646e613339363931353672616e646f6d2e6661737461, 2, '2023-04-18 16:04:53.460687'),
(7507904, 'random_sequence', 0x646e613735303739303472616e646f6d2e6661737461, 1, '2023-04-18 16:06:29.744147'),
(9434714, 'random_sequence', 0x646e613934333437313472616e646f6d2e6661737461, 2, '2023-04-18 16:07:48.464080'),
(2876293, 'random_sequence', 0x646e613238373632393372616e646f6d2e6661737461, 2, '2023-04-18 16:08:02.599167'),
(9270884, 'random_sequence', 0x646e613932373038383472616e646f6d2e6661737461, 2, '2023-04-18 16:08:51.288963'),
(5451602, 'random_sequence', 0x646e613534353136303272616e646f6d2e6661737461, 2, '2023-04-18 16:08:54.409830'),
(7639850, 'random_sequence', 0x646e613736333938353072616e646f6d2e6661737461, 2, '2023-04-18 16:09:23.008040'),
(3939978, 'random_sequence', 0x646e613339333939373872616e646f6d2e6661737461, 2, '2023-04-18 16:09:24.485210'),
(4187739, 'local_alignment', 0x616c69676e6d656e745f726573756c7434313837373339616c69676e6d656e745f726573756c742e747874, 2, '2023-04-18 16:09:33.347823'),
(508040, 'local_alignment', 0x616c69676e6d656e745f726573756c74353038303430616c69676e6d656e745f726573756c742e747874, 2, '2023-04-18 16:10:19.841840'),
(3043133, 'local_alignment', 0x616c69676e6d656e745f726573756c7433303433313333616c69676e6d656e745f726573756c742e747874, 2, '2023-04-18 16:10:45.849008'),
(6551629, 'cds_extract', 0x36353531363239726573756c7461646f2e747874, 2, '2023-04-18 16:12:31.530358'),
(5229736, 'dnaprotein', 0x646e6170726f7465696e2f35323239373336616c69676e6d656e745f726573756c7434313837373339616c69676e6d656e745f726573756c742e747874, 2, '2023-04-18 16:15:47.440381'),
(3537697, 'dnaprotein', 0x646e6170726f7465696e2f3335333736393773657175656e6365202834292e6762, 2, '2023-04-18 16:16:06.480835'),
(5969525, 'dnaprotein', 0x646e6170726f7465696e2f35393639353235646e613238373632393372616e646f6d5f70726f7465696e2e6661737461, 2, '2023-04-18 16:17:09.202395');

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int NOT NULL,
  `role_name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL
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
  `id` int NOT NULL,
  `username` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `surname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `pass_hash` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `role_id` int NOT NULL
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
(18, 'fsadf', 'Arnau', 'sadfdf', 'sdf@asd.com', 'asdfsdafsdf', 1);

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

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