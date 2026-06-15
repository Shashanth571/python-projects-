print("Quiz Starting...")

question_1 = input("What is the capital of France?\n").lower()
question_2 = input("What is 2 + 2?\n").lower()
question_3 = input("What is the largest planet in our solar system?\n").lower()
question_4 = input("What is the biggest continent?\n").lower()
question_5 = input("What is the smallest country in the world?\n").lower()

score = 0

if question_1 == "paris":
    score += 1

if question_2 == "4":
    score += 1

if question_3 == "jupiter":
    score += 1

if question_4 == "asia":
    score += 1

if question_5 == "vatican city":
    score += 1

print(f"Your score is {score}/5")