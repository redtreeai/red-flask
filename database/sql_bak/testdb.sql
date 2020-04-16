/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50615
Source Host           : localhost:3306
Source Database       : testdb

Target Server Type    : MYSQL
Target Server Version : 50615
File Encoding         : 65001

Date: 2020-04-16 11:07:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `salt` varchar(4) NOT NULL,
  `password` varchar(32) NOT NULL,
  `del_flag` tinyint(4) NOT NULL,
  `created_time` int(11) NOT NULL,
  `updated_time` int(11) NOT NULL,
  `created_user` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
