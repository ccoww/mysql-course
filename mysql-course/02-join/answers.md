# 第2课参考答案

## 题1
```sql
SELECT
    o.order_no,
    u.username,
    o.total_amount,
    o.created_at
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.status = 'paid';
```

## 题2
```sql
SELECT
    oi.order_id,
    p.name,
    oi.quantity,
    oi.unit_price,
    oi.subtotal
FROM order_items oi
JOIN products p ON oi.product_id = p.id;
```

## 题3
```sql
SELECT
    p.name,
    c.name AS category
FROM products p
JOIN categories c ON p.category_id = c.id;
```

## 题4
```sql
SELECT
    u.username,
    COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

## 题5
```sql
SELECT
    p.name,
    COALESCE(SUM(oi.quantity), 0) AS total_sold
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name;
```

## 题6
```sql
SELECT
    p.name,
    SUM(oi.quantity) AS sales
FROM products p
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE p.category_id = 2
  AND o.status != 'cancelled'
GROUP BY p.id, p.name;
```

## 题7
```sql
SELECT
    o.order_no,
    p.name,
    oi.quantity,
    oi.unit_price,
    oi.subtotal
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE u.username = '张三';
```

## 题8
```sql
SELECT
    u.username,
    SUM(o.total_amount) AS total_spent
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.status != 'cancelled'
GROUP BY u.id, u.username
ORDER BY total_spent DESC;
```

## 题9
```sql
SELECT u.username
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

## 题10
```sql
SELECT
    u.username,
    SUM(o.total_amount) AS total_spent
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.status != 'cancelled'
GROUP BY u.id, u.username
HAVING total_spent > 5000;
```
