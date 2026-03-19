#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MySQL 单节课内容生成器
面向零基础学员，90分钟，主题：SQL 入门 SELECT 基础查询
"""

import pathlib

DESKTOP = pathlib.Path.home() / "Desktop"
ROOT = DESKTOP / "mysql-course"

FILES = {}

# ============================================================
# README.md
# ============================================================
FILES["README.md"] = """\
# MySQL 入门：第一次写 SELECT 查询

> 面向零基础学员 | 课时：90 分钟 | MySQL 8.0

## 本节课学完你能做什么

- 看懂一张数据库表的结构
- 用 SELECT 查询你想要的数据
- 用 WHERE 过滤、ORDER BY 排序、LIMIT 控制条数
- 用常见函数处理字符串和日期
- 独立完成本节课全部 10 道练习题

## 文件说明

| 文件 | 内容 |
|------|------|
| `outline.md` | 课程大纲（90分钟时间分配） |
| `lecture.md` | 完整讲义（含所有示例代码） |
| `case/schema.sql` | 案例建表语句 |
| `case/seed_data.sql` | 案例测试数据 |
| `case/demo.sql` | 课堂演示查询 |
| `exercises.md` | 课后练习题（10题） |
| `answers.md` | 参考答案 |

## 快速开始

```bash
# 1. 建表并导入数据
mysql -u root -p < case/schema.sql
mysql -u root -p < case/seed_data.sql

# 2. 打开 lecture.md 开始学习
# 3. 完成 exercises.md 中的练习
```

## 环境要求

- MySQL 8.0+（或 MariaDB 10.5+）
- 任意客户端：MySQL Workbench / DBeaver / 命令行均可
"""

# ============================================================
# outline.md —— 单节课大纲
# ============================================================
FILES["outline.md"] = """\
# 课程大纲

**主题：** SQL 入门 —— 用 SELECT 查询数据
**面向：** 零基础学员
**时长：** 90 分钟

---

## 时间分配

| 时段 | 时长 | 内容 | 形式 |
|------|------|------|------|
| 0:00 - 0:10 | 10 分钟 | **导入：数据库是什么？** 用日常例子引出概念 | 讲解 |
| 0:10 - 0:20 | 10 分钟 | **认识表结构**：行、列、主键；导入案例数据 | 演示 |
| 0:20 - 0:35 | 15 分钟 | **SELECT 基础**：查所有列、查指定列、列别名 | 讲解 + 跟练 |
| 0:35 - 0:55 | 20 分钟 | **WHERE 过滤**：比较、BETWEEN、IN、LIKE、IS NULL | 讲解 + 跟练 |
| 0:55 - 1:05 | 10 分钟 | **排序与分页**：ORDER BY、LIMIT | 讲解 + 跟练 |
| 1:05 - 1:15 | 10 分钟 | **常用函数**：字符串、日期、数值 | 演示 |
| 1:15 - 1:30 | 15 分钟 | **课堂练习**：独立完成 5 道练习题 + 讲评 | 练习 |

---

## 教学目标

学完本节课，学员能够：

1. 说出"数据库、表、行、列"各自是什么意思
2. 写出 `SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT` 完整语句
3. 用 6 种 WHERE 条件筛选数据
4. 用 3 类常用函数处理查询结果

## 不在本节课范围内

- 多表 JOIN 查询（下节课）
- 聚合函数 GROUP BY（第三节课）
- 增删改数据（INSERT / UPDATE / DELETE）
- 索引、事务、存储过程

---

## 案例数据库

本节课使用 **在线书店** 数据库（`bookstore`），包含两张表：

- `books`（图书）：25 条记录
- `authors`（作者）：10 条记录

> 场景贴近生活，字段简单，便于零基础学员理解。
"""

# ============================================================
# lecture.md —— 完整讲义
# ============================================================
FILES["lecture.md"] = """\
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
"""

# ============================================================
# case/schema.sql
# ============================================================
FILES["case/schema.sql"] = """\
-- ============================================================
-- 在线书店数据库 Schema
-- MySQL 8.0+
-- ============================================================

DROP DATABASE IF EXISTS bookstore;
CREATE DATABASE bookstore
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE bookstore;

-- 作者表
CREATE TABLE authors (
    id          INT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50)     NOT NULL,
    country     VARCHAR(30)     NOT NULL DEFAULT '中国',
    born_year   YEAR
) ENGINE=InnoDB;

-- 图书表
CREATE TABLE books (
    id              INT UNSIGNED    AUTO_INCREMENT PRIMARY KEY,
    title           VARCHAR(100)    NOT NULL,
    author_id       INT UNSIGNED    NOT NULL,
    category        VARCHAR(20)     NOT NULL,
    price           DECIMAL(8,2)    NOT NULL CHECK (price > 0),
    stock           INT             NOT NULL DEFAULT 0,
    published_year  YEAR,
    is_available    BOOLEAN         NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_books_author
        FOREIGN KEY (author_id) REFERENCES authors(id)
) ENGINE=InnoDB;
"""

# ============================================================
# case/seed_data.sql
# ============================================================
FILES["case/seed_data.sql"] = """\
USE bookstore;

