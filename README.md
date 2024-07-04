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
# 配置, 并且修改 python 位置
cp .env.example .env

# 初始化项目
build.sh

# 载入环境
. .env
# 验证
which poetry

# 添加依赖:
poetry add requests

# 运行
poetry run python main.py

# 打包
poetry build

# 制作 requirements.txt
uv pip freeze >> requirements.txt
```

### 项目结构:
```
my_project/
├── poetry.toml
├── pyproject.toml
└── main.py
```
