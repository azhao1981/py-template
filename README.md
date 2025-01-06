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
project_name/
├── src/
│   ├── project_name/
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   ├── module2.py
│   │   ├── submodule/
│   │   │   ├── __init__.py
│   │   │   ├── sub_module.py
│   │   └── ...
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   ├── test_module2.py
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_api.py
│   │   └── ...
│   └── ...
├── docs/
│   ├── conf.py
│   ├── index.rst
│   ├── modules.rst
│   └── ...
├── examples/
│   ├── example1.py
│   ├── example2.py
│   └── ...
├── data/
│   ├── input/
│   └── output/
├── scripts/
│   ├── setup_env.sh
│   ├── run_analysis.py
│   └── ...
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── setup.py
└── MANIFEST.in
```

**各部分解释：**

* **`project_name/` (顶层目录):**  这是你项目的根目录，包含所有其他文件和目录。

* **`src/` (源代码目录):**
    * **目的:**  将实际的应用程序代码与项目中的其他部分（例如测试和文档）隔离。这使得代码更容易导入和分发。
    * **结构:**  通常包含一个与项目名称相同的子目录 (`project_name/`)，这个子目录被视为一个 Python 包。
    * **`project_name/` 子目录:**
        * **`__init__.py`:**  使 `project_name` 目录成为一个 Python 包。可以为空，也可以包含包的初始化代码。
        * **模块文件 (`module1.py`, `module2.py`):**  包含你的实际 Python 代码。根据功能将代码组织成不同的模块。
        * **子包 (`submodule/`):**  用于进一步组织代码，包含自己的 `__init__.py` 文件。

* **`tests/` (测试目录):**
    * **目的:**  包含你的单元测试、集成测试和其他类型的测试。
    * **结构:**
        * **`__init__.py`:**  使 `tests` 目录成为一个 Python 包。
        * **测试模块 (`test_module1.py`, `test_module2.py`):**  通常与 `src/project_name/` 中的模块对应，包含对这些模块的测试。
        * **子目录 (`integration/`):**  用于组织特定类型的测试，例如集成测试。

* **`docs/` (文档目录):**
    * **目的:**  包含项目的文档。
    * **结构:**  通常使用 Sphinx 等文档生成工具。
        * **`conf.py`:**  Sphinx 的配置文件。
        * **`index.rst`:**  文档的入口文件。
        * **`modules.rst`:**  自动生成的模块文档。
        * **其他 `.rst` 文件:**  包含其他文档内容，例如教程、API 参考等。

* **`examples/` (示例目录):**
    * **目的:**  包含如何使用你的库或应用程序的示例代码。这对于用户理解如何使用你的项目非常有帮助。

* **`data/` (数据目录):**
    * **目的:**  包含项目运行时需要的数据文件。
    * **结构:**  可以根据数据类型或用途进一步组织，例如 `input/` 和 `output/`。

* **`scripts/` (脚本目录):**
    * **目的:**  包含用于自动化任务的脚本，例如设置环境、运行分析、部署等。

* **`.gitignore`:**  指定 Git 应该忽略的文件和目录，例如临时文件、编译后的代码等。

* **`README.md`:**  项目的入口文件，提供项目的基本信息、安装说明、使用示例等。通常使用 Markdown 格式。

* **`LICENSE`:**  项目的许可证文件，声明你的代码的使用条款。

* **`requirements.txt`:**  列出项目依赖的 Python 包及其版本。可以使用 `pip freeze > requirements.txt` 生成。

* **`pyproject.toml`:**  一种新的标准，用于声明项目的构建系统和其他元数据。常用于与 Poetry 或 Flit 等工具一起使用。

* **`setup.py`:**  用于构建、打包和安装你的项目的脚本。虽然 `pyproject.toml` 越来越流行，但 `setup.py` 仍然很常见。

* **`MANIFEST.in`:**  用于指定在打包你的项目时需要包含的其他文件（例如数据文件）。

**选择 `src` 目录的优点：**

* **清晰的分隔:**  明确区分了源代码和项目中的其他部分。
* **避免命名冲突:**  防止顶层目录下的模块与项目名称冲突。
* **易于导入:**  使得从源代码目录导入模块更加清晰和一致。

**其他一些最佳实践：**

* **保持简单:**  对于小型项目，可以简化结构。不必一开始就使用所有目录。
* **命名清晰:**  使用描述性的文件名和目录名。
* **保持一致性:**  在整个项目中保持文件和目录结构的命名约定一致。
* **模块化:**  将代码分解成小的、有凝聚力的模块和包。
* **文档化:**  编写清晰的文档，包括 README 和代码注释。
* **测试:**  编写全面的测试来确保代码的正确性。
* **使用虚拟环境:**  为每个项目创建独立的虚拟环境，以隔离依赖关系。
* **选择合适的工具:**  根据项目需求选择合适的构建、测试和文档工具。
* **迭代和适应:**  随着项目的发展，你的文件结构可能需要调整。

**不同规模的项目：**

* **小型项目/脚本:**  可能不需要 `src` 目录，可以直接在顶层目录下创建模块和脚本。
* **中型项目/库:**  建议使用 `src` 目录结构，并包含测试和文档。
* **大型项目/应用程序:**  可能需要更复杂的结构，例如将不同的应用程序部分放在单独的包中，并使用更高级的测试和部署策略。

