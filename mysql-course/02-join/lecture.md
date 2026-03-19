# 第2课：JOIN 多表查询

> 本课使用电商数据库 `ecommerce`

## 1. 为什么要多表

实际数据分散在多张表中：

```
users ────── orders ────── order_items ────── products
  │            │               │                  │
用户信息      订单头          订单明细           商品信息
```

## 2. 认识表关系

```sql
-- users.id = orders.user_id（主键-外键关系）
-- orders.id = order_items.order_id
-- products.id = order_items.product_id
-- products.category_id = categories.id
```

## 3. INNER JOIN 内连接

**只返回两表都有的记录**

### 3.1 两表连接

```sql
-- 查询订单及其用户信息
SELECT
    o.id          AS 订单ID,
    o.total_amount AS 金额,
    u.username    AS 用户名,
    u.email       AS 邮箱
FROM orders o
INNER JOIN users u ON o.user_id = u.id;
```

### 3.2 多表连接

```sql
-- 查询订单明细：订单号、商品名称、购买数量
SELECT
    o.order_no    AS 订单号,
    p.name        AS 商品名,
    oi.quantity   AS 数量
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

## 4. LEFT JOIN 左外连接

**返回左表所有记录，右表无匹配则显示 NULL**

```sql
-- 查询所有用户及其订单（含未下单用户）
SELECT
    u.username,
    o.id        AS 订单ID,
    o.total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

## 5. RIGHT JOIN 右外连接

```sql
-- 所有订单都要显示，即使用户已被删除
SELECT
    o.id        AS 订单ID,
    u.username  AS 用户名
FROM orders o
RIGHT JOIN users u ON o.user_id = u.id;
```

## 6. 多表连接进阶

### 6.1 查询完整订单信息

```sql
SELECT
    o.order_no           AS 订单号,
    u.username            AS 用户名,
    p.name                AS 商品名,
    oi.quantity           AS 数量,
    oi.unit_price         AS 单价,
    oi.subtotal           AS 小计
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.status = 'completed'
ORDER BY o.created_at DESC;
```

### 6.2 LEFT JOIN 统计

```sql
-- 每个用户的订单数量（含未下单的）
SELECT
    u.username,
    COUNT(o.id) AS 订单数
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

## 7. 自连接（SELF JOIN）

同一表内关联（适用于层级数据，如分类的父子关系）

```sql
-- 查询分类及其父分类
SELECT
    c1.name    AS 子分类,
    c2.name     AS 父分类
FROM categories c1
LEFT JOIN categories c2 ON c1.parent_id = c2.id;
```

## 8. 课堂练习

1. 查询所有已支付订单的用户名、订单号、金额
2. 查询所有商品及其分类名称
3. 查询所有用户及其订单数量（含未下单的）
4. 查询购买过"手机"分类商品的用户
5. 查询每个订单的商品明细
