\# Automated Interview Evaluation System



\## 📌 Overview

The Automated Interview Evaluation System is a real-time backend application that simulates a technical interview, evaluates candidate responses, and generates a structured interview report.



The system is built using FastAPI and WebSockets to enable real-time, interactive communication. It is designed with a modular architecture and is \*\*AI-ready\*\*, allowing future integration with Large Language Models (LLMs).



---



\## 🚀 Features

\- Real-time interview using WebSockets

\- Difficulty levels: Easy, Medium, Hard

\- Automated answer evaluation and scoring

\- Per-question feedback

\- Final interview report with strengths and weaknesses

\- PASS / NEEDS IMPROVEMENT decision logic



---



\## 🛠️ Tech Stack

\- Python

\- FastAPI

\- WebSockets

\- Async programming

\- Rule-based evaluation engine



---



\## 🧠 Evaluation Logic

Each candidate answer is evaluated based on:

\- \*\*Answer length\*\*

\- \*\*Keyword relevance\*\*

\- \*\*Clarity of explanation\*\*



Each question is scored out of 3, and the final score determines the interview result.



---



\## ▶️ How to Run the Project



1\. Activate virtual environment:

```bash

venv\\Scripts\\activate

uvicorn app.main:app --reload 

Open the WebSocket test client (test\_ws.html) in a browser and start the interview.



