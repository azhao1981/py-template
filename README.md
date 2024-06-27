# py-template

## env

uv + poetry

### 安装 uv

下载 https://github.com/astral-sh/uv/releases

```bash
which uv
```

### 安装 poetry

https://python-poetry.org/docs/ 官方的要求是建在虚拟环境中，以防止异常升级造成环境破坏。

```bash
# 配置
cp .env.example .env

build.sh
# 载入环境
. .env
# 验证
which poetry

# 添加依赖:
poetry add requests

# 运行
poetry run python main.py
```

### 项目结构:
```
my_project/
├── poetry.toml
├── pyproject.toml
└── main.py
```
