# Simple Quiz Game

questions = [
    ["What is the capital of India?", "A) Delhi", "B) Mumbai", "C) Pune", "A"],
    ["Which planet is called the Red Planet?", "A) Earth", "B) Mars", "C) Venus", "B"],
    ["2 + 3 = ?", "A) 4", "B) 6", "C) 5", "C"]
]

score = 0

for q in questions:
    print("\n" + q[0])
    print(q[1])
    print(q[2])
    print(q[3])

    answer = input("Enter your answer (A/B/C): ").upper()

    if answer == q[4]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nFinal Score:", score, "/", len(questions))