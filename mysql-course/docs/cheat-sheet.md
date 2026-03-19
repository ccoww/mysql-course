# SQL 查询速查表

## SELECT 基础

```sql
-- 查询所有列
SELECT * FROM 表名;

-- 查询指定列
SELECT 列1, 列2 FROM 表名;

-- 列别名
SELECT 列名 AS 别名 FROM 表名;

-- 去重
SELECT DISTINCT 列名 FROM 表名;
```

## WHERE 条件

```sql
-- 比较运算
WHERE age > 18
WHERE name = '张三'
WHERE price != 50

-- 范围
WHERE age BETWEEN 20 AND 30
WHERE price NOT BETWEEN 10 AND 50

-- 列表
WHERE category IN ('文学', '历史')
WHERE id NOT IN (1, 2, 3)

-- 模糊匹配
WHERE name LIKE '%三%'      -- 包含
WHERE name LIKE '张%'       -- 开头
WHERE name LIKE '_三'       -- 恰好2字

-- 空值
WHERE col IS NULL
WHERE col IS NOT NULL
```

## 排序与分页

```sql
-- 排序
ORDER BY 列名 ASC           -- 升序（默认）
ORDER BY 列名 DESC          -- 降序
ORDER BY 列1 ASC, 列2 DESC  -- 多列排序

-- 分页
LIMIT 10                   -- 取前10条
LIMIT 10 OFFSET 20         -- 跳过20条，取10条
LIMIT 20, 10               -- 同上
```

## JOIN 多表

```sql
-- 内连接
SELECT * FROM A JOIN B ON A.id = B.a_id;

-- 左外连接
SELECT * FROM A LEFT JOIN B ON A.id = B.a_id;

-- 右外连接
SELECT * FROM A RIGHT JOIN B ON A.id = B.a_id;

-- 多表连接
SELECT * FROM A
  JOIN B ON A.id = B.a_id
  JOIN C ON B.id = C.b_id;
```

## 聚合函数

```sql
COUNT(*)        -- 总行数
COUNT(列名)     -- 非空行数
SUM(列名)       -- 求和
AVG(列名)       -- 平均值
MAX(列名)       -- 最大值
MIN(列名)       -- 最小值
```

## 分组统计

```sql
-- 分组
SELECT category, COUNT(*) FROM products GROUP BY category;

-- 分组 + 过滤
SELECT category, COUNT(*) AS cnt
FROM products
GROUP BY category
HAVING cnt > 5;
```

## 常用函数

```sql
-- 字符串
UPPER('abc')           -- 转大写
LOWER('ABC')           -- 转小写
LENGTH('你好')         -- 字符数
CONCAT('A', 'B')       -- 拼接
SUBSTRING('ABC', 1, 2) -- 截取

-- 数值
ROUND(3.14159, 2)      -- 四舍五入
CEIL(3.1)              -- 向上取整
FLOOR(3.9)             -- 向下取整

-- 日期
NOW()                  -- 当前时间
CURDATE()              -- 当前日期
YEAR(date)             -- 年份
MONTH(date)            -- 月份
DATEDIFF(d1, d2)       -- 日期差
```

## 条件表达式

```sql
-- IF
SELECT IF(price > 50, '贵', '便宜') FROM products;

-- CASE WHEN
SELECT
  CASE
    WHEN price < 30 THEN '便宜'
    WHEN price < 60 THEN '中等'
    ELSE '昂贵'
  END
FROM products;
```
