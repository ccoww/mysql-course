-- ============================================================
-- 在线书店数据库 Schema
-- MySQL 8.0+
-- ============================================================

DROP DATABASE IF EXISTS bookstore;
CREATE DATABASE bookstore
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE bookstore;

-- 作者表
CREATE TABLE authors (
    id          INT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50)     NOT NULL,
    country     VARCHAR(30)     NOT NULL DEFAULT '中国',
    born_year   YEAR
) ENGINE=InnoDB;

-- 图书表
CREATE TABLE books (
    id              INT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    title           VARCHAR(100)    NOT NULL,
    author_id       INT UNSIGNED    NOT NULL,
    category        VARCHAR(20)     NOT NULL,
    price           DECIMAL(8,2)    NOT NULL CHECK (price > 0),
    stock           INT             NOT NULL DEFAULT 0,
    published_year  YEAR,
    is_available    BOOLEAN         NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_books_author
        FOREIGN KEY (author_id) REFERENCES authors(id)
) ENGINE=InnoDB;
