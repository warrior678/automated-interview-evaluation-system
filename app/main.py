from fastapi import FastAPI, WebSocket

app = FastAPI(title="Automated Candidate Interview System")

INTERVIEW = {
    "Easy": [
        {
            "question": "What is Python?",
            "keywords": ["language", "programming", "interpreted"]
        },
        {
            "question": "What is a variable?",
            "keywords": ["variable", "store", "value"]
        }
    ],
    "Medium": [
        {
            "question": "Difference between list and tuple?",
            "keywords": ["mutable", "immutable", "list", "tuple"]
        },
        {
            "question": "What is a dictionary in Python?",
            "keywords": ["key", "value", "mapping"]
        }
    ],
    "Hard": [
        {
            "question": "Explain how Python manages memory.",
            "keywords": ["memory", "heap", "garbage"]
        },
        {
            "question": "What is data cleaning?",
            "keywords": ["missing", "duplicate", "clean"]
        }
    ]
}

@app.websocket("/ws/interview")
async def interview_socket(websocket: WebSocket):
    await websocket.accept()

    difficulty = "Medium"  # Easy | Medium | Hard
    questions = INTERVIEW[difficulty]

    total_score = 0
    max_score = len(questions) * 3
    strengths = []
    weaknesses = []

    await websocket.send_text(
        f"Interview started.\nDifficulty level: {difficulty}\nAnswer clearly."
    )

    for q in questions:
        await websocket.send_text(q["question"])
        answer = await websocket.receive_text()
        answer_lower = answer.lower()
        score = 0

        # Rule 1: Length
        if len(answer.strip()) > 20:
            score += 1

        # Rule 2: Keyword relevance
        if any(k in answer_lower for k in q["keywords"]):
            score += 1

        # Rule 3: Clarity
        if "." in answer or len(answer.split()) > 5:
            score += 1

        total_score += score

        if score >= 2:
            strengths.append(q["question"])
        else:
            weaknesses.append(q["question"])

        await websocket.send_text(f"Score for this answer: {score}/3")

    percentage = int((total_score / max_score) * 100)

    await websocket.send_text("\n--- INTERVIEW REPORT ---")
    await websocket.send_text(f"Total Score: {total_score}/{max_score}")
    await websocket.send_text(f"Percentage: {percentage}%")

    await websocket.send_text("\nStrengths:")
    if strengths:
        for s in strengths:
            await websocket.send_text(f"- {s}")
    else:
        await websocket.send_text("- None")

    await websocket.send_text("\nWeaknesses:")
    if weaknesses:
        for w in weaknesses:
            await websocket.send_text(f"- {w}")
    else:
        await websocket.send_text("- None")

    if percentage >= 60:
        await websocket.send_text("\nFinal Result: PASS ✅")
    else:
        await websocket.send_text("\nFinal Result: NEEDS IMPROVEMENT ❌")
