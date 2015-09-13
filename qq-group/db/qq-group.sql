SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `d_qq` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `d_qq` ;

-- -----------------------------------------------------
-- Table `d_qq`.`t_qq_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_qq`.`t_qq_info` (
  `c_qq` BIGINT NOT NULL,
  `c_nick` VARCHAR(45) NOT NULL,
  `c_sex` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`c_qq`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `d_qq`.`t_qq_group_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_qq`.`t_qq_group_info` (
  `c_group` BIGINT NOT NULL,
  `c_group_name` VARCHAR(45) NOT NULL,
  `c_group_info` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`c_group`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `d_qq`.`t_qq_group_map`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_qq`.`t_qq_group_map` (
  `c_qq` BIGINT NOT NULL,
  `c_group` BIGINT NOT NULL,
  `c_group_nick` VARCHAR(45) NOT NULL,
  `t_group_role` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`c_qq`, `c_group`),
  INDEX `fk_t_qq_group_map_t_group_info_idx` (`c_group` ASC),
  CONSTRAINT `fk_t_qq_group_map_t_group_info`
    FOREIGN KEY (`c_group`)
    REFERENCES `d_qq`.`t_qq_group_info` (`c_group`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_t_qq_group_map_t_qq_info1`
    FOREIGN KEY (`c_qq`)
    REFERENCES `d_qq`.`t_qq_info` (`c_qq`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;




CREATE TABLE `t_qq_info_0` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_1` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_2` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_3` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_4` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_5` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_6` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_7` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_8` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_info_9` (`c_qq` bigint(20) NOT NULL,`c_nick` varchar(45) DEFAULT NULL,`c_sex` varchar(45) DEFAULT NULL,`c_state` int(11) NOT NULL DEFAULT '0',PRIMARY KEY (`c_qq`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;





CREATE TABLE `t_group_info_0` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_1` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_2` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_3` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_4` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_5` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_6` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_7` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_8` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_info_9` (`c_group` bigint(20) NOT NULL,`c_group_name` varchar(45) DEFAULT NULL,`c_group_info` varchar(255) DEFAULT NULL,`c_state` int(11) NOT NULL,PRIMARY KEY (`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;



CREATE TABLE `t_qq_to_group_0` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_1` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_2` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_3` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_4` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_5` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_6` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_7` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_8` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_qq_to_group_9` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;






CREATE TABLE `t_group_to_qq_0` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_1` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_2` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_3` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_4` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_5` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_6` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_7` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_8` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `t_group_to_qq_9` (`c_qq` bigint(20) NOT NULL,`c_group` bigint(20) NOT NULL,`c_group_nick` varchar(45) NOT NULL,`t_group_role` varchar(45) NOT NULL,`t_group_sex` varchar(45) NOT NULL,PRIMARY KEY (`c_qq`,`c_group`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;



























