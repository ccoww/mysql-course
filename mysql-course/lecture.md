# 讲义：SQL 入门 —— 用 SELECT 查询数据

---

## 第一部分：数据库是什么？（10 分钟）

### 从 Excel 说起

你用过 Excel 吗？一张 Excel 表格就长这样：

| 书名 | 作者 | 价格 | 库存 |
|------|------|------|------|
| 活着 | 余华 | 39.00 | 120 |
| 白夜行 | 东野圭吾 | 52.00 | 85 |

数据库里的**表（Table）** 和这个几乎一样，只是：

- 数据量可以到几亿行（Excel 撑不住）
- 多张表可以互相关联
- 可以用 SQL 语言快速找到你要的数据

### 几个核心概念

| 概念 | 通俗理解 | 举例 |
|------|----------|------|
| **数据库（Database）** | 一个文件夹，装着很多表 | `bookstore`（书店数据库）|
| **表（Table）** | 一张 Excel 表格 | `books`（图书表）|
| **行（Row）** | 表格里的一条记录 | 一本书的信息 |
| **列（Column）** | 表格里的一个字段 | `price`（价格）|
| **主键（Primary Key）** | 每行的唯一编号 | `id`（自动递增） |

### SQL 是什么

SQL（Structured Query Language，结构化查询语言）就是和数据库"对话"的语言。

今天学的 `SELECT` 就是在问数据库：**"请给我看这些数据"**。

---

## 第二部分：认识今天的案例数据（10 分钟）

### 在线书店数据库

我们用一个**在线书店**的数据库来练习，里面有两张表。

**图书表 `books`**

```
id | title        | author_id | category | price | stock | published_year | is_available
---+--------------+-----------+----------+-------+-------+----------------+-------------
 1 | 活着          |     1     | 文学      | 39.00 |  120  |     1993       |     1
 2 | 白夜行        |     2     | 悬疑      | 52.00 |   85  |     1999       |     1
...
```

**作者表 `authors`**

```
id | name     | country | born_year
---+----------+---------+----------
 1 | 余华      | 中国     |  1960
 2 | 东野圭吾  | 日本     |  1958
...
```

### 先把数据导进去

```sql
-- 在你的 MySQL 客户端里执行：
SOURCE /path/to/case/schema.sql;
SOURCE /path/to/case/seed_data.sql;

-- 切换到书店数据库
USE bookstore;

-- 看看有哪些表
SHOW TABLES;

-- 看看 books 表的结构
DESCRIBE books;
```

---

## 第三部分：SELECT 基础（15 分钟）

### 3.1 查询所有列

语法：
```sql
SELECT * FROM 表名;
```

`*` 是通配符，意思是"所有列"。

```sql
-- 查询全部图书
SELECT * FROM books;
```

> 实际工作中尽量少用 `SELECT *`，指定列名更规范、性能更好。

---

### 3.2 查询指定列

语法：
```sql
SELECT 列1, 列2, 列3 FROM 表名;
```

```sql
-- 只看书名和价格
SELECT title, price FROM books;

-- 看书名、分类、库存
SELECT title, category, stock FROM books;
```

---

### 3.3 列别名（AS）

有时列名太长或不直观，可以起个别名：

```sql
SELECT
    title       AS 书名,
    price       AS 售价,
    stock       AS 库存数量
FROM books;
```

`AS` 可以省略，但加上更清晰：
```sql
SELECT title 书名, price 售价 FROM books;  -- 效果相同
```

---

### 3.4 去除重复值（DISTINCT）

```sql
-- 书有哪些分类（去掉重复）
SELECT DISTINCT category FROM books;

-- 有哪些出版年份
SELECT DISTINCT published_year FROM books ORDER BY published_year;
```

---

### 小结：SELECT 基础语法

```sql
SELECT [DISTINCT] 列名1, 列名2, ...
FROM 表名;
```

---

## 第四部分：WHERE 过滤数据（20 分钟）

