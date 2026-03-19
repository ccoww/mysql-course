# 第1课：SELECT 基础查询

> 本课使用电商数据库 `ecommerce`

## 1. 数据库是什么

数据库就是**存放数据的仓库**，里面有很多**表（Table）**。

| 概念 | 比喻 |
|------|------|
| 数据库 | 文件柜 |
| 表 | 文件夹里的一张表格 |
| 行 Row | 表格中的一行记录 |
| 列 Column | 表格中的一个字段 |

## 2. 认识电商数据库

本课使用电商数据库，包含：

- `users` - 用户表（10人）
- `products` - 商品表（30个）
- `categories` - 分类表（8类）
- `orders` - 订单表（20笔）
- `order_items` - 订单明细（27条）
- `reviews` - 商品评论（17条）

### 查看表结构

```sql
USE ecommerce;

-- 查看所有表
SHOW TABLES;

-- 查看表结构
DESCRIBE products;
-- 或
SHOW COLUMNS FROM products;
```

## 3. SELECT 基础

### 3.1 查询所有列

```sql
SELECT * FROM products;
```

### 3.2 查询指定列

```sql
SELECT name, price, stock FROM products;
```

### 3.3 列别名

```sql
SELECT name AS 商品名, price AS 价格 FROM products;
```

### 3.4 去重

```sql
SELECT DISTINCT category_id FROM products;
```

## 4. WHERE 条件过滤

### 4.1 比较运算

```sql
-- 价格高于1000的商品
SELECT name, price FROM products WHERE price > 1000;

-- 指定分类的商品
SELECT name, category_id FROM products WHERE category_id = 2;
```

### 4.2 AND / OR 逻辑运算

```sql
-- 并且
SELECT name, price FROM products WHERE price > 100 AND price < 5000;

-- 或者
SELECT name, category_id FROM products WHERE category_id = 2 OR category_id = 3;
```

### 4.3 BETWEEN 范围

```sql
SELECT name, price FROM products WHERE price BETWEEN 100 AND 500;
```

### 4.4 IN 列表

```sql
SELECT name, category_id FROM products WHERE category_id IN (2, 3, 4);
```

### 4.5 LIKE 模糊匹配

```sql
-- 名称包含"手机"的商品
SELECT name FROM products WHERE name LIKE '%手机%';

-- 以"i"开头的商品
SELECT name FROM products WHERE name LIKE 'i%';
```

### 4.6 IS NULL 空值

```sql
-- 有评分的商品
SELECT name, rating FROM products WHERE rating IS NOT NULL;
```

## 5. 排序与分页

### 5.1 ORDER BY 排序

```sql
-- 按价格升序
SELECT name, price FROM products ORDER BY price ASC;

-- 按价格降序
SELECT name, price FROM products ORDER BY price DESC;

-- 多列排序
SELECT name, price, sales_count FROM products
ORDER BY price DESC, sales_count DESC;
```

### 5.2 LIMIT 分页

```sql
-- 前5个商品
SELECT name, price FROM products ORDER BY price DESC LIMIT 5;

-- 第2页（每页5条）
SELECT name, price FROM products ORDER BY price DESC LIMIT 5 OFFSET 10;
-- 或
SELECT name, price FROM products ORDER BY price DESC LIMIT 10, 5;
```

## 6. 常用函数

### 6.1 字符串函数

```sql
SELECT
    UPPER(name)   AS 大写名称,
    LENGTH(name)  AS 字符数
FROM products;
```

### 6.2 数值函数

```sql
SELECT
    name,
    price,
    ROUND(price, 0)    AS 四舍五入,
    CEIL(price)        AS 向上取整
FROM products;
```

### 6.3 条件函数

```sql
SELECT
    name,
    price,
    CASE
        WHEN price < 100 THEN '便宜'
        WHEN price < 1000 THEN '中等'
        ELSE '昂贵'
    END AS 价格档次
FROM products;
```

## 7. 课堂练习

1. 查询所有在售商品，显示名称、价格、库存
2. 查询价格低于 100 元的商品
3. 查询"手机"分类或"电脑"分类的商品
4. 查询销量前5的商品
5. 查询商品，显示名称、八折价格（保留2位小数）
