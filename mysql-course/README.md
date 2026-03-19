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
