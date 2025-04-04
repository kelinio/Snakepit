import tkinter as tk
from tkinter import messagebox
import os
import json

def load_questions():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data.json")
    print(f"Looking for data.json at: {file_path}")  # Debug line
    with open(file_path, 'r') as file:
        return json.load(file)

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.setup_ui()

    def setup_ui(self):
        self.instruction_label = tk.Label(self.root, text="", font=("Arial", 12, "italic"))
        self.instruction_label.pack(pady=5)
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=10)
        self.option_frame = tk.Frame(self.root)
        self.option_frame.pack(pady=10)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)
        self.score_label = tk.Label(self.root, text="Score: 0/0", font=("Arial", 12))
        self.score_label.pack(pady=10)
        self.display_question()

    def display_question(self):
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        self.option_vars = []
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        is_multiple = question_data["type"] == "multiple"
        if is_multiple:
            self.instruction_label.config(text="Select all that apply")
        else:
            self.instruction_label.config(text="Select one answer")
        if is_multiple:
            for option in question_data["options"]:
                var = tk.BooleanVar()
                cb = tk.Checkbutton(self.option_frame, text=option, variable=var, font=("Arial", 12))
                cb.pack(anchor="w")
                self.option_vars.append((var, option))
        else:
            var = tk.StringVar(value="")
            for option in question_data["options"]:
                rb = tk.Radiobutton(self.option_frame, text=option, variable=var, value=option, font=("Arial", 12))
                rb.pack(anchor="w")
            self.option_vars.append(var)
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.feedback_label.config(text="")

    def check_answer(self):
        question_data = self.questions[self.current_question]
        correct_answer = question_data["correct_answer"]
        is_multiple = question_data["type"] == "multiple"
        if is_multiple:
            selected = [option for var, option in self.option_vars if var.get()]
            user_answer = " ".join(selected)
        else:
            user_answer = self.option_vars[0].get()
        if user_answer == correct_answer:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Incorrect. Correct answer: {correct_answer}", fg="red")
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.score_label.config(text=f"Score: {self.score}/{self.current_question + 1}")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Your final score: {self.score}/{len(self.questions)}")
            self.root.quit()

def main():
    questions = load_questions()
    root = tk.Tk()
    root.title("CATIA V5 Quiz")
    root.geometry("1000x1000")
    app = QuizApp(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()