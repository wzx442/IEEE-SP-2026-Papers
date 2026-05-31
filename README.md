# IEEE S&P 2026 Accepted Papers

> **Total papers: 199** | 
> Categories: 12 | 
> Generated from [IEEE S&P 2026 Proceedings](https://www.computer.org/csdl/proceedings/sp/2026/2bojuokAJK8)

> Classification performed by DeepSeek AI; 
> please excuse any errors.

---

<details>
<summary>IEEE S&P 2026 Paper Fetcher & Classifier (click to expand)</summary>

## IEEE S&P 2026 Paper Fetcher & Classifier

Fetches all papers from the IEEE S&P 2026 proceedings via the IEEE CSDL GraphQL API, classifies them using DeepSeek AI, and generates an organized Markdown file.

No browser, Playwright, or manual interaction needed — pure API pipeline.

### Setup

```bash
pip install -r requirements.txt
cp .env.example .env         # then edit .env with your DeepSeek API key
```

### Usage

```bash
python main.py                  # Full pipeline (fetch + classify + output)
python main.py --fetch-only     # Only fetch from API
python main.py --classify-only  # Only classify (from cache)
python main.py --output-only    # Only generate MD (from cache)
python main.py --force          # Force re-fetch and re-classify
```

### How it works

1. Calls the IEEE CSDL GraphQL API to fetch all 199 papers (title, abstract, authors, DOI) in one request
2. Classifies each paper into a broad category and a specific sub-area using DeepSeek API
3. Generates `output/SP2026.md` with papers grouped by category, each as a `[title](link) | sub-area` table row

### Output

See [output/SP2026.md](output/SP2026.md) for the full categorized paper list.

</details>

## Table of Contents

- [Cryptography and Privacy (50)](#cryptography-and-privacy)
- [Systems Security (37)](#systems-security)
- [Software Security (24)](#software-security)
- [Usable Security and Privacy (20)](#usable-security-and-privacy)
- [LLMs and AI Safety (16)](#llms-and-ai-safety)
- [Network Security (12)](#network-security)
- [Machine Learning and Security (11)](#machine-learning-and-security)
- [Web Security (11)](#web-security)
- [Blockchain and Distributed Systems (6)](#blockchain-and-distributed-systems)
- [Formal Methods and Verification (5)](#formal-methods-and-verification)
- [IoT and Cyber-Physical Systems (5)](#iot-and-cyber-physical-systems)
- [Digital Forensics and Cybercrime (2)](#digital-forensics-and-cybercrime)

---

## Cryptography and Privacy

*50 papers*

| Paper | Sub-area |
|-------|----------|
| [No Honor Among Crooks: Non-transferable Anonymous Tokens from Betrayability](https://doi.org/10.1109/SP63933.2026.00050) | Anonymous Tokens and Non-transferability |
| [Practical Asynchronous Distributed Key Reconfiguration and Its Applications](https://doi.org/10.1109/SP63933.2026.00033) | Asynchronous Distributed Key Generation |
| [Breaking the Barrier for Asynchronous MPC with a Friend](https://doi.org/10.1109/SP63933.2026.00077) | Asynchronous MPC |
| [GoSSamer: Lightweight and Linear-Communication Asynchronous (Dynamic Proactive) Secret Sharing and the Applications](https://doi.org/10.1109/SP63933.2026.00185) | Asynchronous Secret Sharing |
| [Generate-then-Verify: Reconstructing Data from Limited Published Statistics](https://doi.org/10.1109/SP63933.2026.00038) | Data Reconstruction Attacks |
| [Auditing Apple’s DifferentialPrivacy.framework: Implementation Bugs, Misconfigurations, and Practical Risks](https://doi.org/10.1109/SP63933.2026.00225) | Differential Privacy Auditing |
| [CBUE: Conclusion Based Utility Evaluation for Differentially Private Categorical Data](https://doi.org/10.1109/SP63933.2026.00058) | Differential Privacy Utility Evaluation |
| [Chorus: Secret Recovery with Ephemeral Client Committees](https://doi.org/10.1109/SP63933.2026.00149) | Distributed Secret Recovery |
| [Secret State Leakage Attacks and their Impacts on EMV Contactless Payment Apps](https://doi.org/10.1109/SP63933.2026.00125) | EMV contactless payment security |
| [Your Eyes Won't Lie: Snooping Online Voting Privacy from User Webcam](https://doi.org/10.1109/SP63933.2026.00232) | Eye Movement Side Channel |
| [Parasol Compiler: Pushing the Boundaries of FHE Program Efficiency](https://doi.org/10.1109/SP63933.2026.00020) | FHE Compilation |
| [Efficient Arithmetic-and-Comparison Homomorphic Encryption with Space Switching](https://doi.org/10.1109/SP63933.2026.00226) | Fully Homomorphic Encryption |
| [New Constructions of Functional Adaptor Signatures: Broader Functions and Improved Efficiency](https://doi.org/10.1109/SP63933.2026.00100) | Functional Adaptor Signatures |
| [Efficient Fuzzy Private Set Intersection from Secret-shared OPRF](https://doi.org/10.1109/SP63933.2026.00172) | Fuzzy Private Set Intersection |
| [From Perfect to Approximate Hints: Efficient LWE Secret Recovery Leveraging Low Hamming Weight](https://doi.org/10.1109/SP63933.2026.00239) | LWE Secret Recovery with Side Information |
| [Lattice-based Threshold Blind Signatures](https://doi.org/10.1109/SP63933.2026.00118) | Lattice-based Threshold Blind Signatures |
| [Can I Get More? An Incremental Inference Attack on Encrypted SQL](https://doi.org/10.1109/SP63933.2026.00133) | Leakage-Abuse Attacks on Encrypted Databases |
| [Consistent Estimation of Numerical Distributions under Local Differential Privacy by Wavelet Expansion](https://doi.org/10.1109/SP63933.2026.00054) | Local Differential Privacy |
| [Sparse Estimation Under Local Differential Privacy at All Privacy Levels](https://doi.org/10.1109/SP63933.2026.00234) | Local Differential Privacy Sparse Estimation |
| [Concretely-Efficient Multi-Key Homomorphic Secret Sharing and Applications](https://doi.org/10.1109/SP63933.2026.00004) | Multi-Key Homomorphic Secret Sharing |
| [ A Maliciously-Secure Post-Quantum OPRF from Crypto Dark Matter](https://doi.org/10.1109/SP63933.2026.00221) | Oblivious Pseudorandom Functions |
| [LatORAM: ORAMs from Lateral Stashes and Delayed Shuffling](https://doi.org/10.1109/SP63933.2026.00075) | Oblivious RAM |
| [Privacy-Conscious Algorithm Design via PAC Privacy](https://doi.org/10.1109/SP63933.2026.00147) | PAC Privacy Optimization |
| [Blinding Post-Quantum Hash-and-Sign Signatures](https://doi.org/10.1109/SP63933.2026.00032) | Post-Quantum Blind Signatures |
| [Starfighters—On the General Applicability of X-Wing](https://doi.org/10.1109/SP63933.2026.00143) | Post-Quantum KEM Combiners |
| [Decomposition-Based Optimal Bounds for Privacy Amplification via Shuffling](https://doi.org/10.1109/SP63933.2026.00151) | Privacy Amplification Shuffling |
| [Practical Anonymous Two-Party Gradient Boosting Decision Tree](https://doi.org/10.1109/SP63933.2026.00084) | Privacy-Preserving GBDT |
| [InsPIRe: Communication-Efficient PIR with Server-side Preprocessing](https://doi.org/10.1109/SP63933.2026.00061) | Private Information Retrieval |
| [Single-server Stateful PIR with Verifiability and Balanced Efficiency](https://doi.org/10.1109/SP63933.2026.00019) | Private Information Retrieval |
| [VIA: Communication-Efficient Single-Server Private Information Retrieval](https://doi.org/10.1109/SP63933.2026.00086) | Private Information Retrieval |
| [Verifiable PIR with Small Client Storage](https://doi.org/10.1109/SP63933.2026.00024) | Private Information Retrieval |
| [Zelda: Efficient Multi-server Preprocessing PIR with Unconditional Security](https://doi.org/10.1109/SP63933.2026.00021) | Private Information Retrieval |
| [Sort, Sweep, Mirror: Batch Private Interval Lookup with Logarithmic Cost](https://doi.org/10.1109/SP63933.2026.00113) | Private Lookup Protocols |
| [Practical Multi-party Private Set Intersection with Reducible Zero-sharing](https://doi.org/10.1109/SP63933.2026.00006) | Private Set Intersection |
| [A Leakage-Free Framework for Private Set Operations](https://doi.org/10.1109/SP63933.2026.00171) | Private Set Operations |
| [xDup: Privacy-Preserving Deduplication for Humanitarian Organizations using Fuzzy PSI](https://doi.org/10.1109/SP63933.2026.00140) | Private set intersection for deduplication |
| [Optimistic Asynchronous Dynamic-committee Proactive Secret Sharing](https://doi.org/10.1109/SP63933.2026.00243) | Proactive Secret Sharing |
| [Dory: Streaming PCG with Small Memory](https://doi.org/10.1109/SP63933.2026.00079) | Pseudorandom Correlation Generators |
| [Scalable Registration-Based Encryption from Lattices](https://doi.org/10.1109/SP63933.2026.00199) | Registration-Based Encryption |
| [Euston: Efficient and User-Friendly Secure Transformer Inference with Non-Interactivity](https://doi.org/10.1109/SP63933.2026.00048) | Secure Inference |
| [Cavern: Efficient Honest-Majority Maliciously Secure Z_$(2+1)$_Z -PC for Z_$\mathbb{Z}_{2^n}$_Z via DPFs](https://doi.org/10.1109/SP63933.2026.00089) | Secure MPC with DPFs |
| [Secure Lookup Tables: Faster, Leaner, and More General](https://doi.org/10.1109/SP63933.2026.00209) | Secure multi-party computation |
| [Single-Server Private Outsourcing of zk-SNARKs](https://doi.org/10.1109/SP63933.2026.00194) | Server-aided zk-SNARKs |
| [Coral: Fast Succinct Non-Interactive Zero-Knowledge CFG Proofs](https://doi.org/10.1109/SP63933.2026.00059) | Succinct ZK Proofs |
| [AESpoly: Symmetric-Key Cryptographic Designs Using Instruction-Level Parallelism between AES and Polynomial Hash](https://doi.org/10.1109/SP63933.2026.00138) | Symmetric-key cryptography design |
| [Robot: Robust Threshold BBS+ in Two Rounds](https://doi.org/10.1109/SP63933.2026.00238) | Threshold Anonymous Credentials |
| [A Full Threshold NIST PQC-Compliant Framework for Distributed Trust in Federal Public Key Infrastructure](https://doi.org/10.1109/SP63933.2026.00164) | Threshold Post-Quantum Signatures |
| [Nebula: Proving machine executions via folding schemes](https://doi.org/10.1109/SP63933.2026.00099) | Verifiable Computation |
| [Towards Practical Zero-Knowledge Proof for PSPACE](https://doi.org/10.1109/SP63933.2026.00041) | Zero-Knowledge Proofs for PSPACE |
| [VerfCNN, Optimal Complexity zkSNARK for Convolutional Neural Networks](https://doi.org/10.1109/SP63933.2026.00028) | Zero-knowledge proofs for ML |

---

## Systems Security

*37 papers*

| Paper | Sub-area |
|-------|----------|
| [RISCy Cache Coherence: Timer-Free Architectural Cache Attacks via Instruction/Data Cache Incoherence](https://doi.org/10.1109/SP63933.2026.00192) | Cache coherence side channel |
| [SeqAss: Using Sequential Associative Caches to Mitigate Conflict-Based Cache Attacks with Reduced Cache Misses and Performance Overhead](https://doi.org/10.1109/SP63933.2026.00073) | Cache side-channel mitigation |
| [It’s a Feature, Not a Bug: Secure and Auditable State Rollback for Confidential Cloud Applications](https://doi.org/10.1109/SP63933.2026.00148) | Confidential Cloud State Rollback |
| [Understanding and Analyzing Privacy Risks in Mobile Consent-Management Platforms](https://doi.org/10.1109/SP63933.2026.00069) | Consent management in mobile apps |
| [Phoenix: Rowhammer Attacks on DDR5 with Self-Correcting Synchronization](https://doi.org/10.1109/SP63933.2026.00083) | DDR5 Rowhammer attacks |
| [PrintSpy: Pixel-Level Eavesdropping on Commodity Laser Printers via Electromagnetic Side Channels](https://doi.org/10.1109/SP63933.2026.00119) | Electromagnetic Side Channel |
| [Demystifying and Exploiting ASLR on NVIDIA GPUs](https://doi.org/10.1109/SP63933.2026.00078) | GPU ASLR analysis |
| [GDDRHammer: Greatly Disturbing DRAM Rows — Cross-Component Rowhammer Attacks from Modern GPUs](https://doi.org/10.1109/SP63933.2026.00228) | GPU Rowhammer attacks |
| [GeForge: Hammering GDDR Memory to Forge GPU Page Tables for Fun and Profit](https://doi.org/10.1109/SP63933.2026.00230) | GPU Rowhammer page table attack |
| [GHost in the SHELL: A GPU-to-Host Memory Attack and Its Mitigation](https://doi.org/10.1109/SP63933.2026.00047) | GPU memory attack |
| [INSIGHT: Automatic Generation of Explanations for Efficient Identification of Hardware Bugs and Underspecifications](https://doi.org/10.1109/SP63933.2026.00201) | Hardware Bug Detection |
| [Hardware Trojans from Invisible Inversions: On the Trojanizability of Standard Cell Libraries](https://doi.org/10.1109/SP63933.2026.00219) | Hardware Trojan Detection |
| [Fine-Grained Kernel Auditing using Augmented Syscall Reference Behavior Analysis and Virtualized Selective Tracing](https://doi.org/10.1109/SP63933.2026.00013) | Kernel Auditing |
| [Heap Localization: Cache Side-Channel based Linux Kernel Heap Exploit Techniques](https://doi.org/10.1109/SP63933.2026.00196) | Kernel Heap Exploitation |
| [RadKey: An LLM-Guided RF Backscatter System for Through-Wall Keystroke Inference](https://doi.org/10.1109/SP63933.2026.00160) | Keystroke Inference |
| [KeyTAR: Practical Keystroke Timing Attacks and Input Reconstruction](https://doi.org/10.1109/SP63933.2026.00106) | Keystroke timing attack |
| [Battering RAM: Low-Cost Interposer Attacks on Confidential Computing via Dynamic Memory Aliasing](https://doi.org/10.1109/SP63933.2026.00052) | Memory Bus Attacks |
| [TEE.fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition](https://doi.org/10.1109/SP63933.2026.00101) | Memory Bus Interposition |
| [NanoTag: Systems Support for Efficient Byte-Granular Overflow Detection on ARM MTE](https://doi.org/10.1109/SP63933.2026.00231) | Memory Tagging Extension |
| [Enter, Exit, Page Fault, Leak: Testing Isolation Boundaries for Microarchitectural Leaks](https://doi.org/10.1109/SP63933.2026.00007) | Microarchitectural isolation testing |
| [Fractal: An Operating System Designed for Microarchitecture Reverse Engineering](https://doi.org/10.1109/SP63933.2026.00141) | Microarchitecture Reverse Engineering |
| [Convenience at a Cost: The Security Risks of Template-based Development in the App-in-App Ecosystem](https://doi.org/10.1109/SP63933.2026.00074) | Mini-app template security |
| [Sealing the Window: Efficient Tamper Protection for Provenance Logs](https://doi.org/10.1109/SP63933.2026.00092) | Provenance Log Tamper Detection |
| [SoK: Systematizing a Decade of Architectural RowHammer Defenses Through the Lens of Streaming Algorithms](https://doi.org/10.1109/SP63933.2026.00114) | RowHammer Defenses |
| [AEX-NStep: Probabilistic Interrupt Counting Attacks on Intel SGX](https://doi.org/10.1109/SP63933.2026.00035) | SGX Interrupt Attacks |
| [SmuFuzz: Enable Deep System Management Mode Fuzzing in Fully Featured UEFI Runtime Environment](https://doi.org/10.1109/SP63933.2026.00011) | SMM Fuzzing |
| [Chypnosis: Undervolting-based Static Side-channel Attacks](https://doi.org/10.1109/SP63933.2026.00090) | Side-Channel Attacks |
| [VMSCAPE: Exposing and Exploiting Incomplete Branch Predictor Isolation in Cloud Environments](https://doi.org/10.1109/SP63933.2026.00046) | Speculative Execution Attacks |
| [Leafblower: a Leakage Attack Against TEE-Based Encrypted Databases](https://doi.org/10.1109/SP63933.2026.00008) | TEE Encrypted Database Attacks |
| [Rain: Transiently Leaking Data from Public Clouds Using Old Vulnerabilities](https://doi.org/10.1109/SP63933.2026.00063) | Transient Execution Attacks |
| [TREVEX: A Black-Box Detection Framework For Data-Flow Transient Execution Vulnerabilities](https://doi.org/10.1109/SP63933.2026.00135) | Transient execution detection |
| [Defeating Transient Execution Attacks by Limiting Secret Reachability through Register Hiding and ShadowCFI](https://doi.org/10.1109/SP63933.2026.00015) | Transient execution mitigation |
| [Crucible: Retrofitting Commodity CPUs with Vulnerabilities via Transparent Software Emulation](https://doi.org/10.1109/SP63933.2026.00186) | Transient execution simulation |
| [Transient Architectural Execution: From Weird Gates to Weird Programs](https://doi.org/10.1109/SP63933.2026.00066) | Transient execution weird computation |
| [TÄMU: Emulating Trusted Applications at the (GlobalPlatform)-API Layer](https://doi.org/10.1109/SP63933.2026.00139) | Trusted Application Emulation |
| [EyeSpy: Inferring Eye Gaze via Side-Channel Attacks Against Foveated Rendering](https://doi.org/10.1109/SP63933.2026.00145) | VR Eye Gaze Side-Channel Attack |
| [When VR Meets BCI: (Un)Observable Brainwave-aware Privacy Reconstruction in the Metaverse via Unrestricted Inbuilt Motion Sensors](https://doi.org/10.1109/SP63933.2026.00117) | VR side-channel attacks |

---

## Software Security

*24 papers*

| Paper | Sub-area |
|-------|----------|
| [SFA-Miner: Mining Path-Sensitive API Usage Patterns via Symbolic Finite Automata](https://doi.org/10.1109/SP63933.2026.00056) | API Usage Pattern Mining |
| [PORTGPT: Towards Automated Backporting Using Large Language Models](https://doi.org/10.1109/SP63933.2026.00034) | Automated Patch Backporting |
| [CiRCLE: Recovering Complex Data Structures in Binaries beyond Fragmentation](https://doi.org/10.1109/SP63933.2026.00146) | Binary Data Structure Recovery |
| [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://doi.org/10.1109/SP63933.2026.00211) | CLI Fuzzing |
| [Agentic Concolic Execution](https://doi.org/10.1109/SP63933.2026.00003) | Concolic Execution |
| [PLaTypus: Restricting Cross-Module Transitions to Mitigate Code-Reuse Attacks](https://doi.org/10.1109/SP63933.2026.00189) | Control-Flow Integrity Defenses |
| [Best of Both Worlds: Effective Foreign Bridge Identification in V8 Embedders for Security Analysis](https://doi.org/10.1109/SP63933.2026.00115) | Cross-language Security Analysis |
| [TrigFuzz: Triggering Conditions Guided Directed Fuzzing](https://doi.org/10.1109/SP63933.2026.00156) | Directed Fuzzing |
| [Stop Starving or Stuffing Me: Boosting Firmware Fuzzing Efficiency with On-demand Input Delivery](https://doi.org/10.1109/SP63933.2026.00155) | Firmware Fuzzing |
| [Cosseter: GitHub Actions Permission Reduction Using Demand-Driven Static Analysis](https://doi.org/10.1109/SP63933.2026.00067) | GitHub Actions Permission Analysis |
| [Crashing Through Defenses: Exploiting Segfaults and Chaining around Intel CET](https://doi.org/10.1109/SP63933.2026.00216) | Intel CET Bypass |
| [Jazzer: Coverage-Guided Fuzzing for Semantic Vulnerabilities in the Java Ecosystem](https://doi.org/10.1109/SP63933.2026.00134) | Java Fuzzing |
| [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://doi.org/10.1109/SP63933.2026.00223) | Java Vulnerability Discovery |
| [Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis](https://doi.org/10.1109/SP63933.2026.00121) | LLM-based Program Analysis |
| [Cottontail: Large Language Model-Driven Concolic Execution for Highly Structured Test Input Generation](https://doi.org/10.1109/SP63933.2026.00110) | LLM-guided Concolic Execution |
| [QuickSafe: Targeted Hardening Against Memory Corruption](https://doi.org/10.1109/SP63933.2026.00085) | Memory Safety Hardening |
| [Beyond Nodes vs. Edges: A Multi-View Fusion Framework for Provenance-Based Intrusion Detection](https://doi.org/10.1109/SP63933.2026.00242) | Multi-View Provenance-Based Intrusion Detection |
| [Fizzle: A Framework for Deterministic and Reproducible Network Fuzzing](https://doi.org/10.1109/SP63933.2026.00091) | Network protocol fuzzing |
| [Navigating Developers’ Quagmire: LLM-Enabled Privacy Compliance Analysis for SDK Integrations](https://doi.org/10.1109/SP63933.2026.00126) | Privacy compliance for SDKs |
| [A Context is Worth a Thousand Lies: Evading Intrusion Detectors via Intelligent Context Distortion](https://doi.org/10.1109/SP63933.2026.00202) | Provenance-Based IDS Evasion via Context Distortion |
| [The First Large-Scale Systematic Study of Python Class Pollution Vulnerability](https://doi.org/10.1109/SP63933.2026.00108) | Python Class Pollution |
| [PUFFERDOS: Efficient and Effective Attack String Generation for Regular Expression Denial of Service Vulnerabilities](https://doi.org/10.1109/SP63933.2026.00169) | ReDoS Attack Generation |
| [deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses](https://doi.org/10.1109/SP63933.2026.00060) | Rust Memory Safety Fuzzing |
| [zkFuzz: Foundation and Framework for Effective Fuzzing of Zero-Knowledge Circuits](https://doi.org/10.1109/SP63933.2026.00049) | ZK circuit fuzzing |

---

## Usable Security and Privacy

*20 papers*

| Paper | Sub-area |
|-------|----------|
| [Usable Anonymity in Reproductive Health Privacy](https://doi.org/10.1109/SP63933.2026.00023) | Anonymity Usability |
| [Consumer Beware! Exploring Data Brokers’ CCPA Compliance](https://doi.org/10.1109/SP63933.2026.00104) | CCPA Compliance Study |
| [When Designers Meet GenAI: Understanding the Role of Prompt-to-Design Generators in Privacy Dark Patterns](https://doi.org/10.1109/SP63933.2026.00131) | Dark Patterns in Generative Design |
| [Towards Automating Data Access Permissions in AI Agents](https://doi.org/10.1109/SP63933.2026.00018) | Data Access Permissions for AI Agents |
| [Searching for a Farang: Collective Security among Women in Pattaya, Thailand](https://doi.org/10.1109/SP63933.2026.00017) | Digital security for sex workers |
| [Setting the Course, but Forgetting to Steer: Analyzing Compliance with GDPR’s Right of Access to Data by Instagram, TikTok, and YouTube](https://doi.org/10.1109/SP63933.2026.00051) | GDPR Compliance Analysis |
| [Toward Inclusive Security and Privacy for Deaf and Hard-of-Hearing People: A Community-Based Interview Study](https://doi.org/10.1109/SP63933.2026.00027) | Inclusive S&P for DHH communities |
| [LISA: A Scale-Optimized and Psychometrically-Validated Instrument for the Lightweight Assessment of Organizational Information Security Awareness in Heterogeneous Organizations](https://doi.org/10.1109/SP63933.2026.00174) | Information security awareness measurement |
| [The Passkey Promise: A Comparative Usability Study of MFA Methods](https://doi.org/10.1109/SP63933.2026.00055) | MFA Usability |
| [No Password, No Problem? A Large-Scale Field Study of Passkey Adoption and Usage](https://doi.org/10.1109/SP63933.2026.00022) | Passkey Adoption and Usage |
| [MAYA: Addressing Inconsistencies in Generative Password Guessing through a Unified Benchmark](https://doi.org/10.1109/SP63933.2026.00081) | Password guessing evaluation |
| [Hidden Secrets in the arXiv: Discovering, Analyzing, and Preventing Unintentional Information Disclosure in Source Files of Scientific Preprints](https://doi.org/10.1109/SP63933.2026.00217) | Preprint Source Code Privacy |
| [Privacy Perspectives and Practices of Chinese Smart Home Product Teams](https://doi.org/10.1109/SP63933.2026.00014) | Privacy practices in smart home product teams |
| [Perceived Privacy Risk and Mitigation Post-Roe](https://doi.org/10.1109/SP63933.2026.00064) | Reproductive privacy behavior |
| [From "Be Careful" to "Here's Why": Investigating User Reasoning with Context-Specific SMS Scam Warnings](https://doi.org/10.1109/SP63933.2026.00200) | SMS Scam Warning Usability |
| [LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres](https://doi.org/10.1109/SP63933.2026.00111) | SOC Analyst LLM Usage |
| [International Students and Scams: At Risk Abroad](https://doi.org/10.1109/SP63933.2026.00094) | Scams Targeting International Students |
| ["I Wonder if These Warnings Are Accurate": Security and Privacy Advice in Nine Majority World Countries](https://doi.org/10.1109/SP63933.2026.00005) | Security advice in non-Western contexts |
| [Responsible Disclosure is a Two-Way Street: Empirically Measuring the Responsible Disclosure Contract in the Firmware Ecosystem](https://doi.org/10.1109/SP63933.2026.00180) | Vulnerability Disclosure Measurement |
| [Behind the Curtain: How Shared Hosting Providers Respond to Vulnerability Notifications](https://doi.org/10.1109/SP63933.2026.00036) | Vulnerability Notification Response |

---

## LLMs and AI Safety

*16 papers*

| Paper | Sub-area |
|-------|----------|
| [AI Wrote My Paper and All I Got Was This False Negative:* Measuring the Efficacy of Commercial AI Text Detectors](https://doi.org/10.1109/SP63933.2026.00088) | AI Text Detection |
| [Investigating the Impact of Dark Patterns on LLM-Based Web Agents](https://doi.org/10.1109/SP63933.2026.00042) | Dark Patterns in Web Agents |
| [GraphRAG under Fire](https://doi.org/10.1109/SP63933.2026.00070) | GraphRAG Poisoning |
| [MetaBreak: Jailbreaking Online LLM Services via Special Token Manipulation](https://doi.org/10.1109/SP63933.2026.00095) | Jailbreak Attacks |
| [URLcoat: Exploiting Web Search Capability to Jailbreak Large Language Models](https://doi.org/10.1109/SP63933.2026.00082) | Jailbreak Attacks |
| [SoK: Evaluating Jailbreak Guardrails for Large Language Models](https://doi.org/10.1109/SP63933.2026.00076) | Jailbreak Guardrails |
| [SoK: Robustness in Large Language Models against Jailbreak Attacks](https://doi.org/10.1109/SP63933.2026.00107) | Jailbreak Robustness |
| [LLM Unlearning Should Be Form-Independent](https://doi.org/10.1109/SP63933.2026.00037) | LLM Unlearning |
| [LLMThief: Evaluating Configuration Leaking Risks in Commercial LLM App Stores](https://doi.org/10.1109/SP63933.2026.00195) | LLM app configuration leakage |
| [WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers](https://doi.org/10.1109/SP63933.2026.00025) | LLM web agent security |
| [When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins](https://doi.org/10.1109/SP63933.2026.00062) | Prompt Injection Attacks |
| [PromptLocate: Localizing Prompt Injection Attacks](https://doi.org/10.1109/SP63933.2026.00105) | Prompt Injection Localization |
| [DREAM: Scalable Red Teaming for Text-to-Image Generative Systems via Distribution Modeling](https://doi.org/10.1109/SP63933.2026.00112) | Red Teaming |
| [Who Taught the Lie? Responsibility Attribution for Poisoned Knowledge in Retrieval-Augmented Generation](https://doi.org/10.1109/SP63933.2026.00053) | Retrieval-Augmented Generation Poisoning |
| [EnchTable: Unified Safety Alignment Transfer in Fine-tuned Large Language Models](https://doi.org/10.1109/SP63933.2026.00072) | Safety Alignment Transfer |
| [WRATH: Turning Watermark Robustness Against Itself via a Watermark-Agnostic Black-Box Invalidation Attack](https://doi.org/10.1109/SP63933.2026.00197) | Watermark Attacks |

---

## Network Security

*12 papers*

| Paper | Sub-area |
|-------|----------|
| [Guardians of the Air: In-Device Detection of 5G Control-Plane Threats](https://doi.org/10.1109/SP63933.2026.00204) | 5G Control-Plane Threat Detection |
| [The Threat Landscape of IP Leasing in the RPKI Era](https://doi.org/10.1109/SP63933.2026.00012) | BGP/RPKI security |
| [One Tap to Hijack Them All: A Security Analysis of the Google Fast Pair Protocol](https://doi.org/10.1109/SP63933.2026.00210) | Bluetooth Pairing Security |
| [CenAlert: Amplifying User Voices to Rally Censorship Investigation](https://doi.org/10.1109/SP63933.2026.00229) | Censorship Detection |
| [CenRL: A Framework for Performing Intelligent Censorship Measurements](https://doi.org/10.1109/SP63933.2026.00098) | Censorship Measurement |
| [Designing Transport-Level Encryption for Datacenter Networks](https://doi.org/10.1109/SP63933.2026.00080) | Datacenter network encryption |
| [Revisiting PQ WireGuard: A Comprehensive Security Analysis With a New Design Using Reinforced KEMs](https://doi.org/10.1109/SP63933.2026.00057) | Post-Quantum VPN Protocols |
| [STIR/SHAKEN: A Cocktail of Cryptographic Clumsiness](https://doi.org/10.1109/SP63933.2026.00093) | Telephone Spoofing Prevention |
| [Descriptors of Exposure: Undermining Tor Anonymity through Exploiting Descriptor Flood](https://doi.org/10.1109/SP63933.2026.00071) | Tor Descriptor Flood Exploitation |
| [SaTor: Exploring Satellite Routing in Tor to Reduce Latency](https://doi.org/10.1109/SP63933.2026.00068) | Tor Latency Reduction with Satellite Routing |
| [LeakyLinks: Measuring the Security and Privacy Risks of URL Scanning Services](https://doi.org/10.1109/SP63933.2026.00130) | URL scanning privacy risks |
| [RIS-CLA: Reviving CSI-Based Continuous Location Authentication with Reconfigurable Intelligent Surfaces](https://doi.org/10.1109/SP63933.2026.00031) | Wireless authentication |

---

## Machine Learning and Security

*11 papers*

| Paper | Sub-area |
|-------|----------|
| [MusicShield: Protection for Musicians in the Era of Generative AI](https://doi.org/10.1109/SP63933.2026.00039) | Adversarial examples for generative models |
| [Ensemble Conformal Predictor (EnCP): A New Conformal Predictor with Robustness Guarantees against Data Poisoning Attacks](https://doi.org/10.1109/SP63933.2026.00043) | Conformal Prediction Robustness |
| [Your Compiler is Backdooring Your Model: Understanding and Exploiting Compilation Inconsistency Vulnerabilities in Deep Learning Compilers](https://doi.org/10.1109/SP63933.2026.00097) | DL Compiler Backdoors |
| [Revelio: Blurred Images Can Still Disclose Your Identity](https://doi.org/10.1109/SP63933.2026.00030) | Face Deblurring Attack |
| [ARES: Scalable and Practical Gradient Inversion Attack in Federated Learning through Activation Recovery](https://doi.org/10.1109/SP63933.2026.00181) | Gradient Inversion Attack |
| [On the Detectability of Active Gradient Inversion Attacks in Federated Learning](https://doi.org/10.1109/SP63933.2026.00193) | Gradient Inversion Attack Detection |
| [On the (In)Security of Loading Machine Learning Models](https://doi.org/10.1109/SP63933.2026.00123) | Model Loading Security |
| [ Exploiting Leaderboards for Large-Scale Distribution of Poisoned Models](https://doi.org/10.1109/SP63933.2026.00044) | Model Poisoning |
| [Weaponizing Reflectivity for Pointcloud Deception with Forged Invisible Geometries](https://doi.org/10.1109/SP63933.2026.00183) | Physical Adversarial Pointcloud Attacks |
| [Are LLM-Enhanced Graph Neural Networks Robust against Poisoning Attacks?](https://doi.org/10.1109/SP63933.2026.00212) | Poisoning Robustness |
| [Shared Spotlight Meridian: Distributed Sparse Pseudorandom Functions for Scalable Federated Learning](https://doi.org/10.1109/SP63933.2026.00065) | Secure Federated Learning Aggregation |

---

## Web Security

*11 papers*

| Paper | Sub-area |
|-------|----------|
| [KeyChaser: Unveiling API Keys in Browser Extensions](https://doi.org/10.1109/SP63933.2026.00187) | API Key Detection |
| [Web Application Vulnerability Repair via Context-Aware Fault Localization and Directed Differential Fuzzing](https://doi.org/10.1109/SP63933.2026.00237) | Automated Vulnerability Repair |
| [State of Browser Process-Isolation: The Same-Site Weakness](https://doi.org/10.1109/SP63933.2026.00096) | Browser Process Isolation |
| [Breaking the Illusion: Automated Reasoning of GDPR Consent Violations](https://doi.org/10.1109/SP63933.2026.00040) | GDPR consent violation detection |
| [Poisoned by the Host: Large-Scale Measurement of Host Name Poisoning in Web Applications](https://doi.org/10.1109/SP63933.2026.00166) | Host Name Poisoning Measurement |
| [Understanding Data Collection, Brokerage, and Spam in the Lead Marketing Ecosystem](https://doi.org/10.1109/SP63933.2026.00162) | Lead Marketing Data Privacy |
| [Demystifying the (In)Security of OAuth-based Account Linking in Connector Ecosystems](https://doi.org/10.1109/SP63933.2026.00128) | OAuth Account Linking |
| [Audience Injection Attacks: A New Class of Attacks on Web-Based Authorization and Authentication Standards](https://doi.org/10.1109/SP63933.2026.00116) | OAuth/OpenID Connect Attacks |
| [Credential Extraction Attacks Against Compromised Credential Checking Services of Password Managers](https://doi.org/10.1109/SP63933.2026.00103) | Password manager security |
| [APIEcho: Training-less Anomaly Detection via Intra-API Behavioral Comparison for Web Applications](https://doi.org/10.1109/SP63933.2026.00016) | Web Anomaly Detection |
| [SoK: After Decades of Web Tracker Detection, What’s Next?](https://doi.org/10.1109/SP63933.2026.00222) | Web Tracker Detection |

---

## Blockchain and Distributed Systems

*6 papers*

| Paper | Sub-area |
|-------|----------|
| [Scalable Accountable Byzantine Agreement and Beyond](https://doi.org/10.1109/SP63933.2026.00029) | Byzantine Agreement Accountability |
| [Mechanized Safety and Liveness Proofs for the Mysticeti Consensus Protocol under the LiDO-DAG Framework](https://doi.org/10.1109/SP63933.2026.00009) | Consensus Protocol Verification |
| [A Liveness Attack to Ethereum PoS with No Additional Cost](https://doi.org/10.1109/SP63933.2026.00235) | Ethereum PoS Liveness Attack |
| [Prrr: Personal Random Rewards for Blockchain Reporting](https://doi.org/10.1109/SP63933.2026.00136) | Incentive Mechanism Design |
| [Jigsaw: Doubly Private Smart Contracts](https://doi.org/10.1109/SP63933.2026.00109) | Privacy-Preserving Smart Contracts |
| [Fast Deterministically Safe Proof-of-Work Consensus](https://doi.org/10.1109/SP63933.2026.00102) | Proof-of-Work Consensus |

---

## Formal Methods and Verification

*5 papers*

| Paper | Sub-area |
|-------|----------|
| [C-Verifier: Understanding and Formally Verifying Cross-Service Flaws in AWS Cognito](https://doi.org/10.1109/SP63933.2026.00010) | Cloud Security Verification |
| [Automated formal analysis of Signal's Double Ratchet: attacks, fixes and security proofs](https://doi.org/10.1109/SP63933.2026.00120) | Protocol Verification |
| [DY* Unchained: Now with Composable Security Proofs and Precise   Compromise Scenarios](https://doi.org/10.1109/SP63933.2026.00220) | Protocol verification |
| [The Secrets Must Not Flow: Scaling Security Verification to Large Codebases](https://doi.org/10.1109/SP63933.2026.00026) | Security Protocol Verification |
| [Language-Agnostic Detection of Computation-Constraint Inconsistencies in ZKP Programs via Value Inference](https://doi.org/10.1109/SP63933.2026.00207) | ZKP program verification |

---

## IoT and Cyber-Physical Systems

*5 papers*

| Paper | Sub-area |
|-------|----------|
| [BACHunter: Detecting Broken Access Control Vulnerabilities in Intelligent Connected Vehicles](https://doi.org/10.1109/SP63933.2026.00152) | Access Control Vulnerability Detection |
| [Bridge: High-Order Taint Vulnerabilities Detection in Linux-based IoT Firmware](https://doi.org/10.1109/SP63933.2026.00001) | Firmware Vulnerability Detection |
| [Camveil: Unveiling Security Camera Vulnerabilities through Multi-Protocol Coordinated Fuzzing](https://doi.org/10.1109/SP63933.2026.00002) | IoT fuzzing |
| [SatBleed: Security of Commoditized Communication Modules in Satellites](https://doi.org/10.1109/SP63933.2026.00213) | Satellite security |
| [2FiA: Towards WiFi Sensing-Based Authentication with Unique Biometrics](https://doi.org/10.1109/SP63933.2026.00087) | WiFi Biometric Authentication |

---

## Digital Forensics and Cybercrime

*2 papers*

| Paper | Sub-area |
|-------|----------|
| [Breaking Free from Ivory Tower: Evaluating and Enhancing Real-world Chinese Underground Adversarial Jargon Detection](https://doi.org/10.1109/SP63933.2026.00233) | Adversarial Jargon Detection |
| [PromoGuardian: Detecting Promotion Abuse Fraud with Multi-Relation Fused Graph Neural Networks](https://doi.org/10.1109/SP63933.2026.00045) | Promotion Abuse Fraud Detection |

---

## Statistics

| Category | Paper Count |
|-----------|-------------|
| Cryptography and Privacy | 50 |
| Systems Security | 37 |
| Software Security | 24 |
| Usable Security and Privacy | 20 |
| LLMs and AI Safety | 16 |
| Network Security | 12 |
| Machine Learning and Security | 11 |
| Web Security | 11 |
| Blockchain and Distributed Systems | 6 |
| Formal Methods and Verification | 5 |
| IoT and Cyber-Physical Systems | 5 |
| Digital Forensics and Cybercrime | 2 |
| **Total** | **199** |

## Sub-Area Distribution

| Sub-area | Count |
|----------|-------|
| Private Information Retrieval | 5 |
| Jailbreak Attacks | 2 |
| LLM Unlearning | 1 |
| Jailbreak Guardrails | 1 |
| Jailbreak Robustness | 1 |
| Conformal Prediction Robustness | 1 |
| Model Poisoning | 1 |
| GraphRAG Poisoning | 1 |
| AI Text Detection | 1 |
| DL Compiler Backdoors | 1 |
| Red Teaming | 1 |
| Model Loading Security | 1 |
| Watermark Attacks | 1 |
| Poisoning Robustness | 1 |
| Adversarial Jargon Detection | 1 |
| LLM web agent security | 1 |
| GPU memory attack | 1 |
| GPU ASLR analysis | 1 |
| DDR5 Rowhammer attacks | 1 |
| GPU Rowhammer attacks | 1 |
| GPU Rowhammer page table attack | 1 |
| Microarchitectural isolation testing | 1 |
| Transient execution mitigation | 1 |
| Transient execution weird computation | 1 |
| Cache side-channel mitigation | 1 |
| Keystroke timing attack | 1 |
| Transient execution detection | 1 |
| Symmetric-key cryptography design | 1 |
| Transient execution simulation | 1 |
| Cache coherence side channel | 1 |
| Security advice in non-Western contexts | 1 |
| Privacy practices in smart home product teams | 1 |
| Digital security for sex workers | 1 |
| Inclusive S&P for DHH communities | 1 |
| Private set intersection for deduplication | 1 |
| Information security awareness measurement | 1 |
| Reproductive privacy behavior | 1 |
| GDPR consent violation detection | 1 |
| Consent management in mobile apps | 1 |
| Mini-app template security | 1 |
| VR side-channel attacks | 1 |
| EMV contactless payment security | 1 |
| Privacy compliance for SDKs | 1 |
| LLM app configuration leakage | 1 |
| URL scanning privacy risks | 1 |
| Multi-Key Homomorphic Secret Sharing | 1 |
| Anonymous Tokens and Non-transferability | 1 |
| Post-Quantum VPN Protocols | 1 |
| Leakage-Abuse Attacks on Encrypted Databases | 1 |
| Post-Quantum KEM Combiners | 1 |
| Private Set Operations | 1 |
| Hardware Trojan Detection | 1 |
| Oblivious Pseudorandom Functions | 1 |
| Byzantine Agreement Accountability | 1 |
| Post-Quantum Blind Signatures | 1 |
| Asynchronous Distributed Key Generation | 1 |
| Lattice-based Threshold Blind Signatures | 1 |
| Threshold Post-Quantum Signatures | 1 |
| Threshold Anonymous Credentials | 1 |
| Functional Adaptor Signatures | 1 |
| Private Set Intersection | 1 |
| Secure Inference | 1 |
| Oblivious RAM | 1 |
| Protocol Verification | 1 |
| Transient Execution Attacks | 1 |
| Side-Channel Attacks | 1 |
| RowHammer Defenses | 1 |
| Keystroke Inference | 1 |
| Concolic Execution | 1 |
| Cloud Security Verification | 1 |
| Speculative Execution Attacks | 1 |
| LLM-based Program Analysis | 1 |
| Browser Process Isolation | 1 |
| API Key Detection | 1 |
| Security Protocol Verification | 1 |
| Consensus Protocol Verification | 1 |
| Zero-Knowledge Proofs for PSPACE | 1 |
| Succinct ZK Proofs | 1 |
| Pseudorandom Correlation Generators | 1 |
| Secure MPC with DPFs | 1 |
| Private Lookup Protocols | 1 |
| Data Reconstruction Attacks | 1 |
| GDPR Compliance Analysis | 1 |
| Privacy-Preserving GBDT | 1 |
| CCPA Compliance Study | 1 |
| Confidential Cloud State Rollback | 1 |
| Lead Marketing Data Privacy | 1 |
| Differential Privacy Utility Evaluation | 1 |
| Proof-of-Work Consensus | 1 |
| PAC Privacy Optimization | 1 |
| Privacy Amplification Shuffling | 1 |
| Differential Privacy Auditing | 1 |
| Local Differential Privacy Sparse Estimation | 1 |
| Secure Federated Learning Aggregation | 1 |
| Privacy-Preserving Smart Contracts | 1 |
| Distributed Secret Recovery | 1 |
| Gradient Inversion Attack | 1 |
| Gradient Inversion Attack Detection | 1 |
| Telephone Spoofing Prevention | 1 |
| Ethereum PoS Liveness Attack | 1 |
| Provenance Log Tamper Detection | 1 |
| Fuzzy Private Set Intersection | 1 |
| Asynchronous Secret Sharing | 1 |
| Registration-Based Encryption | 1 |
| LWE Secret Recovery with Side Information | 1 |
| Scams Targeting International Students | 1 |
| SMS Scam Warning Usability | 1 |
| Data Access Permissions for AI Agents | 1 |
| GitHub Actions Permission Analysis | 1 |
| VR Eye Gaze Side-Channel Attack | 1 |
| Tor Latency Reduction with Satellite Routing | 1 |
| Tor Descriptor Flood Exploitation | 1 |
| Provenance-Based IDS Evasion via Context Distortion | 1 |
| Multi-View Provenance-Based Intrusion Detection | 1 |
| 5G Control-Plane Threat Detection | 1 |
| BGP/RPKI security | 1 |
| IoT fuzzing | 1 |
| Datacenter network encryption | 1 |
| Network protocol fuzzing | 1 |
| Satellite security | 1 |
| Wireless authentication | 1 |
| Adversarial examples for generative models | 1 |
| Password guessing evaluation | 1 |
| Password manager security | 1 |
| Zero-knowledge proofs for ML | 1 |
| ZK circuit fuzzing | 1 |
| Server-aided zk-SNARKs | 1 |
| ZKP program verification | 1 |
| Secure multi-party computation | 1 |
| Protocol verification | 1 |
| Fully Homomorphic Encryption | 1 |
| Proactive Secret Sharing | 1 |
| Verifiable Computation | 1 |
| Local Differential Privacy | 1 |
| Asynchronous MPC | 1 |
| Cross-language Security Analysis | 1 |
| Firmware Vulnerability Detection | 1 |
| API Usage Pattern Mining | 1 |
| Safety Alignment Transfer | 1 |
| Memory Safety Hardening | 1 |
| Access Control Vulnerability Detection | 1 |
| Memory Tagging Extension | 1 |
| FHE Compilation | 1 |
| Python Class Pollution | 1 |
| LLM-guided Concolic Execution | 1 |
| Hardware Bug Detection | 1 |
| Binary Data Structure Recovery | 1 |
| Passkey Adoption and Usage | 1 |
| Anonymity Usability | 1 |
| MFA Usability | 1 |
| WiFi Biometric Authentication | 1 |
| Bluetooth Pairing Security | 1 |
| SMM Fuzzing | 1 |
| Java Fuzzing | 1 |
| CLI Fuzzing | 1 |
| Java Vulnerability Discovery | 1 |
| Rust Memory Safety Fuzzing | 1 |
| Censorship Measurement | 1 |
| Incentive Mechanism Design | 1 |
| Censorship Detection | 1 |
| Promotion Abuse Fraud Detection | 1 |
| Preprint Source Code Privacy | 1 |
| Face Deblurring Attack | 1 |
| Kernel Auditing | 1 |
| Microarchitecture Reverse Engineering | 1 |
| Firmware Fuzzing | 1 |
| ReDoS Attack Generation | 1 |
| Kernel Heap Exploitation | 1 |
| Vulnerability Disclosure Measurement | 1 |
| OAuth/OpenID Connect Attacks | 1 |
| Web Anomaly Detection | 1 |
| Automated Patch Backporting | 1 |
| Vulnerability Notification Response | 1 |
| Directed Fuzzing | 1 |
| Automated Vulnerability Repair | 1 |
| Retrieval-Augmented Generation Poisoning | 1 |
| Prompt Injection Attacks | 1 |
| Prompt Injection Localization | 1 |
| SOC Analyst LLM Usage | 1 |
| TEE Encrypted Database Attacks | 1 |
| SGX Interrupt Attacks | 1 |
| Memory Bus Attacks | 1 |
| Memory Bus Interposition | 1 |
| Electromagnetic Side Channel | 1 |
| Trusted Application Emulation | 1 |
| Dark Patterns in Web Agents | 1 |
| OAuth Account Linking | 1 |
| Dark Patterns in Generative Design | 1 |
| Web Tracker Detection | 1 |
| Eye Movement Side Channel | 1 |
| Physical Adversarial Pointcloud Attacks | 1 |
| Control-Flow Integrity Defenses | 1 |
| Intel CET Bypass | 1 |
| Host Name Poisoning Measurement | 1 |
