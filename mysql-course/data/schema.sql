-- ============================================================
-- 电商数据库 Schema
-- MySQL 8.0+
-- 3节课系列课程共用数据库
-- ============================================================

DROP DATABASE IF EXISTS ecommerce;
CREATE DATABASE ecommerce
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE ecommerce;

-- 用户表
CREATE TABLE users (
    id          INT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    username    VARCHAR(50)     NOT NULL UNIQUE,
    email       VARCHAR(100)    NOT NULL UNIQUE,
    phone       VARCHAR(20),
    gender      ENUM('M','F')   DEFAULT 'M',
    age         TINYINT UNSIGNED,
    created_at  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status      ENUM('active','inactive') DEFAULT 'active'
) ENGINE=InnoDB;

-- 商品分类
CREATE TABLE categories (
    id          INT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50)     NOT NULL UNIQUE,
    parent_id   INT UNSIGNED    DEFAULT NULL,
    sort_order  INT             DEFAULT 0
) ENGINE=InnoDB;

-- 商品表
CREATE TABLE products (
    id              INT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(100)    NOT NULL,
    category_id     INT UNSIGNED    NOT NULL,
    price           DECIMAL(10,2)   NOT NULL,
    stock           INT             NOT NULL DEFAULT 0,
    sales_count     INT             NOT NULL DEFAULT 0,
    rating          DECIMAL(2,1)    DEFAULT 0,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_on_sale      BOOLEAN         DEFAULT TRUE,
    INDEX idx_category (category_id),
    INDEX idx_price (price),
    CONSTRAINT fk_products_cat FOREIGN KEY (category_id) REFERENCES categories(id)
) ENGINE=InnoDB;

-- 订单表
CREATE TABLE orders (
    id              BIGINT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    user_id         INT UNSIGNED      NOT NULL,
    order_no        VARCHAR(32)       NOT NULL UNIQUE,
    total_amount    DECIMAL(12,2)     NOT NULL DEFAULT 0,
    status          ENUM('pending','paid','shipped','completed','cancelled') DEFAULT 'pending',
    paid_at         DATETIME,
    shipped_at      DATETIME,
    created_at      DATETIME          NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_user (user_id),
    INDEX idx_status (status),
    INDEX idx_created (created_at),
    CONSTRAINT fk_orders_user FOREIGN KEY (user_id) REFERENCES users(id)
) ENGINE=InnoDB;

-- 订单明细
CREATE TABLE order_items (
    id              BIGINT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    order_id        BIGINT UNSIGNED    NOT NULL,
    product_id      INT UNSIGNED       NOT NULL,
    product_name    VARCHAR(100)       NOT NULL,
    unit_price      DECIMAL(10,2)      NOT NULL,
    quantity        INT                NOT NULL DEFAULT 1,
    subtotal        DECIMAL(12,2)      NOT NULL,
    INDEX idx_order (order_id),
    INDEX idx_product (product_id),
    CONSTRAINT fk_items_order FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    CONSTRAINT fk_items_product FOREIGN KEY (product_id) REFERENCES products(id)
) ENGINE=InnoDB;

-- 商品评论
CREATE TABLE reviews (
    id          BIGINT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    product_id  INT UNSIGNED       NOT NULL,
    user_id     INT UNSIGNED       NOT NULL,
    rating      TINYINT            NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment     TEXT,
    created_at  DATETIME           NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_product (product_id),
    INDEX idx_user (user_id),
    CONSTRAINT fk_reviews_product FOREIGN KEY (product_id) REFERENCES products(id),
    CONSTRAINT fk_reviews_user FOREIGN KEY (user_id) REFERENCES users(id)
) ENGINE=InnoDB;
