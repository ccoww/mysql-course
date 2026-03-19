# MySQL 环境安装指南

## Windows 安装

### 方法一：使用 MySQL Installer（推荐）

1. 下载 [MySQL Installer](https://dev.mysql.com/downloads/installer/)
2. 运行安装程序，选择 **Developer Default**
3. 设置 root 密码
4. 完成安装

### 方法二：使用 Docker（推荐开发者）

```powershell
# 安装 Docker Desktop 后运行：
docker run -d `
  --name mysql8 `
  -e MYSQL_ROOT_PASSWORD=root123 `
  -p 3306:3306 `
  mysql:8.0

# 连接：
# Host: localhost
# Port: 3306
# User: root
# Password: root123
```

## macOS 安装

### 使用 Homebrew

```bash
# 安装
brew install mysql
brew services start mysql

# 安全配置
mysql_secure_installation

# 连接
mysql -u root -p
```

## Linux 安装

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo mysql_secure_installation
```

## 客户端工具推荐

| 工具 | 平台 | 特点 |
|------|------|------|
| [MySQL Workbench](https://www.mysql.com/products/workbench/) | 官方 GUI | 功能全，跨平台 |
| [DBeaver](https://dbeaver.io/) | 免费开源 | 支持多种数据库 |
| [DataGrip](https://www.jetbrains.com/datagrip/) | 付费 | 强大，适合专业开发者 |
| 命令行 mysql | 终端 | 轻量，快捷 |

## 验证安装

```bash
# 命令行连接
mysql -u root -p

# 查看版本
SELECT VERSION();

# 查看数据库
SHOW DATABASES;
```

## 常见问题

### Q: 忘记 root 密码怎么办？

```bash
# 1. 停止 MySQL 服务
# 2. 以安全模式启动
mysqld --skip-grant-tables

# 3. 另开终端，无密码登录
mysql -u root

# 4. 重置密码
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码';
```

### Q: 连接报错 "Access denied"？

- 检查用户名、密码是否正确
- 确认 MySQL 服务已启动
- 检查防火墙是否阻止 3306 端口
