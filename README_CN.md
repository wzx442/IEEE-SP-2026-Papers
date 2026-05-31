# IEEE S&P 2026 论文抓取与分类工具

通过 IEEE CSDL GraphQL API 获取 IEEE S&P 2026 会议全部 199 篇论文，使用 DeepSeek AI 将论文归类到 12 个大类和具体子领域，生成结构化的 Markdown 文件。

无需浏览器、Playwright 或手动操作 —— 纯 API 流水线。

## 环境配置

```bash
pip install -r requirements.txt
cp .env.example .env         # 编辑 .env 填入你的 DeepSeek API Key
```

## 使用方式

```bash
python main.py                  # 完整流程（抓取 + 分类 + 输出）
python main.py --fetch-only     # 仅从 GraphQL API 抓取论文数据
python main.py --classify-only  # 仅分类（从 data/papers.json 缓存读取）
python main.py --output-only    # 仅生成 Markdown（从 data/classified.json 缓存读取）
python main.py --force          # 强制重新抓取和分类，忽略缓存
```

## 工作流程

1. **抓取**：调用 IEEE CSDL GraphQL API（`https://www.computer.org/csdl/api/v1/graphql`），一次请求获取全部 199 篇论文的标题、摘要、作者和 DOI
2. **分类**：通过 DeepSeek API 对每篇论文进行两级分类 —— 大类（如 "Cryptography and Privacy"、"LLMs and AI Safety" 等）和具体子领域（如 "Federated Learning"、"LLM Jailbreaking" 等）
3. **输出**：生成 `output/SP2026.md`，一级标题为 "IEEE S&P 2026"，二级标题为研究大类，每个大类下是两列表格（论文名+链接 | 子领域），末尾附统计信息

## 项目结构

```
sp2026-scraper/
├── main.py               # 入口：编排完整流程
├── fetcher.py             # GraphQL API 数据获取
├── classifier.py          # DeepSeek API 分类
├── output.py              # Markdown 生成
├── config.py              # 配置文件
├── requirements.txt       # 依赖（仅 requests + tqdm）
├── .env.example           # API Key 模板
├── README.md              # 英文说明
├── README_CN.md           # 中文说明（本文件）
├── data/
│   ├── papers.json        # 论文原始数据缓存
│   └── classified.json    # 分类结果缓存
└── output/
    └── SP2026.md          # 最终输出的 Markdown 文件
```

## 输出

完整分类论文列表见 [output/SP2026.md](output/SP2026.md)，共 199 篇论文，分为 12 个大类。
