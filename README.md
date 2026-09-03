# Playwright+Pytest自动化测试项目
> UI自动化测试项目，基于Playwright、pytest、allure‑pytest实现Web端自动化测试，覆盖SauceDemo页面UI与Reqres接口测试。

## 🛠技术栈
- Python 3.10
- Playwright：Web页面自动化
- pytest：测试执行框架
- pytest‑playwright：pytest与playwright集成
- allure‑pytest：生成可视化测试报告

## ✨项目特性
1. **用例分组管理**：使用pytest mark实现smoke冒烟用例、regression回归用例分组，支持不同场景选择性执行。
2. **数据驱动测试**：`@pytest.mark.parametrize`实现登录场景多组输入，覆盖正常账号、错误账号、空输入场景。
3. **失败自动收集现场**：基于pytest_runtest_makereport钩子捕获用例失败，自动采集页面URL、全屏截图、机器公网IP，存入Allure报告，辅助定位缺陷。
4. 同时支持UI自动化测试 + HTTP接口测试。
5. Allure可视化报告展示用例执行状态、执行时长、附件信息。
6. GitHub Actions CI流水线：push代码自动执行测试，上传Allure结果制品。

## 📂项目目录
Playwright‑Python‑Example
├── api/                #接口测试用例
├── tests/              #UI 测试用例
├── src/                #页面对象 PO 模型封装
├── .github/workflows/  #GitHub Actions CI 配置
├── conftest.py         #pytest 钩子、全局 fixture
├── pytest.ini          #pytest 配置，自定义 mark 标记
└── requirements.txt    #依赖清单

## 🚀运行步骤
```bash
#创建虚拟环境
python -m venv venv
source venv/Scripts/activate

#安装依赖
pip install -r requirements.txt
playwright install

#执行全部用例，生成allure结果
pytest --alluredir=allure‑results

#启动allure报告
allure serve allure‑results

#只运行冒烟用例
pytest -m smoke -v

#只运行回归用例
pytest -m regression -v
