/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP TABLE IF EXISTS `pet_user`;
CREATE TABLE `pet_user` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `pet_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `pet_vet`;
CREATE TABLE `pet_vet` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `vet_id` int DEFAULT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `time_id` time DEFAULT NULL,
  `date` date DEFAULT NULL,
  `pet_id` int DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `pets`;
CREATE TABLE `pets` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `breed` varchar(255) DEFAULT NULL,
  `species` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `sterilized` tinyint(1) DEFAULT NULL,
  `microchip` int DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `year_of_birth` int DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `types`;
CREATE TABLE `types` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(255) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `vets`;
CREATE TABLE `vets` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `type_id` int DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `pet_user` (`id`, `pet_id`, `user_id`) VALUES
(1, 1, 1);
INSERT INTO `pet_user` (`id`, `pet_id`, `user_id`) VALUES
(2, 1, 2);
INSERT INTO `pet_user` (`id`, `pet_id`, `user_id`) VALUES
(3, 2, 3);

INSERT INTO `pet_vet` (`id`, `user_id`, `vet_id`, `notes`, `time_id`, `date`, `pet_id`) VALUES
(1, 1, 1, NULL, '09:00:00', '2024-05-23', 1);
INSERT INTO `pet_vet` (`id`, `user_id`, `vet_id`, `notes`, `time_id`, `date`, `pet_id`) VALUES
(2, 1, 1, NULL, '09:30:00', '2024-05-23', 2);
INSERT INTO `pet_vet` (`id`, `user_id`, `vet_id`, `notes`, `time_id`, `date`, `pet_id`) VALUES
(3, 2, 3, NULL, '15:00:00', '2024-05-24', 3);

INSERT INTO `pets` (`id`, `breed`, `species`, `name`, `sterilized`, `microchip`, `gender`, `year_of_birth`) VALUES
(1, 'Labrador Retriever', 'Dog', 'Buddy', 1, 1234567890, 'M', 2020);
INSERT INTO `pets` (`id`, `breed`, `species`, `name`, `sterilized`, `microchip`, `gender`, `year_of_birth`) VALUES
(2, 'Persian', 'Cat', 'Luna', 0, 0, 'F', 2019);
INSERT INTO `pets` (`id`, `breed`, `species`, `name`, `sterilized`, `microchip`, `gender`, `year_of_birth`) VALUES
(3, 'Leopard Gecko', 'Reptile', 'Leo', 0, 0, 'U', 2022);

INSERT INTO `types` (`id`, `type`) VALUES
(1, 'household');
INSERT INTO `types` (`id`, `type`) VALUES
(2, 'reptiles');
INSERT INTO `types` (`id`, `type`) VALUES
(3, 'farm');
INSERT INTO `types` (`id`, `type`) VALUES
(4, 'Aquatic'),
(5, 'Rodents'),
(6, 'Exotic'),
(7, 'Zoo');

INSERT INTO `users` (`id`, `name`, `last_name`, `password`, `email`) VALUES
(1, 'John', 'Doe', 'password123', 'john.doe@example.com');
INSERT INTO `users` (`id`, `name`, `last_name`, `password`, `email`) VALUES
(2, 'Jane', 'Smith', 'securepassword', 'jane.smith@example.com');
INSERT INTO `users` (`id`, `name`, `last_name`, `password`, `email`) VALUES
(3, 'pakawi', 'park', 'zoopassword', 'pakawi@example.com');

INSERT INTO `vets` (`id`, `name`, `description`, `location`, `email`, `type_id`) VALUES
(1, 'Happy Pets Clinic', 'Friendly and experienced vet care', '123 Main St', 'info@happypets.com', 1);
INSERT INTO `vets` (`id`, `name`, `description`, `location`, `email`, `type_id`) VALUES
(2, 'Exotic Animal Hospital', 'Specializing in exotic pet care', '456 Elm St', 'exoticpets@hospital.com', 6);
INSERT INTO `vets` (`id`, `name`, `description`, `location`, `email`, `type_id`) VALUES
(3, 'Reptile Specialists Clinic', 'Experienced care for all your reptile friends', '555 Elm St', 'reptilespecialists@vetcare.com', 2);


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;