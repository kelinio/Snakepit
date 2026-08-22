import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import json
import random

def correct_options(question_data):
    """Return the correct options as a list of exact option strings.

    `correct_answer` is normally a list. Older data files stored it as a single
    string holding the correct options run together, so fall back to matching
    options against that string.
    """
    correct_answer = question_data["correct_answer"]
    if isinstance(correct_answer, list):
        return correct_answer
    if question_data["type"] == "multiple":
        return [o for o in question_data["options"] if o in correct_answer]
    return [correct_answer.strip()]

def load_questions():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data.json")
    try:
        # utf-8-sig so a byte-order mark left by a Windows editor doesn't break parsing
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            questions = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Question file not found:\n{file_path}")
        raise SystemExit(1)
    except json.JSONDecodeError as e:
        messagebox.showerror("Error", f"Invalid JSON in data file:\n{e}")
        raise SystemExit(1)

    # Validate question structure
    required_keys = {"question", "options", "correct_answer", "type"}
    for i, q in enumerate(questions):
        missing = required_keys - set(q.keys())
        if missing:
            messagebox.showerror("Error", f"Question {i+1} is missing keys: {missing}")
            raise SystemExit(1)
        if q["type"] not in ("single", "multiple"):
            messagebox.showerror("Error", f"Question {i+1} has unknown type: {q['type']!r}")
            raise SystemExit(1)
        answers = correct_options(q)
        if not answers:
            messagebox.showerror("Error", f"Question {i+1} has no correct answer")
            raise SystemExit(1)
        unknown = [a for a in answers if a not in q["options"]]
        if unknown:
            messagebox.showerror("Error", f"Question {i+1} marks answers that are not options: {unknown}")
            raise SystemExit(1)

    return questions

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        random.shuffle(self.questions)
        self.setup_ui()

    def setup_ui(self):
        self.instruction_label = tk.Label(self.root, text="", font=("Arial", 20, "italic"))
        self.instruction_label.pack(pady=10)
        self.question_label = tk.Label(self.root, text="", font=("Arial", 26, "bold"), wraplength=1100)
        self.question_label.pack(pady=20)
        self.option_frame = tk.Frame(self.root)
        self.option_frame.pack(pady=15)
        self.submit_button = tk.Button(self.root, text="Submit", font=("Arial", 18), command=self.check_answer, width=15, height=2)
        self.submit_button.pack(pady=10)
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 20), wraplength=1100)
        self.feedback_label.pack(pady=10)
        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 18), command=self.next_question, state=tk.DISABLED, width=15, height=2)
        self.next_button.pack(pady=10)
        self.score_label = tk.Label(self.root, text="Score: 0/0", font=("Arial", 18))
        self.score_label.pack(pady=10)
        self.review_button = tk.Button(self.root, text="Review All Questions", font=("Arial", 18), command=self.review_mode, state=tk.DISABLED, width=22, height=2)
        self.review_button.pack(pady=10)
        self.display_question()

    def display_question(self):
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        self.option_vars = []
        question_data = self.questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question+1}. {question_data['question']}")
        is_multiple = question_data["type"] == "multiple"
        if is_multiple:
            self.instruction_label.config(text="Select all that apply")
        else:
            self.instruction_label.config(text="Select one answer")
        if is_multiple:
            for option in question_data["options"]:
                var = tk.BooleanVar()
                cb = tk.Checkbutton(self.option_frame, text=option, variable=var, font=("Arial", 20))
                cb.pack(anchor="w", padx=40, pady=6)
                self.option_vars.append((var, option))
        else:
            var = tk.StringVar(value="")
            for option in question_data["options"]:
                rb = tk.Radiobutton(self.option_frame, text=option, variable=var, value=option, font=("Arial", 20))
                rb.pack(anchor="w", padx=40, pady=6)
            self.option_vars.append(var)
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.feedback_label.config(text="")

    def check_answer(self):
        question_data = self.questions[self.current_question]
        answers = correct_options(question_data)
        is_multiple = question_data["type"] == "multiple"

        if is_multiple:
            selected = [option for var, option in self.option_vars if var.get()]
            if not selected:
                self.feedback_label.config(text="Please select at least one answer.", fg="orange")
                return
        else:
            user_answer = self.option_vars[0].get()
            if not user_answer:
                self.feedback_label.config(text="Please select an answer.", fg="orange")
                return
            selected = [user_answer]

        is_correct = set(selected) == set(answers)
        user_answer_display = ", ".join(selected)
        correct_answer_display = ", ".join(answers)

        self.user_answers.append({
            "question": question_data["question"],
            "your_answer": user_answer_display,
            "correct_answer": correct_answer_display,
            "explanation": question_data.get("explanation", ""),
            "is_correct": is_correct
        })
        if is_correct:
            self.feedback_label.config(
                text=f"Correct!\n\nExplanation:\n{question_data.get('explanation', '')}",
                fg="green"
            )
            self.score += 1
        else:
            self.feedback_label.config(
                text=f"Incorrect.\nYour answer: {user_answer_display}\nCorrect answer: {correct_answer_display}\n\nExplanation:\n{question_data.get('explanation', '')}",
                fg="red"
            )
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.score_label.config(text=f"Score: {self.score}/{self.current_question + 1}")
        if self.current_question == len(self.questions) - 1:
            self.next_button.config(text="Finish")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Your final score: {self.score}/{len(self.questions)}")
            self.review_button.config(state=tk.NORMAL)
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)

    def review_mode(self):
        review_win = tk.Toplevel(self.root)
        review_win.title("Review Mode")
        text = scrolledtext.ScrolledText(review_win, width=120, height=40, font=("Arial", 18))
        text.pack()
        for i, ua in enumerate(self.user_answers, 1):
            status = "✔️ Correct" if ua["is_correct"] else "❌ Incorrect"
            block = (
                f"Q{i}: {ua['question']}\n"
                f"Your answer: {ua['your_answer']}\n"
                f"Correct answer: {ua['correct_answer']}\n"
                f"{status}\n"
                f"Explanation: {ua['explanation']}\n"
                "--------------------------------------------------\n"
            )
            text.insert(tk.END, block)
        text.see("1.0")
        text.configure(state='disabled')

def main():
    questions = load_questions()
    root = tk.Tk()
    root.title("CATIA V5 Quiz")
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    win_w = min(1200, screen_w - 100)
    win_h = min(900, screen_h - 100)
    root.geometry(f"{win_w}x{win_h}")
    app = QuizApp(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()
