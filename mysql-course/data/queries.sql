-- ============================================================
-- 电商数据库综合业务查询
-- 涵盖 SELECT / JOIN / 聚合统计
-- ============================================================

USE ecommerce;

-- 1. 查询各分类商品数量和平均价格
SELECT
    c.name                    AS 分类,
    COUNT(p.id)               AS 商品数,
    ROUND(AVG(p.price), 2)    AS 平均价格,
    SUM(p.stock)              AS 总库存
FROM categories c
LEFT JOIN products p ON c.id = p.category_id
WHERE p.is_on_sale = TRUE
GROUP BY c.id, c.name
ORDER BY 商品数 DESC;

-- 2. 查询各用户的消费统计
SELECT
    u.username,
    COUNT(o.id)               AS 订单数,
    SUM(o.total_amount)       AS 总消费,
    ROUND(AVG(o.total_amount), 2) AS 平均订单金额,
    MAX(o.created_at)        AS 最后下单时间
FROM users u
LEFT JOIN orders o ON u.id = o.user_id AND o.status != 'cancelled'
GROUP BY u.id, u.username
ORDER BY 总消费 DESC;

-- 3. 查询畅销商品 TOP 10
SELECT
    p.name,
    c.name            AS 分类,
    p.sales_count     AS 销量,
    p.stock           AS 库存,
    ROUND(p.rating, 1) AS 评分
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE p.is_on_sale = TRUE
ORDER BY p.sales_count DESC
LIMIT 10;

-- 4. 查询各月份订单趋势
SELECT
    DATE_FORMAT(created_at, '%Y-%m') AS 月份,
    COUNT(*)                          AS 订单数,
    SUM(total_amount)                 AS 销售额,
    SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS 取消数
FROM orders
GROUP BY 月份
ORDER BY 月份;

-- 5. 查询复购用户
SELECT
    u.username,
    COUNT(DISTINCT o.id) AS 订单数,
    SUM(o.total_amount)  AS 总消费
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.status != 'cancelled'
GROUP BY u.id, u.username
HAVING COUNT(DISTINCT o.id) > 1
ORDER BY 总消费 DESC;

-- 6. 查询商品评分统计
SELECT
    c.name                    AS 分类,
    COUNT(r.id)               AS 评论数,
    ROUND(AVG(r.rating), 2)   AS 平均评分,
    MAX(r.rating)             AS 最高评分,
    MIN(r.rating)             AS 最低评分
FROM categories c
JOIN products p ON c.id = p.category_id
JOIN reviews r ON p.id = r.product_id
GROUP BY c.id, c.name
ORDER BY 平均评分 DESC;
