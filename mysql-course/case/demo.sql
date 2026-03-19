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
