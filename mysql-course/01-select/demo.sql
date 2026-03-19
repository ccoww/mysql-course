-- 第1课课堂演示

USE ecommerce;

-- 查看表
SHOW TABLES;
DESCRIBE products;

-- SELECT基础
SELECT * FROM products LIMIT 3;
SELECT name, price, stock FROM products;
SELECT name AS 商品名, price AS 价格 FROM products;
SELECT DISTINCT category_id FROM products;

-- WHERE
SELECT name, price FROM products WHERE price > 1000;
SELECT name, price FROM products WHERE price BETWEEN 100 AND 1000;
SELECT name, category_id FROM products WHERE category_id IN (2,3);
SELECT name FROM products WHERE name LIKE '%手机%';
SELECT name, rating FROM products WHERE rating IS NULL;

-- ORDER BY & LIMIT
SELECT name, price FROM products ORDER BY price DESC LIMIT 5;
SELECT name, price FROM products ORDER BY price DESC LIMIT 5, 5;

-- 函数
SELECT
    name,
    UPPER(name) AS 大写,
    ROUND(price, 0) AS 四舍五入
FROM products;

SELECT
    name,
    price,
    CASE
        WHEN price < 100 THEN '便宜'
        WHEN price < 1000 THEN '中等'
        ELSE '贵'
    END AS 档次
FROM products;
