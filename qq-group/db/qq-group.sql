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


-- -----------------------------------------------------
-- Table `d_qq`.`t_people_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_qq`.`t_people_info` (
  `c_card_id` VARCHAR(32) NOT NULL,
  `c_name` VARCHAR(45) NOT NULL,
  `c_sex` VARCHAR(45) NOT NULL,
  `c_aAddress` VARCHAR(256) NOT NULL,
  `c_mobile` VARCHAR(45) NOT NULL,
  `c_eMail` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`c_card_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
