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

---

## 论文分类结果

> 共 199 篇论文，12 个大类

### 密码学与隐私

*50 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [Cavern: Efficient Honest-Majority Maliciously Secure Z_$(2+1)$_Z -PC for Z_$\mathbb{Z}_{2^n}$_Z via DPFs](https://doi.org/10.1109/SP63933.2026.00089) | DPF安全多方计算 |
| [Secret State Leakage Attacks and their Impacts on EMV Contactless Payment Apps](https://doi.org/10.1109/SP63933.2026.00125) | EMV非接触安全 |
| [Parasol Compiler: Pushing the Boundaries of FHE Program Efficiency](https://doi.org/10.1109/SP63933.2026.00020) | FHE编译 |
| [Privacy-Conscious Algorithm Design via PAC Privacy](https://doi.org/10.1109/SP63933.2026.00147) | PAC隐私优化 |
| [Towards Practical Zero-Knowledge Proof for PSPACE](https://doi.org/10.1109/SP63933.2026.00041) | PSPACE零知识证明 |
| [LatORAM: ORAMs from Lateral Stashes and Delayed Shuffling](https://doi.org/10.1109/SP63933.2026.00075) | 不经意RAM |
| [ A Maliciously-Secure Post-Quantum OPRF from Crypto Dark Matter](https://doi.org/10.1109/SP63933.2026.00221) | 不经意伪随机函数 |
| [Optimistic Asynchronous Dynamic-committee Proactive Secret Sharing](https://doi.org/10.1109/SP63933.2026.00243) | 主动秘密共享 |
| [Dory: Streaming PCG with Small Memory](https://doi.org/10.1109/SP63933.2026.00079) | 伪随机关联生成器 |
| [Efficient Arithmetic-and-Comparison Homomorphic Encryption with Space Switching](https://doi.org/10.1109/SP63933.2026.00226) | 全同态加密 |
| [Chorus: Secret Recovery with Ephemeral Client Committees](https://doi.org/10.1109/SP63933.2026.00149) | 分布密钥恢复 |
| [New Constructions of Functional Adaptor Signatures: Broader Functions and Improved Efficiency](https://doi.org/10.1109/SP63933.2026.00100) | 功能适配签名 |
| [Can I Get More? An Incremental Inference Attack on Encrypted SQL](https://doi.org/10.1109/SP63933.2026.00133) | 加密库泄露滥用攻击 |
| [No Honor Among Crooks: Non-transferable Anonymous Tokens from Betrayability](https://doi.org/10.1109/SP63933.2026.00050) | 匿名令牌不可转让 |
| [xDup: Privacy-Preserving Deduplication for Humanitarian Organizations using Fuzzy PSI](https://doi.org/10.1109/SP63933.2026.00140) | 去重私密交集 |
| [Nebula: Proving machine executions via folding schemes](https://doi.org/10.1109/SP63933.2026.00099) | 可验证计算 |
| [Starfighters—On the General Applicability of X-Wing](https://doi.org/10.1109/SP63933.2026.00143) | 后量子KEM组合器 |
| [Blinding Post-Quantum Hash-and-Sign Signatures](https://doi.org/10.1109/SP63933.2026.00032) | 后量子盲签名 |
| [Concretely-Efficient Multi-Key Homomorphic Secret Sharing and Applications](https://doi.org/10.1109/SP63933.2026.00004) | 多密钥同态秘密分享 |
| [Secure Lookup Tables: Faster, Leaner, and More General](https://doi.org/10.1109/SP63933.2026.00209) | 安全多方计算 |
| [Euston: Efficient and User-Friendly Secure Transformer Inference with Non-Interactivity](https://doi.org/10.1109/SP63933.2026.00048) | 安全推理 |
| [AESpoly: Symmetric-Key Cryptographic Designs Using Instruction-Level Parallelism between AES and Polynomial Hash](https://doi.org/10.1109/SP63933.2026.00138) | 对称密钥设计 |
| [Auditing Apple’s DifferentialPrivacy.framework: Implementation Bugs, Misconfigurations, and Practical Risks](https://doi.org/10.1109/SP63933.2026.00225) | 差分隐私审计 |
| [CBUE: Conclusion Based Utility Evaluation for Differentially Private Categorical Data](https://doi.org/10.1109/SP63933.2026.00058) | 差分隐私效用评估 |
| [From Perfect to Approximate Hints: Efficient LWE Secret Recovery Leveraging Low Hamming Weight](https://doi.org/10.1109/SP63933.2026.00239) | 带边信息LWE恢复 |
| [Practical Asynchronous Distributed Key Reconfiguration and Its Applications](https://doi.org/10.1109/SP63933.2026.00033) | 异步分布式密钥生成 |
| [Breaking the Barrier for Asynchronous MPC with a Friend](https://doi.org/10.1109/SP63933.2026.00077) | 异步多方计算 |
| [GoSSamer: Lightweight and Linear-Communication Asynchronous (Dynamic Proactive) Secret Sharing and the Applications](https://doi.org/10.1109/SP63933.2026.00185) | 异步秘密共享 |
| [Generate-then-Verify: Reconstructing Data from Limited Published Statistics](https://doi.org/10.1109/SP63933.2026.00038) | 数据重建攻击 |
| [Single-Server Private Outsourcing of zk-SNARKs](https://doi.org/10.1109/SP63933.2026.00194) | 服务辅助零知识证明 |
| [Sparse Estimation Under Local Differential Privacy at All Privacy Levels](https://doi.org/10.1109/SP63933.2026.00234) | 本地差分稀疏估计 |
| [Consistent Estimation of Numerical Distributions under Local Differential Privacy by Wavelet Expansion](https://doi.org/10.1109/SP63933.2026.00054) | 本地差分隐私 |
| [VerfCNN, Optimal Complexity zkSNARK for Convolutional Neural Networks](https://doi.org/10.1109/SP63933.2026.00028) | 机器学习零知识证明 |
| [Lattice-based Threshold Blind Signatures](https://doi.org/10.1109/SP63933.2026.00118) | 格基门限盲签名 |
| [Efficient Fuzzy Private Set Intersection from Secret-shared OPRF](https://doi.org/10.1109/SP63933.2026.00172) | 模糊隐私交集 |
| [Scalable Registration-Based Encryption from Lattices](https://doi.org/10.1109/SP63933.2026.00199) | 注册基加密 |
| [Your Eyes Won't Lie: Snooping Online Voting Privacy from User Webcam](https://doi.org/10.1109/SP63933.2026.00232) | 眼动侧信道 |
| [InsPIRe: Communication-Efficient PIR with Server-side Preprocessing](https://doi.org/10.1109/SP63933.2026.00061) | 私密信息检索 |
| [Single-server Stateful PIR with Verifiability and Balanced Efficiency](https://doi.org/10.1109/SP63933.2026.00019) | 私密信息检索 |
| [VIA: Communication-Efficient Single-Server Private Information Retrieval](https://doi.org/10.1109/SP63933.2026.00086) | 私密信息检索 |
| [Verifiable PIR with Small Client Storage](https://doi.org/10.1109/SP63933.2026.00024) | 私密信息检索 |
| [Zelda: Efficient Multi-server Preprocessing PIR with Unconditional Security](https://doi.org/10.1109/SP63933.2026.00021) | 私密信息检索 |
| [Sort, Sweep, Mirror: Batch Private Interval Lookup with Logarithmic Cost](https://doi.org/10.1109/SP63933.2026.00113) | 私密查询协议 |
| [Practical Multi-party Private Set Intersection with Reducible Zero-sharing](https://doi.org/10.1109/SP63933.2026.00006) | 私密集合交集 |
| [A Leakage-Free Framework for Private Set Operations](https://doi.org/10.1109/SP63933.2026.00171) | 私密集合运算 |
| [Coral: Fast Succinct Non-Interactive Zero-Knowledge CFG Proofs](https://doi.org/10.1109/SP63933.2026.00059) | 简洁零知识证明 |
| [Robot: Robust Threshold BBS+ in Two Rounds](https://doi.org/10.1109/SP63933.2026.00238) | 门限匿名凭证 |
| [A Full Threshold NIST PQC-Compliant Framework for Distributed Trust in Federal Public Key Infrastructure](https://doi.org/10.1109/SP63933.2026.00164) | 门限后量子签名 |
| [Practical Anonymous Two-Party Gradient Boosting Decision Tree](https://doi.org/10.1109/SP63933.2026.00084) | 隐私保护GBDT |
| [Decomposition-Based Optimal Bounds for Privacy Amplification via Shuffling](https://doi.org/10.1109/SP63933.2026.00151) | 隐私放大混洗 |

### 系统安全

*37 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [Phoenix: Rowhammer Attacks on DDR5 with Self-Correcting Synchronization](https://doi.org/10.1109/SP63933.2026.00083) | DDR5内存破坏攻击 |
| [Demystifying and Exploiting ASLR on NVIDIA GPUs](https://doi.org/10.1109/SP63933.2026.00078) | GPU ASLR分析 |
| [GDDRHammer: Greatly Disturbing DRAM Rows — Cross-Component Rowhammer Attacks from Modern GPUs](https://doi.org/10.1109/SP63933.2026.00228) | GPU Rowhammer攻击 |
| [GeForge: Hammering GDDR Memory to Forge GPU Page Tables for Fun and Profit](https://doi.org/10.1109/SP63933.2026.00230) | GPU Rowhammer页表攻 |
| [GHost in the SHELL: A GPU-to-Host Memory Attack and Its Mitigation](https://doi.org/10.1109/SP63933.2026.00047) | GPU内存攻击 |
| [SoK: Systematizing a Decade of Architectural RowHammer Defenses Through the Lens of Streaming Algorithms](https://doi.org/10.1109/SP63933.2026.00114) | RowHammer防御 |
| [AEX-NStep: Probabilistic Interrupt Counting Attacks on Intel SGX](https://doi.org/10.1109/SP63933.2026.00035) | SGX中断攻击 |
| [SmuFuzz: Enable Deep System Management Mode Fuzzing in Fully Featured UEFI Runtime Environment](https://doi.org/10.1109/SP63933.2026.00011) | SMM模糊测试 |
| [Leafblower: a Leakage Attack Against TEE-Based Encrypted Databases](https://doi.org/10.1109/SP63933.2026.00008) | TEE加密数据库攻击 |
| [When VR Meets BCI: (Un)Observable Brainwave-aware Privacy Reconstruction in the Metaverse via Unrestricted Inbuilt Motion Sensors](https://doi.org/10.1109/SP63933.2026.00117) | VR侧信道攻击 |
| [EyeSpy: Inferring Eye Gaze via Side-Channel Attacks Against Foveated Rendering](https://doi.org/10.1109/SP63933.2026.00145) | VR眼动侧信道攻击 |
| [Chypnosis: Undervolting-based Static Side-channel Attacks](https://doi.org/10.1109/SP63933.2026.00090) | 侧信道攻击 |
| [TEE.fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition](https://doi.org/10.1109/SP63933.2026.00101) | 内存总线拦截 |
| [Battering RAM: Low-Cost Interposer Attacks on Confidential Computing via Dynamic Memory Aliasing](https://doi.org/10.1109/SP63933.2026.00052) | 内存总线攻击 |
| [NanoTag: Systems Support for Efficient Byte-Granular Overflow Detection on ARM MTE](https://doi.org/10.1109/SP63933.2026.00231) | 内存标记扩展 |
| [Heap Localization: Cache Side-Channel based Linux Kernel Heap Exploit Techniques](https://doi.org/10.1109/SP63933.2026.00196) | 内核堆利用 |
| [Fine-Grained Kernel Auditing using Augmented Syscall Reference Behavior Analysis and Virtualized Selective Tracing](https://doi.org/10.1109/SP63933.2026.00013) | 内核审计 |
| [RadKey: An LLM-Guided RF Backscatter System for Through-Wall Keystroke Inference](https://doi.org/10.1109/SP63933.2026.00160) | 击键推断 |
| [KeyTAR: Practical Keystroke Timing Attacks and Input Reconstruction](https://doi.org/10.1109/SP63933.2026.00106) | 击键时序攻击 |
| [TÄMU: Emulating Trusted Applications at the (GlobalPlatform)-API Layer](https://doi.org/10.1109/SP63933.2026.00139) | 可信应用模拟 |
| [Convenience at a Cost: The Security Risks of Template-based Development in the App-in-App Ecosystem](https://doi.org/10.1109/SP63933.2026.00074) | 小程序模板安全 |
| [Fractal: An Operating System Designed for Microarchitecture Reverse Engineering](https://doi.org/10.1109/SP63933.2026.00141) | 微架构逆向工程 |
| [Enter, Exit, Page Fault, Leak: Testing Isolation Boundaries for Microarchitectural Leaks](https://doi.org/10.1109/SP63933.2026.00007) | 微架构隔离测试 |
| [VMSCAPE: Exposing and Exploiting Incomplete Branch Predictor Isolation in Cloud Environments](https://doi.org/10.1109/SP63933.2026.00046) | 推测执行攻击 |
| [It’s a Feature, Not a Bug: Secure and Auditable State Rollback for Confidential Cloud Applications](https://doi.org/10.1109/SP63933.2026.00148) | 机密云状态回滚 |
| [Sealing the Window: Efficient Tamper Protection for Provenance Logs](https://doi.org/10.1109/SP63933.2026.00092) | 来源日志篡改检测 |
| [PrintSpy: Pixel-Level Eavesdropping on Commodity Laser Printers via Electromagnetic Side Channels](https://doi.org/10.1109/SP63933.2026.00119) | 电磁侧信道 |
| [Transient Architectural Execution: From Weird Gates to Weird Programs](https://doi.org/10.1109/SP63933.2026.00066) | 瞬态异常计算 |
| [Rain: Transiently Leaking Data from Public Clouds Using Old Vulnerabilities](https://doi.org/10.1109/SP63933.2026.00063) | 瞬态执行攻击 |
| [TREVEX: A Black-Box Detection Framework For Data-Flow Transient Execution Vulnerabilities](https://doi.org/10.1109/SP63933.2026.00135) | 瞬态执行检测 |
| [Crucible: Retrofitting Commodity CPUs with Vulnerabilities via Transparent Software Emulation](https://doi.org/10.1109/SP63933.2026.00186) | 瞬态执行模拟 |
| [Defeating Transient Execution Attacks by Limiting Secret Reachability through Register Hiding and ShadowCFI](https://doi.org/10.1109/SP63933.2026.00015) | 瞬态执行缓解 |
| [Hardware Trojans from Invisible Inversions: On the Trojanizability of Standard Cell Libraries](https://doi.org/10.1109/SP63933.2026.00219) | 硬件木马检测 |
| [INSIGHT: Automatic Generation of Explanations for Efficient Identification of Hardware Bugs and Underspecifications](https://doi.org/10.1109/SP63933.2026.00201) | 硬件缺陷检测 |
| [Understanding and Analyzing Privacy Risks in Mobile Consent-Management Platforms](https://doi.org/10.1109/SP63933.2026.00069) | 移动应用同意管理 |
| [RISCy Cache Coherence: Timer-Free Architectural Cache Attacks via Instruction/Data Cache Incoherence](https://doi.org/10.1109/SP63933.2026.00192) | 缓存一致性侧信道 |
| [SeqAss: Using Sequential Associative Caches to Mitigate Conflict-Based Cache Attacks with Reduced Cache Misses and Performance Overhead](https://doi.org/10.1109/SP63933.2026.00073) | 缓存侧信道缓解 |

### 软件安全

*24 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [SFA-Miner: Mining Path-Sensitive API Usage Patterns via Symbolic Finite Automata](https://doi.org/10.1109/SP63933.2026.00056) | API使用模式挖掘 |
| [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://doi.org/10.1109/SP63933.2026.00211) | CLI模糊测试 |
| [Cosseter: GitHub Actions Permission Reduction Using Demand-Driven Static Analysis](https://doi.org/10.1109/SP63933.2026.00067) | GitHub权限分析 |
| [Crashing Through Defenses: Exploiting Segfaults and Chaining around Intel CET](https://doi.org/10.1109/SP63933.2026.00216) | Intel CET绕过 |
| [Jazzer: Coverage-Guided Fuzzing for Semantic Vulnerabilities in the Java Ecosystem](https://doi.org/10.1109/SP63933.2026.00134) | Java模糊测试 |
| [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://doi.org/10.1109/SP63933.2026.00223) | Java漏洞发现 |
| [The First Large-Scale Systematic Study of Python Class Pollution Vulnerability](https://doi.org/10.1109/SP63933.2026.00108) | Python类污染 |
| [PUFFERDOS: Efficient and Effective Attack String Generation for Regular Expression Denial of Service Vulnerabilities](https://doi.org/10.1109/SP63933.2026.00169) | ReDoS攻击生成 |
| [deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses](https://doi.org/10.1109/SP63933.2026.00060) | Rust内存安全模糊测试 |
| [Navigating Developers’ Quagmire: LLM-Enabled Privacy Compliance Analysis for SDK Integrations](https://doi.org/10.1109/SP63933.2026.00126) | SDK隐私合规 |
| [CiRCLE: Recovering Complex Data Structures in Binaries beyond Fragmentation](https://doi.org/10.1109/SP63933.2026.00146) | 二进制数据结构恢复 |
| [QuickSafe: Targeted Hardening Against Memory Corruption](https://doi.org/10.1109/SP63933.2026.00085) | 内存安全加固 |
| [Stop Starving or Stuffing Me: Boosting Firmware Fuzzing Efficiency with On-demand Input Delivery](https://doi.org/10.1109/SP63933.2026.00155) | 固件模糊测试 |
| [A Context is Worth a Thousand Lies: Evading Intrusion Detectors via Intelligent Context Distortion](https://doi.org/10.1109/SP63933.2026.00202) | 基于来源的IDS规避 |
| [Beyond Nodes vs. Edges: A Multi-View Fusion Framework for Provenance-Based Intrusion Detection](https://doi.org/10.1109/SP63933.2026.00242) | 多视图溯源入侵检测 |
| [Cottontail: Large Language Model-Driven Concolic Execution for Highly Structured Test Input Generation](https://doi.org/10.1109/SP63933.2026.00110) | 大模型指导符号执行 |
| [Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis](https://doi.org/10.1109/SP63933.2026.00121) | 大模型程序分析 |
| [TrigFuzz: Triggering Conditions Guided Directed Fuzzing](https://doi.org/10.1109/SP63933.2026.00156) | 定向模糊测试 |
| [PLaTypus: Restricting Cross-Module Transitions to Mitigate Code-Reuse Attacks](https://doi.org/10.1109/SP63933.2026.00189) | 控制流完整性防御 |
| [Agentic Concolic Execution](https://doi.org/10.1109/SP63933.2026.00003) | 混合执行 |
| [Fizzle: A Framework for Deterministic and Reproducible Network Fuzzing](https://doi.org/10.1109/SP63933.2026.00091) | 网络协议模糊测试 |
| [PORTGPT: Towards Automated Backporting Using Large Language Models](https://doi.org/10.1109/SP63933.2026.00034) | 自动补丁回溯 |
| [Best of Both Worlds: Effective Foreign Bridge Identification in V8 Embedders for Security Analysis](https://doi.org/10.1109/SP63933.2026.00115) | 跨语言安全分析 |
| [zkFuzz: Foundation and Framework for Effective Fuzzing of Zero-Knowledge Circuits](https://doi.org/10.1109/SP63933.2026.00049) | 零知识电路模糊测试 |

### 可用安全与隐私

*20 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [Towards Automating Data Access Permissions in AI Agents](https://doi.org/10.1109/SP63933.2026.00018) | AI代理数据权限 |
| [Consumer Beware! Exploring Data Brokers’ CCPA Compliance](https://doi.org/10.1109/SP63933.2026.00104) | CCPA合规研究 |
| [Setting the Course, but Forgetting to Steer: Analyzing Compliance with GDPR’s Right of Access to Data by Instagram, TikTok, and YouTube](https://doi.org/10.1109/SP63933.2026.00051) | GDPR合规分析 |
| [LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres](https://doi.org/10.1109/SP63933.2026.00111) | SOC分析师LLM使用 |
| [Usable Anonymity in Reproductive Health Privacy](https://doi.org/10.1109/SP63933.2026.00023) | 匿名可用性 |
| [Toward Inclusive Security and Privacy for Deaf and Hard-of-Hearing People: A Community-Based Interview Study](https://doi.org/10.1109/SP63933.2026.00027) | 听障社区包容安全 |
| [The Passkey Promise: A Comparative Usability Study of MFA Methods](https://doi.org/10.1109/SP63933.2026.00055) | 多因子可用性 |
| [LISA: A Scale-Optimized and Psychometrically-Validated Instrument for the Lightweight Assessment of Organizational Information Security Awareness in Heterogeneous Organizations](https://doi.org/10.1109/SP63933.2026.00174) | 安全意识测量 |
| [MAYA: Addressing Inconsistencies in Generative Password Guessing through a Unified Benchmark](https://doi.org/10.1109/SP63933.2026.00081) | 密码猜测评估 |
| [No Password, No Problem? A Large-Scale Field Study of Passkey Adoption and Usage](https://doi.org/10.1109/SP63933.2026.00022) | 密钥采用与使用 |
| [Searching for a Farang: Collective Security among Women in Pattaya, Thailand](https://doi.org/10.1109/SP63933.2026.00017) | 性工作者网安 |
| [Privacy Perspectives and Practices of Chinese Smart Home Product Teams](https://doi.org/10.1109/SP63933.2026.00014) | 智能家居隐私实践 |
| [Responsible Disclosure is a Two-Way Street: Empirically Measuring the Responsible Disclosure Contract in the Firmware Ecosystem](https://doi.org/10.1109/SP63933.2026.00180) | 漏洞披露测量 |
| [Behind the Curtain: How Shared Hosting Providers Respond to Vulnerability Notifications](https://doi.org/10.1109/SP63933.2026.00036) | 漏洞通知响应 |
| [When Designers Meet GenAI: Understanding the Role of Prompt-to-Design Generators in Privacy Dark Patterns](https://doi.org/10.1109/SP63933.2026.00131) | 生成设计暗模式 |
| [Perceived Privacy Risk and Mitigation Post-Roe](https://doi.org/10.1109/SP63933.2026.00064) | 生殖隐私行为 |
| [From "Be Careful" to "Here's Why": Investigating User Reasoning with Context-Specific SMS Scam Warnings](https://doi.org/10.1109/SP63933.2026.00200) | 短信诈骗警告可用性 |
| [International Students and Scams: At Risk Abroad](https://doi.org/10.1109/SP63933.2026.00094) | 针对留学生诈骗 |
| ["I Wonder if These Warnings Are Accurate": Security and Privacy Advice in Nine Majority World Countries](https://doi.org/10.1109/SP63933.2026.00005) | 非西方安全建议 |
| [Hidden Secrets in the arXiv: Discovering, Analyzing, and Preventing Unintentional Information Disclosure in Source Files of Scientific Preprints](https://doi.org/10.1109/SP63933.2026.00217) | 预印本源码隐私 |

### 大语言模型与AI安全

*16 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [AI Wrote My Paper and All I Got Was This False Negative:* Measuring the Efficacy of Commercial AI Text Detectors](https://doi.org/10.1109/SP63933.2026.00088) | AI文本检测 |
| [GraphRAG under Fire](https://doi.org/10.1109/SP63933.2026.00070) | GraphRAG投毒 |
| [WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers](https://doi.org/10.1109/SP63933.2026.00025) | 大模型代理安全 |
| [LLM Unlearning Should Be Form-Independent](https://doi.org/10.1109/SP63933.2026.00037) | 大模型遗忘 |
| [LLMThief: Evaluating Configuration Leaking Risks in Commercial LLM App Stores](https://doi.org/10.1109/SP63933.2026.00195) | 大模型配置泄露 |
| [EnchTable: Unified Safety Alignment Transfer in Fine-tuned Large Language Models](https://doi.org/10.1109/SP63933.2026.00072) | 安全对齐迁移 |
| [PromptLocate: Localizing Prompt Injection Attacks](https://doi.org/10.1109/SP63933.2026.00105) | 提示注入定位 |
| [When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins](https://doi.org/10.1109/SP63933.2026.00062) | 提示注入攻击 |
| [Who Taught the Lie? Responsibility Attribution for Poisoned Knowledge in Retrieval-Augmented Generation](https://doi.org/10.1109/SP63933.2026.00053) | 检索增强生成投毒 |
| [WRATH: Turning Watermark Robustness Against Itself via a Watermark-Agnostic Black-Box Invalidation Attack](https://doi.org/10.1109/SP63933.2026.00197) | 水印攻击 |
| [DREAM: Scalable Red Teaming for Text-to-Image Generative Systems via Distribution Modeling](https://doi.org/10.1109/SP63933.2026.00112) | 红队测试 |
| [Investigating the Impact of Dark Patterns on LLM-Based Web Agents](https://doi.org/10.1109/SP63933.2026.00042) | 网页代理暗模式 |
| [SoK: Evaluating Jailbreak Guardrails for Large Language Models](https://doi.org/10.1109/SP63933.2026.00076) | 越狱护栏 |
| [MetaBreak: Jailbreaking Online LLM Services via Special Token Manipulation](https://doi.org/10.1109/SP63933.2026.00095) | 越狱攻击 |
| [URLcoat: Exploiting Web Search Capability to Jailbreak Large Language Models](https://doi.org/10.1109/SP63933.2026.00082) | 越狱攻击 |
| [SoK: Robustness in Large Language Models against Jailbreak Attacks](https://doi.org/10.1109/SP63933.2026.00107) | 越狱鲁棒性 |

### 网络安全

*12 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [Guardians of the Air: In-Device Detection of 5G Control-Plane Threats](https://doi.org/10.1109/SP63933.2026.00204) | 5G控制面威胁检测 |
| [The Threat Landscape of IP Leasing in the RPKI Era](https://doi.org/10.1109/SP63933.2026.00012) | BGP/RPKI安全 |
| [Descriptors of Exposure: Undermining Tor Anonymity through Exploiting Descriptor Flood](https://doi.org/10.1109/SP63933.2026.00071) | Tor描述符洪泛攻击 |
| [LeakyLinks: Measuring the Security and Privacy Risks of URL Scanning Services](https://doi.org/10.1109/SP63933.2026.00130) | URL扫描隐私风险 |
| [SaTor: Exploring Satellite Routing in Tor to Reduce Latency](https://doi.org/10.1109/SP63933.2026.00068) | 卫星路由降延迟 |
| [Revisiting PQ WireGuard: A Comprehensive Security Analysis With a New Design Using Reinforced KEMs](https://doi.org/10.1109/SP63933.2026.00057) | 后量子VPN协议 |
| [CenAlert: Amplifying User Voices to Rally Censorship Investigation](https://doi.org/10.1109/SP63933.2026.00229) | 审查检测 |
| [CenRL: A Framework for Performing Intelligent Censorship Measurements](https://doi.org/10.1109/SP63933.2026.00098) | 审查测量 |
| [Designing Transport-Level Encryption for Datacenter Networks](https://doi.org/10.1109/SP63933.2026.00080) | 数据中心网络加密 |
| [RIS-CLA: Reviving CSI-Based Continuous Location Authentication with Reconfigurable Intelligent Surfaces](https://doi.org/10.1109/SP63933.2026.00031) | 无线认证 |
| [STIR/SHAKEN: A Cocktail of Cryptographic Clumsiness](https://doi.org/10.1109/SP63933.2026.00093) | 电话诈骗防范 |
| [One Tap to Hijack Them All: A Security Analysis of the Google Fast Pair Protocol](https://doi.org/10.1109/SP63933.2026.00210) | 蓝牙配对安全 |

### Web安全

*11 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [KeyChaser: Unveiling API Keys in Browser Extensions](https://doi.org/10.1109/SP63933.2026.00187) | API密钥检测 |
| [Breaking the Illusion: Automated Reasoning of GDPR Consent Violations](https://doi.org/10.1109/SP63933.2026.00040) | GDPR违规检测 |
| [Audience Injection Attacks: A New Class of Attacks on Web-Based Authorization and Authentication Standards](https://doi.org/10.1109/SP63933.2026.00116) | OAuth/OpenID攻击 |
| [Demystifying the (In)Security of OAuth-based Account Linking in Connector Ecosystems](https://doi.org/10.1109/SP63933.2026.00128) | OAuth账户关联 |
| [APIEcho: Training-less Anomaly Detection via Intra-API Behavioral Comparison for Web Applications](https://doi.org/10.1109/SP63933.2026.00016) | Web异常检测 |
| [Poisoned by the Host: Large-Scale Measurement of Host Name Poisoning in Web Applications](https://doi.org/10.1109/SP63933.2026.00166) | 主机名投毒 |
| [Credential Extraction Attacks Against Compromised Credential Checking Services of Password Managers](https://doi.org/10.1109/SP63933.2026.00103) | 密码管理器安全 |
| [State of Browser Process-Isolation: The Same-Site Weakness](https://doi.org/10.1109/SP63933.2026.00096) | 浏览器进程隔离 |
| [SoK: After Decades of Web Tracker Detection, What’s Next?](https://doi.org/10.1109/SP63933.2026.00222) | 网页追踪检测 |
| [Web Application Vulnerability Repair via Context-Aware Fault Localization and Directed Differential Fuzzing](https://doi.org/10.1109/SP63933.2026.00237) | 自动漏洞修复 |
| [Understanding Data Collection, Brokerage, and Spam in the Lead Marketing Ecosystem](https://doi.org/10.1109/SP63933.2026.00162) | 营销数据隐私 |

### 机器学习与安全

*11 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [Revelio: Blurred Images Can Still Disclose Your Identity](https://doi.org/10.1109/SP63933.2026.00030) | 人脸去模糊攻 |
| [Shared Spotlight Meridian: Distributed Sparse Pseudorandom Functions for Scalable Federated Learning](https://doi.org/10.1109/SP63933.2026.00065) | 安全联邦学习聚合 |
| [Are LLM-Enhanced Graph Neural Networks Robust against Poisoning Attacks?](https://doi.org/10.1109/SP63933.2026.00212) | 投毒鲁棒性 |
| [ARES: Scalable and Practical Gradient Inversion Attack in Federated Learning through Activation Recovery](https://doi.org/10.1109/SP63933.2026.00181) | 梯度反演攻击 |
| [On the Detectability of Active Gradient Inversion Attacks in Federated Learning](https://doi.org/10.1109/SP63933.2026.00193) | 梯度反演检测 |
| [On the (In)Security of Loading Machine Learning Models](https://doi.org/10.1109/SP63933.2026.00123) | 模型加载安全 |
| [ Exploiting Leaderboards for Large-Scale Distribution of Poisoned Models](https://doi.org/10.1109/SP63933.2026.00044) | 模型投毒 |
| [Your Compiler is Backdooring Your Model: Understanding and Exploiting Compilation Inconsistency Vulnerabilities in Deep Learning Compilers](https://doi.org/10.1109/SP63933.2026.00097) | 深度学习编译器后门 |
| [Weaponizing Reflectivity for Pointcloud Deception with Forged Invisible Geometries](https://doi.org/10.1109/SP63933.2026.00183) | 物理对抗点云攻击 |
| [MusicShield: Protection for Musicians in the Era of Generative AI](https://doi.org/10.1109/SP63933.2026.00039) | 生成模型对抗样本 |
| [Ensemble Conformal Predictor (EnCP): A New Conformal Predictor with Robustness Guarantees against Data Poisoning Attacks](https://doi.org/10.1109/SP63933.2026.00043) | 符合预测鲁棒性 |

### 区块链与分布式系统

*6 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [A Liveness Attack to Ethereum PoS with No Additional Cost](https://doi.org/10.1109/SP63933.2026.00235) | 以太坊PoS活攻 |
| [Mechanized Safety and Liveness Proofs for the Mysticeti Consensus Protocol under the LiDO-DAG Framework](https://doi.org/10.1109/SP63933.2026.00009) | 共识协议验证 |
| [Fast Deterministically Safe Proof-of-Work Consensus](https://doi.org/10.1109/SP63933.2026.00102) | 工作量证明共识 |
| [Scalable Accountable Byzantine Agreement and Beyond](https://doi.org/10.1109/SP63933.2026.00029) | 拜占庭共识问责 |
| [Prrr: Personal Random Rewards for Blockchain Reporting](https://doi.org/10.1109/SP63933.2026.00136) | 激励机制设计 |
| [Jigsaw: Doubly Private Smart Contracts](https://doi.org/10.1109/SP63933.2026.00109) | 隐私保护智能合约 |

### 形式化方法与验证

*5 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [C-Verifier: Understanding and Formally Verifying Cross-Service Flaws in AWS Cognito](https://doi.org/10.1109/SP63933.2026.00010) | 云安全验证 |
| [Automated formal analysis of Signal's Double Ratchet: attacks, fixes and security proofs](https://doi.org/10.1109/SP63933.2026.00120) | 协议验证 |
| [DY* Unchained: Now with Composable Security Proofs and Precise   Compromise Scenarios](https://doi.org/10.1109/SP63933.2026.00220) | 协议验证 |
| [The Secrets Must Not Flow: Scaling Security Verification to Large Codebases](https://doi.org/10.1109/SP63933.2026.00026) | 安全协议验证 |
| [Language-Agnostic Detection of Computation-Constraint Inconsistencies in ZKP Programs via Value Inference](https://doi.org/10.1109/SP63933.2026.00207) | 零知识程序验证 |

### 物联网与信息物理系统

*5 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [Camveil: Unveiling Security Camera Vulnerabilities through Multi-Protocol Coordinated Fuzzing](https://doi.org/10.1109/SP63933.2026.00002) | IoT模糊测试 |
| [2FiA: Towards WiFi Sensing-Based Authentication with Unique Biometrics](https://doi.org/10.1109/SP63933.2026.00087) | WiFi生物认证 |
| [SatBleed: Security of Commoditized Communication Modules in Satellites](https://doi.org/10.1109/SP63933.2026.00213) | 卫星安全 |
| [Bridge: High-Order Taint Vulnerabilities Detection in Linux-based IoT Firmware](https://doi.org/10.1109/SP63933.2026.00001) | 固件漏洞检测 |
| [BACHunter: Detecting Broken Access Control Vulnerabilities in Intelligent Connected Vehicles](https://doi.org/10.1109/SP63933.2026.00152) | 访问控制漏洞检测 |

### 数字取证与网络犯罪

*2 篇论文*

| 论文 | 研究领域 |
|------|----------|
| [PromoGuardian: Detecting Promotion Abuse Fraud with Multi-Relation Fused Graph Neural Networks](https://doi.org/10.1109/SP63933.2026.00045) | 促销滥用检测 |
| [Breaking Free from Ivory Tower: Evaluating and Enhancing Real-world Chinese Underground Adversarial Jargon Detection](https://doi.org/10.1109/SP63933.2026.00233) | 对抗术语检测 |
