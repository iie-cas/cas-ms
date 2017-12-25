-- MySQL dump 10.13  Distrib 5.7.20, for Win64 (x86_64)
--
-- Host: localhost    Database: score
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `account` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `is_super` tinyint(4) DEFAULT '0',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'chenliwei','chenliwei123','陈李维',1,'2017-12-07 02:51:33'),(2,'chenliwei','chenliwei123','陈李维',1,'2017-12-07 03:24:49');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fundlog`
--

DROP TABLE IF EXISTS `fundlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fundlog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `value` int(11) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `fundlog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fundlog`
--

LOCK TABLES `fundlog` WRITE;
/*!40000 ALTER TABLE `fundlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `fundlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score_label`
--

DROP TABLE IF EXISTS `score_label`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `score_label` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score_label`
--

LOCK TABLES `score_label` WRITE;
/*!40000 ALTER TABLE `score_label` DISABLE KEYS */;
INSERT INTO `score_label` VALUES (1,'调研报告'),(2,'发表论文'),(3,'开发工具'),(4,'调研报告');
/*!40000 ALTER TABLE `score_label` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scorelog`
--

DROP TABLE IF EXISTS `scorelog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scorelog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `value` int(11) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `scorelog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scorelog`
--

LOCK TABLES `scorelog` WRITE;
/*!40000 ALTER TABLE `scorelog` DISABLE KEYS */;
/*!40000 ALTER TABLE `scorelog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `account` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `education` varchar(100) NOT NULL,
  `grade` varchar(100) NOT NULL,
  `score` int(11) DEFAULT '0',
  `fund` int(11) DEFAULT '0',
  `telephone` varchar(100) DEFAULT NULL,
  `qq` varchar(100) DEFAULT NULL,
  `adm_time` varchar(100) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'ylhao','123456','衣龙浩','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(2,'xiaohua','123456','肖华','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(3,'shecairui','123456','佘才睿','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(4,'gaoyuhan','123456','高语晗','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(5,'yangyaxuan','123456','杨雅轩','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(7,'xuqizhen','123456','许奇臻','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(8,'luguorui','123456','卢国瑞','硕士','研三',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(9,'guoyingjie','123456','郭英杰','硕士','研三',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(10,'zhangyuantong','123456','张元瞳','硕士','研三',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(11,'tianlinan','123456','田力楠','硕士','研三',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(12,'lijinfeng','123456','李锦峰','博士','博一',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(13,'mamengyu','123456','马梦雨','博士','博一',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(14,'liutong','123456','柳童','博士','研二',0,0,NULL,NULL,NULL,'2017-12-07 02:55:36'),(15,'ylhao','123456','衣龙浩','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(16,'xiaohua','123456','肖华','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(17,'shecairui','123456','佘才睿','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(18,'gaoyuhan','123456','高语晗','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(19,'yangyaxuan','123456','杨雅轩','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(20,'zhangfei','123456','张飞','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(21,'xuqizhen','123456','许奇臻','硕士','研二',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(22,'luguorui','123456','卢国瑞','硕士','研三',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(23,'guoyingjie','123456','郭英杰','硕士','研三',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(24,'zhangyuantong','123456','张元瞳','硕士','研三',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(25,'tianlinan','123456','田力楠','硕士','研三',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(26,'lijinfeng','123456','李锦峰','博士','博一',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(27,'mamengyu','123456','马梦雨','博士','博一',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49'),(28,'liutong','123456','柳童','博士','研二',0,0,NULL,NULL,NULL,'2017-12-07 03:24:49');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-07 11:26:00
