# 第3课参考答案

## 题1
```sql
SELECT
    COUNT(*)      AS 商品总数,
    SUM(stock)    AS 总库存,
    AVG(price)    AS 平均价格,
    MAX(price)    AS 最高价,
    MIN(price)    AS 最低价
FROM products;
```

## 题2
```sql
SELECT COUNT(DISTINCT category_id) FROM products;
```

## 题3
```sql
SELECT
    COUNT(*)        AS 订单数,
    SUM(total_amount) AS 总销售额
FROM orders
WHERE status = 'paid';
```

## 题4
```sql
SELECT
    category_id,
    COUNT(*)     AS 商品数,
    AVG(price)   AS 平均价格,
    MAX(price)   AS 最高价
FROM products
GROUP BY category_id;
```

## 题5
```sql
SELECT
    user_id,
    COUNT(*)          AS 订单数,
    SUM(total_amount) AS 消费总额
FROM orders
WHERE status = 'paid'
GROUP BY user_id;
```

## 题6
```sql
SELECT
    DATE_FORMAT(created_at, '%Y-%m') AS 月份,
    COUNT(*)                          AS 订单数
FROM orders
GROUP BY 月份
ORDER BY 月份;
```

## 题7
```sql
SELECT
    category_id,
    COUNT(*) AS cnt
FROM products
GROUP BY category_id
HAVING cnt > 3;
```

## 题8
```sql
SELECT
    u.username,
    SUM(o.total_amount) AS total_spent
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.status = 'paid'
GROUP BY u.id, u.username
HAVING total_spent > 3000;
```

## 题9
```sql
SELECT
    u.username,
    AVG(o.total_amount) AS avg_order
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.status = 'paid'
GROUP BY u.id, u.username
HAVING avg_order < 500;
```

## 题10
```sql
SELECT
    c.name,
    SUM(oi.subtotal) AS 销售额
FROM categories c
JOIN products p ON c.id = p.category_id
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE o.status != 'cancelled'
GROUP BY c.id, c.name
HAVING 销售额 > 10000
ORDER BY 销售额 DESC;
```
