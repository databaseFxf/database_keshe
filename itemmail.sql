--
-- Host: localhost    Database: itemmail
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `celebrate_movies`
--


--
-- Dumping data for table `celebrate_movies`
--

LOCK TABLES `celebrate_movies` WRITE;
/*!40000 ALTER TABLE `celebrate_movies` DISABLE KEYS */;
/*!40000 ALTER TABLE `celebrate_movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `celebrates`
--

DROP TABLE IF EXISTS `celebrates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `celebrates` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `celebrate_name` varchar(20) DEFAULT NULL,
  `celebrate_sex` varchar(5) DEFAULT NULL,
  `celebrate_constellation` varchar(20) DEFAULT NULL,
  `celebrate_birthday` timestamp NULL DEFAULT NULL,
  `celebrate_birthplace` varchar(50) DEFAULT NULL,
  `celebrate_professions` varchar(20) DEFAULT NULL,
  `celebrate_icon_url` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `celebrates_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `celebrates`
--

LOCK TABLES `celebrates` WRITE;
/*!40000 ALTER TABLE `celebrates` DISABLE KEYS */;
/*!40000 ALTER TABLE `celebrates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_sources`
--


--
-- Dumping data for table `movie_sources`
--

LOCK TABLES `movie_sources` WRITE;
/*!40000 ALTER TABLE `movie_sources` DISABLE KEYS */;
/*!40000 ALTER TABLE `movie_sources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `movies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_name` varchar(30) DEFAULT NULL,
  `movie_type` varchar(20) DEFAULT NULL,
  `movie_production` varchar(20) DEFAULT NULL,
  `movie_language` varchar(20) DEFAULT NULL,
  `movie_release_date` varchar(30) DEFAULT NULL,
  `movie_length` varchar(10) DEFAULT NULL,
  `movie_aliases` varchar(100) DEFAULT NULL,
  `IMDB_link` varchar(50) DEFAULT NULL,
  `movie_synopsis` text,
  `movie_poster_url` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `movies_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_comments`
--

DROP TABLE IF EXISTS `user_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `content` text,
  `comment_time` timestamp NULL DEFAULT NULL,
  `tag` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_comments_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_comments`
--

LOCK TABLES `user_comments` WRITE;
/*!40000 ALTER TABLE `user_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_evaluations`
--

DROP TABLE IF EXISTS `user_evaluations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_evaluations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `evaluation_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_evaluations_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_evaluations`
--

LOCK TABLES `user_evaluations` WRITE;
/*!40000 ALTER TABLE `user_evaluations` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_evaluations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--


--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

