# 第1课参考答案

## 题1
```sql
SELECT name, price, stock FROM products;
```

## 题2
```sql
SELECT name, price
FROM products
WHERE price BETWEEN 500 AND 2000
ORDER BY price ASC;
```

## 题3
```sql
SELECT name, category_id
FROM products
WHERE name LIKE '%手机%';
```

## 题4
```sql
SELECT name, category_id, price
FROM products
WHERE category_id IN (2, 3);
```

## 题5
```sql
SELECT name, rating
FROM products
WHERE rating IS NULL;
```

## 题6
```sql
SELECT name, stock
FROM products
WHERE stock < 50
ORDER BY stock ASC;
```

## 题7
```sql
SELECT name, sales_count
FROM products
ORDER BY sales_count DESC
LIMIT 3;
```

## 题8
```sql
SELECT name, category_id, price
FROM products
ORDER BY category_id ASC, price DESC;
```

## 题9
```sql
SELECT
    name,
    price AS 原价,
    ROUND(price * 0.9, 2) AS 折后价
FROM products;
```

## 题10
```sql
SELECT
    name,
    price,
    CASE
        WHEN price < 100 THEN '平价'
        WHEN price < 1000 THEN '中档'
        ELSE '高端'
    END AS 价位档次
FROM products;
```
