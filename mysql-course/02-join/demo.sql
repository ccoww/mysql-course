-- 第2课课堂演示

USE ecommerce;

-- INNER JOIN
SELECT
    o.id,
    u.username,
    o.total_amount
FROM orders o
JOIN users u ON o.user_id = u.id
LIMIT 5;

-- 多表JOIN
SELECT
    o.order_no,
    p.name,
    oi.quantity
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
LIMIT 5;

-- LEFT JOIN
SELECT
    u.username,
    o.id AS order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- 统计每个用户订单数
SELECT
    u.username,
    COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;

-- 自连接：分类父子关系
SELECT
    c1.name AS 子分类,
    c2.name AS 父分类
FROM categories c1
LEFT JOIN categories c2 ON c1.parent_id = c2.id;
