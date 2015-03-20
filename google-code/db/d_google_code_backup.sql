SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `d_google_code_backup` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `d_google_code_backup` ;

-- -----------------------------------------------------
-- Table `d_google_code_backup`.`t_lable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_google_code_backup`.`t_lable` (
  `c_id` INT NOT NULL AUTO_INCREMENT,
  `c_name` VARCHAR(45) NOT NULL,
  `c_search_page` INT NOT NULL DEFAULT 0,
  `c_max_num` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`c_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `d_google_code_backup`.`t_project`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_google_code_backup`.`t_project` (
  `c_id` INT NOT NULL AUTO_INCREMENT,
  `c_name` VARCHAR(45) NOT NULL,
  `c_starred_num` INT NOT NULL DEFAULT 0,
  `c_members_num` INT NOT NULL DEFAULT 0,
  `c_ok` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`c_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `d_google_code_backup`.`t_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_google_code_backup`.`t_user` (
  `c_id` INT NOT NULL AUTO_INCREMENT,
  `c_name` VARCHAR(45) NOT NULL DEFAULT '',
  `c_projects_num` INT NOT NULL DEFAULT 0,
  `c_starred_num` INT NOT NULL DEFAULT 0,
  `c_ok` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`c_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `d_google_code_backup`.`t_prj_lable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_google_code_backup`.`t_prj_lable` (
  `c_prj_name` VARCHAR(45) NOT NULL,
  `c_lable_name` VARCHAR(45) NOT NULL,
  INDEX `fk_t_prj_lable_t_project_idx` (`c_prj_name` ASC),
  INDEX `fk_t_prj_lable_t_lable1_idx` (`c_lable_name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `d_google_code_backup`.`t_prj_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `d_google_code_backup`.`t_prj_user` (
  `c_id` INT NOT NULL AUTO_INCREMENT,
  `c_prj_name` VARCHAR(45) NOT NULL,
  `c_user_name` VARCHAR(45) NOT NULL,
  `c_type` INT NOT NULL DEFAULT 0 COMMENT '0 project\n1 own',
  PRIMARY KEY (`c_id`),
  INDEX `fk_t_prj_user_t_project1_idx` (`c_prj_name` ASC),
  INDEX `fk_t_prj_user_t_user1_idx` (`c_user_name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
