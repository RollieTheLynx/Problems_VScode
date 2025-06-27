-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: Rollie.mysql.pythonanywhere-services.com    Database: Rollie$django_playground
-- ------------------------------------------------------
-- Server version	5.7.44-rds.20240808-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'content_editors');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (6,1,8),(7,1,12),(8,1,16),(9,1,25),(10,1,26),(11,1,27),(12,1,28),(13,1,29),(14,1,30),(15,1,31),(1,1,32),(2,1,33),(3,1,34),(4,1,35),(5,1,36);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add api exchange',7,'add_apiexchange'),(26,'Can change api exchange',7,'change_apiexchange'),(27,'Can delete api exchange',7,'delete_apiexchange'),(28,'Can view api exchange',7,'view_apiexchange'),(29,'Can add cat photo',8,'add_catphoto'),(30,'Can change cat photo',8,'change_catphoto'),(31,'Can delete cat photo',8,'delete_catphoto'),(32,'Can view cat photo',8,'view_catphoto'),(33,'Can add blog post',9,'add_blogpost'),(34,'Can change blog post',9,'change_blogpost'),(35,'Can delete blog post',9,'delete_blogpost'),(36,'Can view blog post',9,'view_blogpost'),(37,'Can add city',10,'add_city'),(38,'Can change city',10,'change_city'),(39,'Can delete city',10,'delete_city'),(40,'Can view city',10,'view_city');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$swN5iYYrrYhn$dol+TlNBe7Rlc+zgmn0eRvs67XixXhB+fgaiYxaHI7w=','2023-06-27 17:45:03.376183',1,'rollie','','','lynx_online@mail.ru',1,1,'2022-09-09 13:58:39.388158');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blogpost`
--

DROP TABLE IF EXISTS `blog_blogpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_blogpost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` longtext NOT NULL,
  `content` longtext NOT NULL,
  `author` longtext NOT NULL,
  `date` datetime(6) NOT NULL,
  `city_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_blogpost_city_id_2fe5c7b7_fk` (`city_id`),
  CONSTRAINT `blog_blogpost_city_id_2fe5c7b7_fk` FOREIGN KEY (`city_id`) REFERENCES `blog_city` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blogpost`
--

