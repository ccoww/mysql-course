-- 第3课课堂演示

USE ecommerce;

-- 聚合函数
SELECT
    COUNT(*)      AS 总数,
    SUM(stock)    AS 库存,
    AVG(price)    AS均价,
    MAX(price)    AS最高,
    MIN(price)    AS最低
FROM products;

-- GROUP BY
SELECT
    category_id,
    COUNT(*)   AS cnt,
    AVG(price) AS avg_price
FROM products
GROUP BY category_id;

-- HAVING
SELECT
    category_id,
    COUNT(*) AS cnt
FROM products
GROUP BY category_id
HAVING cnt > 5;

-- 综合：用户消费排行
SELECT
    u.username,
    COUNT(o.id)       AS order_count,
    SUM(o.total_amount) AS total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.status = 'paid'
GROUP BY u.id, u.username
ORDER BY total DESC
LIMIT 5;
