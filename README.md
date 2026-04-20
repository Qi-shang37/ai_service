# AI 情感分析推理服务

基于 FastAPI + Redis + MySQL + HuggingFace Transformers 构建的高性能情感分析 API 服务。支持文本情感极性判断（正面/负面），具备 Redis 缓存加速和 MySQL 请求日志持久化功能。

## ✨ 特性

- 🚀 **高性能异步 API**：基于 FastAPI 构建，自动生成交互式文档（Swagger UI）
- 🧠 **开箱即用的情感分析**：集成 `distilbert-base-uncased-finetuned-sst-2-english` 模型，无需训练
- ⚡ **Redis 缓存**：相同文本重复请求毫秒级响应，大幅降低推理负载
- 📊 **请求日志**：所有调用记录自动存入 MySQL，便于审计和分析
- 🐳 **易于部署**：提供完整的安装和运行指南，支持 Docker（可选）

## 🛠️ 技术栈

- **Python 3.10**
- **FastAPI** – Web 框架
- **Transformers** – 加载预训练模型
- **Redis** – 缓存
- **MySQL** – 日志存储
- **Uvicorn** – ASGI 服务器

## 📦 安装与运行

### 前提条件

- Python 3.10+
- MySQL 8.0+（已创建数据库和表）
- Redis 5.0+

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/ai-inference-service.git
cd ai-inference-service