LOCK TABLES `blog_blogpost` WRITE;
/*!40000 ALTER TABLE `blog_blogpost` DISABLE KEYS */;
INSERT INTO `blog_blogpost` VALUES (1,'Live!','Сайт переписан на Django и запущен в деплой.','jkjkkkjkjjkkjkjk','2021-09-19 12:44:10.000000',1),(9,'Testing author autofill','blah blah','rollie','2021-09-21 16:14:14.000000',1),(10,'Added authorization','Now only mods can edit blog','rollie','2021-09-22 20:11:22.000000',1),(11,'Added City to blog','City is a foreign key in the database!','rollie','2023-06-27 18:45:18.000000',2);
/*!40000 ALTER TABLE `blog_blogpost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_city`
--

DROP TABLE IF EXISTS `blog_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_city`
--

LOCK TABLES `blog_city` WRITE;
/*!40000 ALTER TABLE `blog_city` DISABLE KEYS */;
INSERT INTO `blog_city` VALUES (1,'Orel'),(2,'Kazan');
/*!40000 ALTER TABLE `blog_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-09-21 13:07:17.919486','1','BlogPost object (1)',2,'\"[{\"\"changed\"\": {\"\"fields\"\": [\"\"Author\"\"]}}]\"',9,1),(2,'2021-09-22 17:40:26.091302','2','giganigga',3,'\"\"',4,1),(3,'2021-09-22 19:44:39.223357','1','content_editors',1,'\"[{\"\"added\"\": {}}]\"',3,1),(4,'2021-09-22 19:45:05.025144','3','tim',2,'\"[{\"\"changed\"\": {\"\"fields\"\": [\"\"Groups\"\"]}}]\"',4,1),(5,'2023-06-27 17:52:03.254880','1','BlogPost object (1)',2,'[{\"changed\": {\"fields\": [\"city\"]}}]',9,1),(6,'2023-06-27 17:52:11.170587','9','BlogPost object (9)',2,'[{\"changed\": {\"fields\": [\"city\"]}}]',9,1),(7,'2023-06-27 17:52:20.758388','10','BlogPost object (10)',2,'[{\"changed\": {\"fields\": [\"city\"]}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'blog','blogpost'),(10,'blog','city'),(5,'contenttypes','contenttype'),(7,'pages','apiexchange'),(8,'pages','catphoto'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-09-08 22:19:33.592240'),(2,'auth','0001_initial','2022-09-08 22:21:34.521337'),(3,'admin','0001_initial','2022-09-08 22:22:10.538996'),(4,'admin','0002_logentry_remove_auto_add','2022-09-08 22:22:10.980716'),(5,'admin','0003_logentry_add_action_flag_choices','2022-09-08 22:22:10.998551'),(6,'contenttypes','0002_remove_content_type_name','2022-09-08 22:22:11.358059'),(7,'auth','0002_alter_permission_name_max_length','2022-09-08 22:22:11.572323'),(8,'auth','0003_alter_user_email_max_length','2022-09-08 22:22:11.784079'),(9,'auth','0004_alter_user_username_opts','2022-09-08 22:22:11.808045'),(10,'auth','0005_alter_user_last_login_null','2022-09-08 22:22:11.944146'),(11,'auth','0006_require_contenttypes_0002','2022-09-08 22:22:11.961153'),(12,'auth','0007_alter_validators_add_error_messages','2022-09-08 22:22:11.984366'),(13,'auth','0008_alter_user_username_max_length','2022-09-08 22:22:12.188306'),(14,'auth','0009_alter_user_last_name_max_length','2022-09-08 22:22:12.363640'),(15,'auth','0010_alter_group_name_max_length','2022-09-08 22:22:12.488923'),(16,'auth','0011_update_proxy_permissions','2022-09-08 22:22:12.506145'),(17,'blog','0001_initial','2022-09-08 22:22:34.708144'),(18,'blog','0002_alter_blogpost_date','2022-09-08 22:22:34.723947'),(19,'blog','0003_alter_blogpost_date','2022-09-08 22:22:34.736712'),(20,'pages','0001_initial','2022-09-08 22:22:57.732109'),(21,'pages','0002_alter_catphoto_photo','2022-09-08 22:22:57.748887'),(22,'pages','0003_auto_20210918_1735','2022-09-08 22:22:57.760148'),(23,'sessions','0001_initial','2022-09-08 22:23:10.994126'),(24,'sessions','0001_initial','2021-09-19 10:44:37.793430'),(25,'blog','0004_city_alter_blogpost_date_blogpost_city','2023-06-27 17:44:15.244922'),(26,'blog','0005_alter_blogpost_date','2023-06-27 17:44:15.310902'),(27,'blog','0006_auto_20230627_1743','2023-06-27 17:44:15.507028'),(28,'pages','0004_alter_catphoto_options','2023-06-27 17:44:15.514444'),(29,'pages','0005_auto_20230627_1743','2023-06-27 17:44:15.614744');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4m8nvuowqoua19jc5ghyce658tjr5vps','.eJxVjEEOwiAQAP_C2RDoFmQ9evcNZFlAqgaS0p6MfzckPeh1ZjJv4Wnfit97Wv0SxUVocfplgfiZ6hDxQfXeJLe6rUuQI5GH7fLWYnpdj_ZvUKiXsY0aJrQppNmQway10cgZwBA4QKtwAhvB5XjmwKwoQ54DZ1IJ0VgnPl_Rpzfd:1mSFgf:8lLVaG4LUJ7_5yNRGwtTEr47P2E5Wv0VQ2jxgZqSjys','2021-10-04 09:34:09.132631'),('807aftriq3mwxcbo3f36me2mq7ljzhne','eyJfbGFuZ3VhZ2UiOiJydSJ9:1nWOV8:FIvHYzfnwkDbE72Rc9aIwN2DVg-hdIbuZOrXnpAE46U','2022-04-04 20:19:38.328218'),('93ghmzlzaispfbwhzobk5d9liyd6b28t','ZWU4NmM0NmM0NTU5ZThhNmNhMDcwNmJiMTZkYzllYmEzY2NjOWVkMDp7Il9sYW5ndWFnZSI6ImVuIn0=','2023-07-13 21:47:33.176273'),('9pj5s814nme2x4hvm2xyaoleu6ned1x0','ZWU4NmM0NmM0NTU5ZThhNmNhMDcwNmJiMTZkYzllYmEzY2NjOWVkMDp7Il9sYW5ndWFnZSI6ImVuIn0=','2023-02-27 22:56:11.547619'),('kqba90cf00qljxwnbrw1oj5i9fimwx8z','MjI1YzY0YzRhNjM1ZjQ1OTU5MmQyNzg4YmQzNWM3MjFkZGNlYTZkZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxMDY5MGVhMDQxNmE0YmMyNTU3Mjk3ODc0NThlOGQ1MTY2Y2MyYThkIn0=','2022-09-23 13:59:05.487833'),('ljqsc537f99antgvp45nwlabuig4lzpg','.eJxVjEEOgyAQRe_CuiHiCHW67L5nIMMwqK3RBGTV9O7VxI3b997_X-VnWoZKg6iHylXdlKe6jb4WyX6KOzRXFog_shwivvflqnldtjwFfST6tEW_1ijz82wvByOV8biNBlp0EqSzZDEZYw1yArAEPaBrsAUXoU_xzoG5oQSpC5yoEUTrevX7A7AwPVU:1nVwaE:E4psMioC_JolRcSM98LmOmiqTsDvrJQejGf14iB8vgo','2022-04-03 14:31:02.211436'),('m4fqq9t9b75a2v7o7v0hppl26gdy8dwe','eyJfbGFuZ3VhZ2UiOiJlbiJ9:1nWXGG:7hULSwwE2q7gyTzFEfnUcqoLBt4fmBNJIRSpqN2kK90','2022-04-05 05:40:52.166965');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_apiexchange`
--

DROP TABLE IF EXISTS `pages_apiexchange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_apiexchange` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `rate_eur_rur` decimal(40,14) NOT NULL,
  `rate_usd_rur` decimal(40,14) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `date` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_apiexchange`
--

LOCK TABLES `pages_apiexchange` WRITE;
/*!40000 ALTER TABLE `pages_apiexchange` DISABLE KEYS */;
INSERT INTO `pages_apiexchange` VALUES (1,'2022-09-09',61.14338122898196,60.71276789508834),(2,'2019-09-20',85.38251366120218,72.80139778683751),(3,'2020-09-20',85.52125203112973,73.04068366079906),(4,'2022-09-20',85.37522410996330,72.85974499089254),(36,'2023-09-20',85.30239699735561,72.84912945290304),(37,'2028-10-20',81.84645604845310,70.57661091114404),(38,'2008-11-20',82.38589553468447,71.26567844925884),(39,'2009-11-20',82.63779852904719,71.21999857560003),(40,'2023-11-20',83.97010664203543,74.74400179385604),(41,'2012-03-20',146.13473622680110,134.03029084573114),(42,'2013-03-20',146.24159110851124,134.01232913428035),(43,'2019-03-20',118.92020454275182,107.41138560687432),(44,'2020-03-20',118.93434823977164,107.41138560687432),(45,'2021-03-20',111.54489682097044,101.04071940992220),(46,'2022-03-20',117.13716762328687,106.55301012253597),(47,'2023-02-04',76.30093087135663,70.59155724975292),(48,'2023-02-13',79.44073721004131,74.06858751203615),(49,'2023-06-28',93.45794392523365,85.38251366120218),(50,'2023-06-29',94.04683532399135,86.39308855291577);
/*!40000 ALTER TABLE `pages_apiexchange` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_catphoto`
--

DROP TABLE IF EXISTS `pages_catphoto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_catphoto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_catphoto`
--

LOCK TABLES `pages_catphoto` WRITE;
/*!40000 ALTER TABLE `pages_catphoto` DISABLE KEYS */;
INSERT INTO `pages_catphoto` VALUES (1,'cat_photos/1.jpg'),(2,'cat_photos/14117813373971.jpg'),(3,'cat_photos/14275277146801.jpg'),(4,'cat_photos/1435691453414.jpg'),(5,'cat_photos/1435692082209.jpg'),(6,'cat_photos/1435692148733.jpg'),(7,'cat_photos/1435694078613.jpg'),(8,'cat_photos/14662200939630.jpg'),(9,'cat_photos/14662208180752.jpg'),(10,'cat_photos/1589711817049.jpg'),(11,'cat_photos/2.jpg'),(12,'cat_photos/3.jpg'),(13,'cat_photos/4.jpg'),(14,'cat_photos/5.jpg'),(15,'cat_photos/6.jpg'),(16,'cat_photos/7.jpg'),(17,'cat_photos/8.jpg'),(18,'cat_photos/9.jpg'),(19,'cat_photos/90.jpg'),(20,'cat_photos/91.jpg'),(21,'cat_photos/a7c49da7gw1ey0x52qkjqj20c80c8jsb.jpg'),(22,'cat_photos/a7c49da7gw1ey0x539760j20c80c80tu.jpg'),(23,'cat_photos/a7c49da7jw1ejsrjhl7fpj20c80923zg.jpg'),(24,'cat_photos/a7c49da7jw1ejsrjq4cr7j20c80lfjsf.jpg'),(25,'cat_photos/a7c49da7jw1ejsrjunmgfj20c80960t9.jpg'),(26,'cat_photos/a7c49da7jw1ejsrjwrzpij20c8096wfk.jpg'),(27,'cat_photos/jellybeans.jpg'),(28,'cat_photos/z1352737299038.jpg');
/*!40000 ALTER TABLE `pages_catphoto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-02 20:49:02
