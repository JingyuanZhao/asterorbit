# Hugging Face Spaces 部署指南

## 已创建的文件

### 1. spaces_config.json
Hugging Face Spaces 配置文件，指定使用 Docker 部署方式。

### 2. Dockerfile
Docker 容器配置，用于构建和运行 Flask 应用。

### 3. requirements.txt（已有）
包含所有 Python 依赖。

## 部署步骤

### 方法一：通过 Git 上传（推荐）

1. **初始化 Git 仓库**（如果还没有）：
   ```bash
   git init
   git add .
   git commit -m "添加 Hugging Face Spaces 配置"
   ```

2. **推送代码到 Hugging Face**：
   ```bash
   # 添加远程仓库
   git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/digest2-asteroid-classifier

   # 推送代码
   git push -u origin main
   ```

### 方法二：通过网页上传

1. 访问 [Hugging Face Spaces](https://huggingface.co/new-space)
2. 选择 "Docker" SDK
3. 上传以下文件：
   - `app.py`
   - `requirements.txt`
   - `Dockerfile`
   - `templates/` 目录
   - `ObsCodes.html`
4. 填写 Space 名称和配置

## 部署验证

部署成功后，应用将在以下地址可用：
```
https://YOUR_USERNAME-digest2-asteroid-classifier.hf.space
```

## 功能说明

部署后的应用包含 4 个页面：

1. **类型评估** (`/`) - 主页面，输入观测数据进行分析
2. **类型说明** (`/types`) - 轨道类型说明
3. **下载** (`/download`) - 下载桌面版本
4. **关于** (`/about`) - 关于项目信息

## 注意事项

- Hugging Face Spaces 的免费版有 CPU 限制
- 如果遇到构建问题，检查 Dockerfile 是否正确
- 确保 `digest2==2.8.0` 包在 Docker 环境中可以正常安装