-- 作者数据
INSERT INTO authors (id, name, country, born_year) VALUES
( 1, '余华',       '中国', 1960),
( 2, '东野圭吾',   '日本', 1958),
( 3, '刘慈欣',     '中国', 1963),
( 4, '张爱玲',     '中国', 1920),
( 5, '村上春树',   '日本', 1949),
( 6, '路遥',       '中国', 1949),
( 7, '陀思妥耶夫斯基', '俄罗斯', 1821),
( 8, '加西亚·马尔克斯', '哥伦比亚', 1927),
( 9, '毛姆',       '英国', 1874),
(10, '三毛',       '中国', 1943);

-- 图书数据（25 本）
INSERT INTO books (id, title, author_id, category, price, stock, published_year, is_available) VALUES
( 1, '活着',              1, '文学',   39.00, 120, 1993, TRUE),
( 2, '许三观卖血记',      1, '文学',   35.00,  98, 1995, TRUE),
( 3, '白夜行',            2, '悬疑',   52.00,  85, 1999, TRUE),
( 4, '解忧杂货店',        2, '悬疑',   45.00, 210, 2012, TRUE),
( 5, '三体',              3, '科幻',   68.00, 300, 2008, TRUE),
( 6, '三体II：黑暗森林',  3, '科幻',   72.00, 250, 2008, TRUE),
( 7, '三体III：死神永生', 3, '科幻',   72.00, 230, 2010, TRUE),
( 8, '倾城之恋',          4, '文学',   28.00,  60, 1943, TRUE),
( 9, '挪威的森林',        5, '文学',   48.00, 175, 1987, TRUE),
(10, '海边的卡夫卡',      5, '文学',   55.00, 140, 2002, TRUE),
(11, '平凡的世界（全三册）',6,'文学',  98.00,  45, 1986, TRUE),
(12, '罪与罚',            7, '文学',   49.00,  30, 1866, TRUE),
(13, '卡拉马佐夫兄弟',    7, '文学',   88.00,  20, 1880, TRUE),
(14, '百年孤独',          8, '文学',   65.00, 180, 1967, TRUE),
(15, '霍乱时期的爱情',    8, '文学',   58.00,  90, 1985, TRUE),
(16, '月亮和六便士',      9, '文学',   36.00, 200, 1919, TRUE),
(17, '刀锋',              9, '文学',   42.00, 155, 1944, TRUE),
(18, '撒哈拉的故事',     10, '散文',   32.00, 125, 1976, TRUE),
(19, '雨季不再来',        10, '散文',   29.00,  70, 1976, TRUE),
(20, '嫌疑人X的献身',     2, '悬疑',   43.00, 190, 2005, TRUE),
(21, '流浪地球',          3, '科幻',   35.00, 280, 2000, TRUE),
(22, '时间简史',          NULL, '科普', 55.00, 110, 1988, TRUE),  -- 演示 NULL
(23, '自私的基因',        NULL, '科普', 62.00,  50, 1976, TRUE),  -- 演示 NULL
(24, '苏菲的世界',        NULL, '哲学', 48.00,  40, 1991, FALSE), -- is_available=FALSE
(25, '菊与刀',            NULL, '历史', 38.00,  75, 1946, TRUE);
"""

# ============================================================
# case/demo.sql —— 课堂演示查询
# ============================================================
FILES["case/demo.sql"] = """\
USE bookstore;

-- ============================================================
-- 课堂演示：跟着讲义一步步运行
-- ============================================================

-- [第三部分] SELECT 基础
-- 3.1 查询所有列
SELECT * FROM books;

-- 3.2 查询指定列
SELECT title, price FROM books;
SELECT title, category, stock FROM books;

-- 3.3 列别名
SELECT
    title    AS 书名,
    price    AS 售价,
    stock    AS 库存数量
FROM books;

-- 3.4 去重
SELECT DISTINCT category FROM books;


-- ============================================================
-- [第四部分] WHERE 过滤
-- ============================================================

-- 4.1 比较运算符
SELECT title, price FROM books WHERE price > 50;
SELECT title, category FROM books WHERE category = '文学';
SELECT title, category FROM books WHERE category != '文学';

-- 4.2 逻辑运算符
SELECT title, category, price
FROM books
WHERE category = '文学' AND price < 50;

SELECT title, category
FROM books
WHERE category = '文学' OR category = '悬疑';

-- 4.3 BETWEEN
SELECT title, price
FROM books
WHERE price BETWEEN 30 AND 60;

