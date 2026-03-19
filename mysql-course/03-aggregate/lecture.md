# 第3课：聚合统计与分组

> 本课使用电商数据库 `ecommerce`

## 1. 聚合函数

| 函数 | 说明 |
|------|------|
| COUNT() | 计数 |
| SUM() | 求和 |
| AVG() | 平均值 |
| MAX() | 最大值 |
| MIN() | 最小值 |

### 1.1 COUNT 计数

```sql
-- 统计总行数
SELECT COUNT(*) FROM products;

-- 统计非空行数
SELECT COUNT(rating) FROM products;

-- 去重计数
SELECT COUNT(DISTINCT category_id) FROM products;
```

### 1.2 SUM/AVG 统计

```sql
-- 商品总库存
SELECT SUM(stock) FROM products;

-- 平均价格
SELECT AVG(price) FROM products;

-- 最高/最低价格
SELECT MAX(price), MIN(price) FROM products;
```

### 1.3 组合使用

```sql
SELECT
    COUNT(*)         AS 商品数,
    SUM(stock)      AS 总库存,
    AVG(price)      AS 平均价格,
    MAX(price)      AS 最高价,
    MIN(price)      AS 最低价
FROM products;
```

## 2. GROUP BY 分组

### 2.1 按分类统计

```sql
SELECT
    category_id,
    COUNT(*)       AS 商品数,
    AVG(price)     AS 平均价格
FROM products
GROUP BY category_id;
```

### 2.2 按用户统计

```sql
SELECT
    user_id,
    COUNT(*)       AS 订单数,
    SUM(total_amount) AS 总金额
FROM orders
WHERE status != 'cancelled'
GROUP BY user_id;
```

### 2.3 多列分组

```sql
SELECT
    category_id,
    is_on_sale,
    COUNT(*) AS cnt
FROM products
GROUP BY category_id, is_on_sale;
```

## 3. HAVING 分组过滤

> WHERE 过滤**行**，HAVING 过滤**分组**

```sql
-- 统计各分类商品数，只显示商品数>3的
SELECT
    category_id,
    COUNT(*) AS cnt
FROM products
GROUP BY category_id
HAVING cnt > 3;
```

### 对比 WHERE vs HAVING

```sql
-- WHERE：先过滤行，再统计
SELECT category_id, AVG(price)
FROM products
WHERE price > 100
GROUP BY category_id;

-- HAVING：先统计，再过滤分组结果
SELECT category_id, AVG(price)
FROM products
GROUP BY category_id
HAVING AVG(price) > 1000;
```

## 4. WITH ROLLUP 合计

```sql
SELECT
    category_id,
    SUM(stock) AS total_stock
FROM products
GROUP BY category_id WITH ROLLUP;
```

## 5. 综合查询示例

### 5.1 各分类销售统计

```sql
SELECT
    c.name                    AS 分类,
    COUNT(DISTINCT o.id)      AS 订单数,
    SUM(oi.quantity)          AS 销售量,
    SUM(oi.subtotal)         AS 销售额
FROM categories c
JOIN products p ON c.id = p.category_id
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE o.status != 'cancelled'
GROUP BY c.id, c.name;
```

### 5.2 用户消费排行

```sql
SELECT
    u.username,
    COUNT(o.id)           AS 订单数,
    SUM(o.total_amount)   AS 总消费,
    AVG(o.total_amount)   AS 平均订单
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.status != 'cancelled'
GROUP BY u.id, u.username
ORDER BY 总消费 DESC
LIMIT 10;
```

## 6. 课堂练习

1. 统计各分类的商品数量和平均价格
2. 统计各用户的订单数和总消费金额
3. 找出消费总额超过5000的用户
4. 统计各月份订单数量和销售额
5. 找出销量最高的商品 TOP 5
