# 参考答案

---

## 题 1

```sql
SELECT
    title    AS 书名,
    category AS 分类,
    price    AS 售价
FROM books;
```

---

## 题 2

```sql
SELECT DISTINCT category
FROM books
ORDER BY category ASC;
```

---

## 题 3

```sql
SELECT title, price, stock
FROM books
WHERE category = '科幻'
ORDER BY price ASC;
```

---

## 题 4

```sql
SELECT title, price, stock
FROM books
WHERE price BETWEEN 40 AND 70
  AND stock > 100;
```

---

## 题 5

```sql
SELECT DISTINCT title, category
FROM books
WHERE title LIKE '%的%'
   OR category = '散文';
```

---

## 题 6

```sql
SELECT title, category
FROM books
WHERE author_id IS NULL;
```

---

## 题 7

```sql
SELECT title, published_year, price
FROM books
WHERE category = '文学'
ORDER BY published_year ASC, price ASC
LIMIT 5;
```

---

## 题 8

```sql
SELECT title, price
FROM books
ORDER BY price DESC
LIMIT 3 OFFSET 2;
```

---

## 题 9

```sql
SELECT
    title,
    price                    AS 原价,
    ROUND(price * 0.9, 2)   AS 折后价
FROM books
ORDER BY 折后价 ASC;
```

---

## 题 10（挑战题）

```sql
SELECT
    title   AS 书名,
    price   AS 价格,
    CASE
        WHEN price < 35              THEN '经济实惠'
        WHEN price BETWEEN 35 AND 60 THEN '性价比高'
        ELSE                              '高端精品'
    END AS 价格档次,
    stock   AS 库存,
    CASE
        WHEN stock < 50              THEN '库存紧张'
        WHEN stock BETWEEN 50 AND 150 THEN '库存正常'
        ELSE                               '库存充足'
    END AS 库存状态
FROM books
ORDER BY price ASC;
```

---

## 课堂练习（讲义第七部分）答案

**题 1**
```sql
SELECT title, price
FROM books
WHERE category = '悬疑'
ORDER BY price ASC;
```

**题 2**
```sql
SELECT title, stock, price
FROM books
WHERE stock > 80 AND price < 50;
```

**题 3**
```sql
SELECT title, category
FROM books
WHERE title LIKE '%的%';
```

**题 4**
```sql
SELECT title, published_year
FROM books
WHERE published_year > 2000
ORDER BY published_year DESC
LIMIT 5;
```

**题 5**
```sql
SELECT
    title,
    price              AS 原价,
    ROUND(price * 0.9, 2) AS 折后价
FROM books
ORDER BY 折后价 ASC;
```
