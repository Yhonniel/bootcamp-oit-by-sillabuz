drop database ecommerce;

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ecommerce
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ecommerce
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ecommerce` DEFAULT CHARACTER SET utf8 ;
USE `ecommerce` ;

-- -----------------------------------------------------
-- Table `ecommerce`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ecommerce`.`Cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellidos` VARCHAR(255) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(11) NULL,
  `pais` VARCHAR(50) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ecommerce`.`Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ecommerce`.`Categoria` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `descripcion` VARCHAR(255) NULL,
  `icono` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ecommerce`.`Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ecommerce`.`Producto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `sku` VARCHAR(50) NOT NULL,
  `nombre` VARCHAR(150) NOT NULL,
  `precio` DECIMAL NOT NULL,
  `imagen` VARCHAR(255) NOT NULL,
  `stock` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ecommerce`.`Orden`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ecommerce`.`Orden` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `orden_direccion` VARCHAR(255) NOT NULL,
  `orden_estado` ENUM('CREADO', 'PAGADO', 'ENVALADO', 'ENVIADO', 'ENTREGADO', 'RECHAZADO', 'CANCELADO') NOT NULL DEFAULT 'CREADO',
  `precio` DECIMAL NOT NULL,
  `cliente_id` INT NOT NULL,
  PRIMARY KEY (`id`, `cliente_id`),
  INDEX `fk_Orden_Cliente1_idx` (`cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_Orden_Cliente1`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `ecommerce`.`Cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ecommerce`.`oden_detalle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ecommerce`.`oden_detalle` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cantidad` VARCHAR(45) NOT NULL,
  `precio` VARCHAR(45) NOT NULL,
  `sku` VARCHAR(45) NOT NULL,
  `orden_id` INT NOT NULL,
  `producto_id` INT NOT NULL,
  PRIMARY KEY (`id`, `orden_id`, `producto_id`),
  UNIQUE INDEX `oden_detallecol_UNIQUE` (`sku` ASC) VISIBLE,
  INDEX `fk_oden_detalle_Orden1_idx` (`orden_id` ASC) VISIBLE,
  INDEX `fk_oden_detalle_Producto1_idx` (`producto_id` ASC) VISIBLE,
  CONSTRAINT `fk_oden_detalle_Orden1`
    FOREIGN KEY (`orden_id`)
    REFERENCES `ecommerce`.`Orden` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_oden_detalle_Producto1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `ecommerce`.`Producto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ecommerce`.`Producto_has_Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ecommerce`.`Producto_has_Categoria` (
  `producto_id` INT NOT NULL,
  `categoria_id` INT NOT NULL,
  PRIMARY KEY (`producto_id`, `categoria_id`),
  INDEX `fk_Producto_has_Categoria_Categoria1_idx` (`categoria_id` ASC) VISIBLE,
  INDEX `fk_Producto_has_Categoria_Producto_idx` (`producto_id` ASC) VISIBLE,
  CONSTRAINT `fk_Producto_has_Categoria_Producto`
    FOREIGN KEY (`producto_id`)
    REFERENCES `ecommerce`.`Producto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_has_Categoria_Categoria1`
    FOREIGN KEY (`categoria_id`)
    REFERENCES `ecommerce`.`Categoria` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