> WHERE 就像一个筛子，只留下满足条件的行。

### 4.1 比较运算符

| 运算符 | 含义 | 示例 |
|--------|------|------|
| `=` | 等于 | `price = 39.00` |
| `!=` 或 `<>` | 不等于 | `category != '文学'` |
| `>` | 大于 | `price > 50` |
| `>=` | 大于等于 | `stock >= 100` |
| `<` | 小于 | `published_year < 2000` |
| `<=` | 小于等于 | `price <= 30` |

```sql
-- 价格超过 50 元的书
SELECT title, price FROM books WHERE price > 50;

-- 文学类图书
SELECT title, category FROM books WHERE category = '文学';

-- 不是文学类的书
SELECT title, category FROM books WHERE category != '文学';
```

---

### 4.2 逻辑运算符（AND / OR / NOT）

```sql
-- 文学类 且 价格低于 50 元
SELECT title, category, price
FROM books
WHERE category = '文学' AND price < 50;

-- 文学类 或 悬疑类
SELECT title, category
FROM books
WHERE category = '文学' OR category = '悬疑';

-- 不是文学类
SELECT title, category
FROM books
WHERE NOT category = '文学';
```

> **注意优先级**：`AND` 优先级高于 `OR`，不确定时加括号。
> ```sql
> -- 以下两句含义不同！
> WHERE category = '文学' OR category = '悬疑' AND price > 40
> WHERE (category = '文学' OR category = '悬疑') AND price > 40
> ```

---

### 4.3 范围查询（BETWEEN）

```sql
-- 价格在 30 到 60 元之间（含两端）
SELECT title, price
FROM books
WHERE price BETWEEN 30 AND 60;

-- 等价写法
WHERE price >= 30 AND price <= 60
```

---

### 4.4 列表查询（IN）

```sql
-- 分类是文学、历史或科普的书
SELECT title, category
FROM books
WHERE category IN ('文学', '历史', '科普');

-- 查询指定 id 的书
SELECT * FROM books WHERE id IN (1, 3, 5, 7);

-- NOT IN：排除某些值
SELECT title, category
FROM books
WHERE category NOT IN ('文学', '悬疑');
```

---

### 4.5 模糊查询（LIKE）

| 通配符 | 含义 | 示例 |
|--------|------|------|
| `%` | 任意个任意字符 | `'%传%'` 含"传"字 |
| `_` | 恰好一个任意字符 | `'三_'` 两字以"三"开头 |

```sql
-- 书名含"三"字的书
SELECT title FROM books WHERE title LIKE '%三%';

-- 书名以"白"开头
SELECT title FROM books WHERE title LIKE '白%';

-- 书名以"记"结尾
SELECT title FROM books WHERE title LIKE '%记';

-- 书名恰好是两个字（两个下划线）
SELECT title FROM books WHERE title LIKE '__';
```

---

### 4.6 空值判断（IS NULL）

```sql
-- 查询没有填写出版年份的书
SELECT title FROM books WHERE published_year IS NULL;

-- 查询已填写出版年份的书
SELECT title, published_year FROM books WHERE published_year IS NOT NULL;
```

> ⚠️ 注意：不能用 `= NULL`，必须用 `IS NULL`。
> ```sql
> WHERE published_year = NULL    -- 错误，永远查不出数据！
> WHERE published_year IS NULL   -- 正确
> ```

---

### 小结：WHERE 条件速查

```
WHERE price > 50              -- 比较
WHERE price BETWEEN 30 AND 60 -- 范围（含两端）
WHERE category IN ('文学','悬疑') -- 列表
WHERE title LIKE '%三%'       -- 模糊匹配
WHERE published_year IS NULL  -- 判断空值
WHERE 条件1 AND 条件2         -- 同时满足
WHERE 条件1 OR  条件2         -- 满足其一
```

---

## 第五部分：排序与分页（10 分钟）