-- 4.4 IN
SELECT title, category
FROM books
WHERE category IN ('文学', '历史', '科普');

-- 4.5 LIKE
SELECT title FROM books WHERE title LIKE '%三%';
SELECT title FROM books WHERE title LIKE '白%';
SELECT title FROM books WHERE title LIKE '%记';

-- 4.6 IS NULL
SELECT title FROM books WHERE author_id IS NULL;
SELECT title, author_id FROM books WHERE author_id IS NOT NULL;


-- ============================================================
-- [第五部分] 排序与分页
-- ============================================================

-- ORDER BY
SELECT title, price FROM books ORDER BY price ASC;
SELECT title, price FROM books ORDER BY price DESC;
SELECT title, category, price
FROM books
ORDER BY category ASC, price DESC;

-- LIMIT
SELECT title, price FROM books ORDER BY price DESC LIMIT 5;

-- 翻页：第2页（每页5条）
SELECT title, price FROM books ORDER BY price DESC LIMIT 5 OFFSET 5;


-- ============================================================
-- [第六部分] 常用函数
-- ============================================================

-- 字符串函数
SELECT
    title,
    LENGTH(title)                    AS 字符数,
    CONCAT(title, ' [', category, ']') AS 书名分类
FROM books;

-- 数值函数
SELECT
    title,
    price,
    ROUND(price * 0.8, 2)  AS 八折价
FROM books;

-- 日期函数
SELECT
    title,
    published_year,
    YEAR(NOW()) - published_year AS 出版距今年数
FROM books
WHERE published_year IS NOT NULL
ORDER BY published_year;

-- CASE WHEN
SELECT
    title,
    price,
    CASE
        WHEN price < 30               THEN '平价'
        WHEN price BETWEEN 30 AND 60  THEN '中等'
        ELSE                               '高价'
    END AS 价格档次
FROM books
ORDER BY price;
"""

# ============================================================
# exercises.md —— 课后练习（10 题）
# ============================================================
FILES["exercises.md"] = """\
# 课后练习题

**数据库：** `bookstore`  **表：** `books` / `authors`

---

### 第一组：SELECT 基础（2 题）

**题 1**
查询所有图书的书名（title）、分类（category）和价格（price），
价格列显示为别名"售价"。

**题 2**
查询图书表中共有哪几种分类（不重复），按分类名称升序排列。

---

### 第二组：WHERE 过滤（4 题）

**题 3**
查询所有"科幻"类图书的书名、价格和库存，按价格从低到高排列。

**题 4**
查询价格在 40 到 70 元之间（含两端）、且库存大于 100 本的图书，
显示书名、价格、库存。

**题 5**
查询书名中含有"的"字，或者分类为"散文"的图书，
显示书名和分类，去掉重复行。

**题 6**
查询 `author_id` 为空（即 author_id IS NULL）的图书，
显示书名和分类。

---

### 第三组：排序与分页（2 题）

**题 7**
查询所有"文学"类图书，按出版年份从早到晚排序，
若出版年份相同则按价格升序排，只显示前 5 条。

**题 8**
查询价格最贵的第 3 ~ 5 名图书（共 3 条），
显示书名和价格（提示：先按价格降序，再用 LIMIT + OFFSET）。

---

### 第四组：函数应用（2 题）

**题 9**
查询所有图书，显示书名、原价、九折价格（ROUND 保留 2 位小数，
列名叫"折后价"），按折后价从低到高排序。

**题 10（挑战题）**
查询所有图书，用 CASE WHEN 将价格分为三档：
- 低于 35 元：'经济实惠'
- 35 ~ 60 元：'性价比高'
- 超过 60 元：'高端精品'

同时用 CASE WHEN 判断库存状态：
- 库存 < 50：'库存紧张'
- 50 ~ 150：'库存正常'
- 超过 150：'库存充足'

显示书名、价格、价格档次、库存、库存状态，按价格升序排列。

---

> 参考答案见 `answers.md`
"""

# ============================================================
# answers.md —— 参考答案
# ============================================================
FILES["answers.md"] = """\
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
"""

# ============================================================
# 生成脚本主逻辑
# ============================================================

def create_file(rel_path: str, content: str):
    abs_path = ROOT / rel_path
    abs_path.parent.mkdir(parents=True, exist_ok=True)
    abs_path.write_text(content, encoding="utf-8")
    print(f"  [OK] {rel_path}")


def main():
    print(f"\n[INFO] 目标目录：{ROOT}\n")
    ROOT.mkdir(parents=True, exist_ok=True)

    for rel_path, content in FILES.items():
        create_file(rel_path, content)

    print(f"\n[DONE] 共生成 {len(FILES)} 个文件")
    print(f"[PATH] {ROOT}")


if __name__ == "__main__":
    main()
