# Intelligent Just-in-Time Knowledge Retrieval for Case Management

![Map](https://github.com/5umitpandey/IIT_Madras_Appian_AI/blob/main/main.jpg)

## Overview
This project demonstrates a **context-aware knowledge retrieval system** designed for enterprise case management workflows such as those used in Appian.

Support agents handling high-stakes cases (insurance claims, regulatory approvals, government benefits) often need to consult multiple policy documents, SOPs, and regulations. These documents are fragmented, lengthy, and frequently updated, forcing agents to manually search across systems.

Our solution provides **Just-in-Time knowledge assistance** by automatically surfacing the most relevant policy clauses based on the active case context, along with **verifiable citations** to ensure compliance and trust.

---

## Problem Statement
- Agents must search across PDFs, SOPs, and regulations outside their workflow
- Manual search increases average handling time (AHT)
- Critical policy updates can be missed, leading to compliance risks
- Keyword-based search fails to capture contextual relevance

The core challenge is **not data availability**, but **timely and contextual access** to the right information.

---

## Solution Summary
We built a **Retrieval-Augmented Generation (RAG)** system that:
- Uses case context as the query instead of free-text search
- Retrieves semantically relevant policy clauses
- Generates concise, grounded answers
- Attaches citations to source documents for verification
- Runs entirely locally using open-source models

The system is designed to be **enterprise-friendly**, privacy-preserving, and audit-ready.

---

## High-Level Workflow
1. Case context is identified (e.g., claim type, location)
2. Relevant policy documents are semantically retrieved
3. A local language model generates a grounded response
4. Source citations are attached automatically
5. The agent verifies and proceeds without leaving the workflow

---

## Example Scenario
**Case Context**
- Claim Type: Flood  
- Location: Florida  

**System Output**
- Flood coverage clause from policy document
- State-specific regulatory guideline
- Internal SOP steps  

Each output includes a reference to the source document and section.

---

## Technology Stack
- **RAG Framework**: paper-qa
- **Local LLM**: Mistral 7B (via Ollama)
- **Embedding Model**: nomic-embed-text
- **Runtime**: CPU-only, fully local
- **Language**: Python

No cloud services or external APIs are required.

---

## Metrics and Impact (Expected)
- ⏱️ **Average Handling Time**: 30–50% reduction (expected)
- 📄 **Policy Lookup Time**: Minutes → Seconds
- 📎 **Citation Coverage**: 100% of responses include source references
- 🔍 **Retrieval Quality**: High relevance via semantic search
- 🧑‍💼 **Agent Confidence**: Reduced rechecks and escalations
---


## 📂 Repository Structure

```text
appian-just-in-time-knowledge/
├── app.py                      # Application entry point
├── requirements.txt            # Project dependencies
├── data/
│   └── sample_policies/        # Local policy documents
├── screenshots/                # UI previews
├── architecture/
│   ├── system_architecture.png # Visual system diagram
│   └── README.md               # Architecture deep-dive
└── .env.example                # Environment variable template

```

---

## 🛠️ Optional Local Setup (For Running the Demo)

### Prerequisites

* **Python:** 3.10+
* **Ollama:** Installed and configured

### One-Time Setup

Execute the following commands in your terminal:

```bash
pip install paper-qa python-dotenv
ollama pull mistral
ollama pull nomic-embed-text

```

### Run

```bash
streamlit run ui.py

```

---

## 🚀 Deployment Considerations

* **Internal Focus:** This prototype is designed for local or internal enterprise deployment.
* **Security Context:** Public cloud deployment is intentionally out of scope to reflect the data privacy constraints of real-world Appian client environments.

---

## ⚠️ Limitations

* **Not production-scaled:** Optimized for demonstration rather than high-concurrency.
* **No RBAC:** Does not currently include role-based access control.
* **Static Data:** No real-time regulatory ingestion or live data streams.

---

## 🔮 Future Enhancements

* **Workflow Integration:** Deeper connectivity with Appian process models.
* **Automated Ingestion:** Real-time policy update synchronization.
* **Reporting:** Interactive dashboards and advanced operational analytics.