### 5.1 ORDER BY 排序

```sql
-- 按价格从低到高（升序，默认）
SELECT title, price FROM books ORDER BY price ASC;

-- 按价格从高到低（降序）
SELECT title, price FROM books ORDER BY price DESC;

-- 先按分类升序，同分类内再按价格降序
SELECT title, category, price
FROM books
ORDER BY category ASC, price DESC;
```

---

### 5.2 LIMIT 限制条数

```sql
-- 只看前 5 条
SELECT title, price FROM books ORDER BY price DESC LIMIT 5;

-- 跳过前 5 条，再取 5 条（用于翻页，第 2 页）
SELECT title, price FROM books ORDER BY price DESC LIMIT 5 OFFSET 5;

-- 简写形式：LIMIT 跳过条数, 取几条
SELECT title, price FROM books ORDER BY price DESC LIMIT 5, 5;
```

**翻页计算公式：**
```
OFFSET = (页码 - 1) × 每页条数
第1页：LIMIT 10 OFFSET 0
第2页：LIMIT 10 OFFSET 10
第3页：LIMIT 10 OFFSET 20
```

---

### 完整查询语句结构

```sql
SELECT  [DISTINCT] 列名
FROM    表名
WHERE   过滤条件
ORDER BY 列名 [ASC|DESC]
LIMIT   条数 [OFFSET 偏移量];
```

> **执行顺序**（和书写顺序不同！）：
> FROM → WHERE → SELECT → ORDER BY → LIMIT

---

## 第六部分：常用函数（10 分钟）

### 6.1 字符串函数

```sql
SELECT
    title,
    LENGTH(title)               AS 字符数,
    UPPER(title)                AS 转大写,
    LOWER(title)                AS 转小写,
    CONCAT(title, ' | ', category) AS 拼接结果,
    SUBSTRING(title, 1, 4)      AS 取前4字符,
    TRIM('  你好  ')             AS 去首尾空格
FROM books;
```

---

### 6.2 数值函数

```sql
SELECT
    price,
    ROUND(price, 0)    AS 四舍五入到整数,
    CEIL(price)        AS 向上取整,
    FLOOR(price)       AS 向下取整,
    ABS(-price)        AS 绝对值,
    price * 0.8        AS 八折价格
FROM books;
```

---

### 6.3 日期函数

```sql
SELECT
    NOW()                           AS 当前日期时间,
    CURDATE()                       AS 今天日期,
    YEAR(NOW())                     AS 今年年份,
    YEAR(NOW()) - published_year    AS 出版至今年数,
    DATE_FORMAT(NOW(), '%Y年%m月%d日') AS 格式化日期
FROM books
WHERE published_year IS NOT NULL;
```

---

### 6.4 条件函数（IF / CASE WHEN）

```sql
-- IF(条件, 真时返回, 假时返回)
SELECT
    title,
    price,
    IF(price > 50, '贵', '实惠')  AS 价格评价
FROM books;

-- CASE WHEN（多条件）
SELECT
    title,
    price,
    CASE
        WHEN price < 30           THEN '平价'
        WHEN price BETWEEN 30 AND 60 THEN '中等'
        ELSE                           '高价'
    END AS 价格档次
FROM books;
```

---

## 第七部分：课堂练习（15 分钟）

> 请独立完成以下 5 题，然后和同学对照答案。

**题 1：** 查询所有"悬疑"类图书的书名和价格，按价格从低到高排序。

**题 2：** 查询库存大于 80 本 且 价格低于 50 元的图书，显示书名、库存、价格。

**题 3：** 查询书名中含有"的"字的图书，只显示书名和分类。

**题 4：** 查询 2000 年以后出版的图书，显示书名和出版年份，按出版年份降序，只取前 5 条。

**题 5：** 查询所有图书，显示书名、原价、九折后的价格（列名叫"折后价"，保留2位小数），按折后价升序排序。

> 完整参考答案见 `answers.md`
