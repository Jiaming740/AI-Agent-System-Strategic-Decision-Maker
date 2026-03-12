# AI-Agent-System-Strategic-Decision-Maker (MAS-SDM)

> A multi-agent collaborative framework designed for enterprise strategic decision-making, featuring dynamic semantic alignment and task consistency protocols across heterogeneous AI agents.

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Google%20ADK%20%7C%20AutoGen-success)
![Status](https://img.shields.io/badge/Status-Prototype%20Validated-orange)

## 📖 Introduction
This repository contains the prototype code for a **5-Agent Collaborative System** specifically designed for enterprise strategic decision-making. By leveraging advanced framework designs inspired by Google ADK, AutoGen, and LangChain, this prototype validates the feasibility of complex task orchestration, dynamic semantic alignment, and task consistency protocols in multi-agent environments. 

It serves as the preliminary engineering foundation and technical proof-of-concept for related academic research in AI-driven strategic management.

## 🏗️ System Architecture
The system operates through a collaborative network of 5 heterogeneous AI Agents:

1. 🔍 **Strategic Analyst**: Handles macro-environmental perception and Retrieval-Augmented Generation (RAG) for market data.
2. 📈 **Scenario Simulator**: Executes multi-scenario modeling and game theory simulations to predict strategic outcomes.
3. 🛡️ **Risk Auditor**: Acts as the critic for logical vulnerability, compliance auditing, and adversarial stress testing.
4. 💰 **Resource Manager**: Optimizes Return on Investment (ROI) and resource allocation under given operational constraints.
5. 🧠 **Decision Controller**: Orchestrates global tasks, verifies consistency protocols, and synthesizes the final strategic blueprint.

## ⚙️ Core Technical Breakthroughs
- **Dynamic Semantic Alignment:** Standardizes cross-domain terminology (e.g., bridging financial and marketing indicators) among agents via the `SemanticAligner` module.
- **Task Consistency Protocol:** Ensures logic integrity and budget/risk compliance across heterogeneous agent outputs via the `ConsistencyProtocol`.
- **Standardized Interfaces:** All agents inherit from the `BaseStrategicAgent` class, ensuring strict input/output protocols and supporting seamless future integrations with the Model Context Protocol (MCP).

## 🚀 Quick Start

**1. Clone the repository**
```bash
git clone https://github.com/your-username/AI-Agent-System-Strategic-Decision-Maker.git
cd AI-Agent-System-Strategic-Decision-Maker
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the prototype system**
```bash
python main.py
*Note: This prototype utilizes mocked asynchronous LLM calls for immediate local demonstration. External API keys are not required to run and verify the core orchestration logic.*
```
## 👨‍💻 Author

**Jiaming**

*Research Focus: Artificial Intelligence & Strategic Management*
