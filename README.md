# MySQL 数据库查询实战系列课程

> 面向零基础学员 | 3 节课共 270 分钟 | MySQL 8.0

## 本系列课程学完你能做什么

| 课程 | 主要内容 | 学完能做什么 |
|------|----------|--------------|
| 第1课 | SELECT 基础查询 | 能从单表中查询想要的数据 |
| 第2课 | JOIN 多表查询 | 能从多关联表中获取数据 |
| 第3课 | 聚合统计与分组 | 能对数据进行汇总分析 |

## 课程特色

- **案例驱动**：全程使用电商数据库，贴近真实业务
- **循序渐进**：从简单查询到复杂统计，步步深入
- **配套完善**：讲义 + 案例代码 + 练习题 + 参考答案

## 文件结构

```
mysql-course/
├── README.md                    # 本文件
├── 01-select/                   # 第1课：SELECT基础
│   ├── outline.md
│   ├── lecture.md
│   ├── exercises.md
│   ├── answers.md
│   └── demo.sql
├── 02-join/                     # 第2课：JOIN多表查询
│   ├── outline.md
│   ├── lecture.md
│   ├── exercises.md
│   ├── answers.md
│   └── demo.sql
├── 03-aggregate/                # 第3课：聚合统计
│   ├── outline.md
│   ├── lecture.md
│   ├── exercises.md
│   ├── answers.md
│   └── demo.sql
├── data/                        # 公共数据库（3课共用）
│   ├── schema.sql
│   ├── seed_data.sql
│   └── queries.sql              # 综合业务查询
└── docs/                        # 附录文档
    ├── environment.md           # 环境安装指南
    └── cheat-sheet.md          # SQL 速查表
```

## 快速开始

```bash
# 1. 安装 MySQL 8.0（见 docs/environment.md）

# 2. 导入数据库
mysql -u root -p < data/schema.sql
mysql -u root -p < data/seed_data.sql

# 3. 开始学习第1课
#    打开 01-select/lecture.md
```

## 案例数据库：电商平台

本系列使用统一的**电商数据库**（`ecommerce`），包含 6 张表：

| 表名 | 说明 | 记录数 |
|------|------|--------|
| users | 用户 | 10 |
| categories | 商品分类 | 8 |
| products | 商品 | 30 |
| orders | 订单 | 20 |
| order_items | 订单明细 | 50 |
| products | 商品评论 | 30 |

## 学习路径建议

```
第1课 SELECT基础（90分钟）
    ↓
第2课 JOIN多表（90分钟）
    ↓
第3课 聚合统计（90分钟）
```

每节课相互独立，也可按需选择学习。

## 参考资源

- [MySQL 官方文档](https://dev.mysql.com/doc/)
- [W3Schools SQL 教程](https://www.w3schools.com/sql/)

---

**作者**：CCOWW
**更新日期**：2026年3月
