# ai-hr-assistant-swynex-internship

# Final AI Application: HR Policy Q&A Assistant (RAG Pipeline)

## 1. Project Overview & Problem Statement
* **Objective:** Build a beginner-friendly, narrow-domain AI application designed to answer employee questions strictly based on internal company HR documents.
* **Target User:** Company employees needing instant, accurate policy answers without waiting for HR tickets.
* **Data Source:** A static set of 12 critical HR policies (e.g., Leave Policy, Remote Work Guidelines).

## 2. Technical Method & Architecture
* **Model Integration:** Uses the Gemini API (`gemini-2.5-flash`) via secure environment variables (`GEMINI_API_KEY`).
* **Retrieval Mechanism:** Implements a mocked vector retrieval layer to filter document contexts before prompt injection.
* **Zero-Hallucination Guardrails:** System prompts force the model to explicitly refuse queries if the information cannot be found in the context.

## 3. Demo & Interface
* **Interface Type:** Interactive Jupyter Notebook (`hr_assistant_demo.ipynb`) featuring a command-line style text loop.
* **Error Handling:** Built-in try/catch exception handling for API connection failures and missing environment credential checks.

## 4. Limitations & Failure Cases
* **Keyword Matching Bottleneck:** Mock retrieval relies on strict keyword matching, which can cause false-negative refusals if synonyms are used (e.g., "coffee shop" vs. "remote work").
* **Temporal Math Constraints:** Static policy text lacks precise pro-ration calculation rules for partial-month start dates, risking calculation errors.

## 5. Ethics & Data Privacy Notes
* **PII Scrubbing:** All sensitive personal identifiable information (PII) is stripped from source texts before database embedding.
* **Security:** Credentials are never hardcoded; authentication is managed entirely through local environment variables or secure vault storage.
