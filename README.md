# Playwright‑Pytest 自动化测试项目
> Web UI自动化 + 接口自动化测试，基于PO页面对象模型，Allure可视化测试报告

## 🛠技术栈
- Python 3.10
- pytest 测试框架
- pytest‑playwright UI自动化
- Allure‑pytest 测试报告
- PO（Page Object）页面对象设计模式

## 📁项目目录
├── api                 # 接口测试用例
├── src
│  │ 
│  └── pages           # PO 页面对象封装
├── tests               # UI 自动化测试用例
├── conftest.py         # pytest 全局 fixture 钩子
├── pytest.ini          # pytest 配置文件
├── requirements.txt    # 项目依赖
└── .gitignore


## 运行步骤
1. 创建虚拟环境
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
playwright install chromium
```

2. 执行全部用例
```
pytest
```

3. 预览 allure 报告

```
allure serve allure-results
```

## 用例说明

- UI 用例：2 条，saucedemo 登录、添加购物车业务场景
- 接口用例：2 条，reqres 接口测试

## 报告效果

Allure 报告包含用例执行统计、运行环境信息。

```

保存，执行git提交推送：
```bash
git add README.md
git commit -m "docs: 添加项目README文档"
git push
```