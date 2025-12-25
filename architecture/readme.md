# System Architecture

![System Architecture](https://github.com/5umitpandey/IIT_Madras_Appian_AI/blob/main/architecture/Architecture.png )

## Overview
This document explains the high-level architecture of the **Just-in-Time Knowledge Retrieval System** and how each component contributes to context-aware, citation-backed decision support.

The design prioritizes:
- Enterprise realism
- Auditability
- Privacy
- Simplicity

---

## Architecture Diagram
The file `system_architecture.png` illustrates the end-to-end flow of data and decisions.

Components:
- Case Context Source
- Document Knowledge Base
- Retrieval Engine
- Language Model
- Citation Layer
- Agent Interface

---

## Component Breakdown

### 1. Case Context Layer
Represents structured case information such as:
- Claim type
- Location
- Case category

This context is used as the **primary query signal**, eliminating the need for manual search.

---

### 2. Knowledge Base
Contains:
- Policy PDFs
- SOP documents
- Regulatory guidelines

Documents are pre-processed into semantic chunks and indexed using vector embeddings.

---

### 3. Retrieval Layer
- Converts case context into semantic queries
- Retrieves the most relevant document sections
- Ensures only context-relevant content is passed forward

This reduces noise and improves answer reliability.

---

### 4. Generation Layer
- Uses a local Large Language Model (Mistral 7B)
- Generates concise, grounded answers
- Does not hallucinate beyond retrieved content

The model operates entirely offline.

---

### 5. Citation & Provenance Layer
- Attaches source document references to every answer
- Enables agents to verify information instantly
- Supports compliance and audit requirements

Citation coverage is enforced by design.

---

### 6. Agent Interface
- Displays answers alongside citations
- Designed to be embedded within existing workflows
- Eliminates context switching

For this prototype, screenshots demonstrate the interaction flow.

---

## Design Principles
- **Context-first**: The case drives retrieval, not keywords
- **Trust by design**: No answer without a source
- **Privacy-aware**: Fully local execution
- **Enterprise-ready**: Aligned with real Appian use cases

---

## Why This Architecture Works
- Reduces handling time
- Prevents missed policy updates
- Improves decision confidence
- Scales across regulated industries

---

## Future Architectural Extensions
- Appian-native UI integration
- Role-aware retrieval
- Real-time document updates
- Analytics on retrieval effectiveness
