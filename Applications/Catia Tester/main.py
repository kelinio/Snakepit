score = 0
questions = [
    {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin", "Rome"], "correct": 0},
    {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Saturn", "Jupiter", "Uranus"], "correct": 2},
    # Add more questions here
]

for question in questions:
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")
    user_answer = int(input("Enter the number of your answer: "))
    if user_answer - 1 == question["correct"]:
        score += 1
    print()

print(f"Your final score is {score} out of {len(questions)}")