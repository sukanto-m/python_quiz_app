import webbrowser
from flask import Flask, render_template, request, redirect, url_for
import threading

app = Flask(__name__)

# Define quiz questions and choices
questions = [
    {
        "question": "What will be the output of the following code?\n\n"
                    "def outer():\n"
                    "    x = 'outer'\n"
                    "    def inner():\n"
                    "        nonlocal x\n"
                    "        x = 'inner'\n"
                    "    inner()\n"
                    "    return x\n\n"
                    "result = outer()\n"
                    "print(result)",
        "choices": ["A) 'outer'", "B) 'inner'", "C) None", "D) Error"],
        "answer": "B) 'inner'"
    },
    {
        "question": "What will be the output of the following code?\n\n"
                    "def func(a, lst=[]):\n"
                    "    lst.append(a)\n"
                    "    return lst\n\n"
                    "print(func(1))\n"
                    "print(func(2))\n"
                    "print(func(3))",
        "choices": ["A) [1] [2] [3]", "B) [1] [1, 2] [1, 2, 3]", "C) [1, 2, 3] [1, 2, 3] [1, 2, 3]", "D) Error"],
        "answer": "B) [1] [1, 2] [1, 2, 3]"
    },
    {
        "question": "What will be the output of the following code?\n\n"
                    "a = {1, 2, 3}\n"
                    "b = {3, 4, 5}\n"
                    "result = a & b\n"
                    "print(result)",
        "choices": ["A) {1, 2, 3, 4, 5}", "B) {1, 2}", "C) {3}", "D) Error"],
        "answer": "C) {3}"
    },
    {
        "question": "Which Python keyword is used to make a variable refer to the global scope within a function?",
        "choices": ["A) global", "B) nonlocal", "C) external", "D) outer"],
        "answer": "A) global"
    },
    {
        "question": "What is the output of the following code?\n\n"
                    "data = [(0, 2), (3, 1), (5, -1), (-2, 4)]\n"
                    "data.sort(key=lambda x: x[1])\n"
                    "print(data)",
        "choices": [
            "A) [(5, -1), (3, 1), (0, 2), (-2, 4)]",
            "B) [(0, 2), (3, 1), (5, -1), (-2, 4)]",
            "C) [(-2, 4), (3, 1), (0, 2), (5, -1)]",
            "D) [(3, 1), (5, -1), (0, 2), (-2, 4)]"
        ],
        "answer": "A) [(5, -1), (3, 1), (0, 2), (-2, 4)]"
    },
    # More questions can be added here if needed
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        user_answers = []
        for i, question in enumerate(questions):
            user_answer = request.form.get(f"question-{i}")
            user_answers.append(user_answer)
            if user_answer == question["answer"]:
                score += 1

        # Render result page with the score and answer review
        return render_template("result.html", score=score, total=len(questions), user_answers=user_answers, questions=questions, enumerate=enumerate)
    
    # Render the quiz page
    return render_template("quiz.html", questions=questions, enumerate=enumerate)

@app.route("/reset")
def reset():
    return redirect(url_for("quiz"))

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # Start the Flask app in a separate thread
    threading.Timer(1, open_browser).start()  # Delay added to ensure the server is ready
    app.run(debug=True)
