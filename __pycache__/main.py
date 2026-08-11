from questions import questions

score = 0

print("=" * 40)
print("       WELCOME TO QUIZ GAME")
print("=" * 40)

for question, answer in questions:

    user_answer = input(question + " : ")

    if user_answer.lower() == answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", answer)
        print()

print("=" * 40)
print("Quiz Finished")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage >= 80:
    print("🏆 Excellent!")
elif percentage >= 60:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")

file = open("score.txt", "w")
file.write("Score : " + str(score) + "/" + str(len(questions)))
file.write("\nPercentage : " + str(percentage) + "%")
file.close()

print("\nScore saved successfully in score.txt")